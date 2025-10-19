/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.lang.reflect.Array;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.ini4j.CommonMultiMap;
import org.ini4j.Config;
import org.ini4j.OptionMap;
import org.ini4j.spi.BeanAccess;
import org.ini4j.spi.BeanTool;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public class BasicOptionMap
extends CommonMultiMap<String, String>
implements OptionMap {
    private static final char SUBST_CHAR = '$';
    private static final String SYSTEM_PROPERTY_PREFIX = "@prop/";
    private static final String ENVIRONMENT_PREFIX = "@env/";
    private static final int SYSTEM_PROPERTY_PREFIX_LEN = "@prop/".length();
    private static final int ENVIRONMENT_PREFIX_LEN = "@env/".length();
    private static final Pattern EXPRESSION = Pattern.compile("(?<!\\\\)\\$\\{(([^\\[\\}]+)(\\[([0-9]+)\\])?)\\}");
    private static final int G_OPTION = 2;
    private static final int G_INDEX = 4;
    private static final long serialVersionUID = 325469712293707584L;
    private BeanAccess _defaultBeanAccess;
    private final boolean _propertyFirstUpper;

    public BasicOptionMap() {
        this(false);
    }

    public BasicOptionMap(boolean propertyFirstUpper) {
        this._propertyFirstUpper = propertyFirstUpper;
    }

    @Override
    public <T> T getAll(Object key, Class<T> clazz) {
        this.requireArray(clazz);
        Object value = Array.newInstance(clazz.getComponentType(), this.length(key));
        for (int i = 0; i < this.length(key); ++i) {
            Array.set(value, i, BeanTool.getInstance().parse((String)this.get(key, i), clazz.getComponentType()));
        }
        return (T)value;
    }

    @Override
    public void add(String key, Object value) {
        super.add(key, value == null || value instanceof String ? (String)value : String.valueOf(value));
    }

    @Override
    public void add(String key, Object value, int index) {
        super.add(key, value == null || value instanceof String ? (String)value : String.valueOf(value), index);
    }

    @Override
    public <T> T as(Class<T> clazz) {
        return BeanTool.getInstance().proxy(clazz, this.getDefaultBeanAccess());
    }

    @Override
    public <T> T as(Class<T> clazz, String keyPrefix) {
        return BeanTool.getInstance().proxy(clazz, this.newBeanAccess(keyPrefix));
    }

    @Override
    public String fetch(Object key) {
        int len = this.length(key);
        return len == 0 ? null : this.fetch(key, len - 1);
    }

    @Override
    public String fetch(Object key, String defaultValue) {
        String str = (String)this.get(key);
        return str == null ? defaultValue : str;
    }

    @Override
    public String fetch(Object key, int index) {
        String value = (String)this.get(key, index);
        if (value != null && value.indexOf(36) >= 0) {
            StringBuilder buffer = new StringBuilder(value);
            this.resolve(buffer);
            value = buffer.toString();
        }
        return value;
    }

    @Override
    public <T> T fetch(Object key, Class<T> clazz) {
        return BeanTool.getInstance().parse(this.fetch(key), clazz);
    }

    @Override
    public <T> T fetch(Object key, Class<T> clazz, T defaultValue) {
        String str = this.fetch(key);
        return str == null ? defaultValue : BeanTool.getInstance().parse(str, clazz);
    }

    @Override
    public <T> T fetch(Object key, int index, Class<T> clazz) {
        return BeanTool.getInstance().parse(this.fetch(key, index), clazz);
    }

    @Override
    public <T> T fetchAll(Object key, Class<T> clazz) {
        this.requireArray(clazz);
        Object value = Array.newInstance(clazz.getComponentType(), this.length(key));
        for (int i = 0; i < this.length(key); ++i) {
            Array.set(value, i, BeanTool.getInstance().parse(this.fetch(key, i), clazz.getComponentType()));
        }
        return (T)value;
    }

    @Override
    public void from(Object bean) {
        BeanTool.getInstance().inject(this.getDefaultBeanAccess(), bean);
    }

    @Override
    public void from(Object bean, String keyPrefix) {
        BeanTool.getInstance().inject(this.newBeanAccess(keyPrefix), bean);
    }

    @Override
    public <T> T get(Object key, Class<T> clazz) {
        return BeanTool.getInstance().parse((String)this.get(key), clazz);
    }

    @Override
    public String get(Object key, String defaultValue) {
        String str = (String)this.get(key);
        return str == null ? defaultValue : str;
    }

    @Override
    public <T> T get(Object key, Class<T> clazz, T defaultValue) {
        String str = (String)this.get(key);
        return str == null ? defaultValue : BeanTool.getInstance().parse(str, clazz);
    }

    @Override
    public <T> T get(Object key, int index, Class<T> clazz) {
        return BeanTool.getInstance().parse((String)this.get(key, index), clazz);
    }

    @Override
    public String put(String key, Object value) {
        return super.put(key, value == null || value instanceof String ? (String)value : String.valueOf(value));
    }

    @Override
    public String put(String key, Object value, int index) {
        return super.put(key, value == null || value instanceof String ? (String)value : String.valueOf(value), index);
    }

    @Override
    public void putAll(String key, Object value) {
        if (value != null) {
            this.requireArray(value.getClass());
        }
        this.remove(key);
        if (value != null) {
            int n = Array.getLength(value);
            for (int i = 0; i < n; ++i) {
                this.add(key, Array.get(value, i));
            }
        }
    }

    @Override
    public void to(Object bean) {
        BeanTool.getInstance().inject(bean, this.getDefaultBeanAccess());
    }

    @Override
    public void to(Object bean, String keyPrefix) {
        BeanTool.getInstance().inject(bean, this.newBeanAccess(keyPrefix));
    }

    synchronized BeanAccess getDefaultBeanAccess() {
        if (this._defaultBeanAccess == null) {
            this._defaultBeanAccess = this.newBeanAccess();
        }
        return this._defaultBeanAccess;
    }

    boolean isPropertyFirstUpper() {
        return this._propertyFirstUpper;
    }

    BeanAccess newBeanAccess() {
        return new Access();
    }

    BeanAccess newBeanAccess(String propertyNamePrefix) {
        return new Access(propertyNamePrefix);
    }

    void resolve(StringBuilder buffer) {
        Matcher m = EXPRESSION.matcher(buffer);
        while (m.find()) {
            String value;
            int index;
            String name = m.group(2);
            int n = index = m.group(4) == null ? -1 : Integer.parseInt(m.group(4));
            if (name.startsWith(ENVIRONMENT_PREFIX)) {
                value = Config.getEnvironment(name.substring(ENVIRONMENT_PREFIX_LEN));
            } else if (name.startsWith(SYSTEM_PROPERTY_PREFIX)) {
                value = Config.getSystemProperty(name.substring(SYSTEM_PROPERTY_PREFIX_LEN));
            } else {
                String string = value = index == -1 ? this.fetch(name) : this.fetch((Object)name, index);
            }
            if (value == null) continue;
            buffer.replace(m.start(), m.end(), value);
            m.reset(buffer);
        }
    }

    private void requireArray(Class clazz) {
        if (!clazz.isArray()) {
            throw new IllegalArgumentException("Array required");
        }
    }

    class Access
    implements BeanAccess {
        private final String _prefix;

        Access() {
            this(null);
        }

        Access(String prefix) {
            this._prefix = prefix;
        }

        public void propAdd(String propertyName, String value) {
            BasicOptionMap.this.add(this.transform(propertyName), value);
        }

        public String propDel(String propertyName) {
            return (String)BasicOptionMap.this.remove(this.transform(propertyName));
        }

        public String propGet(String propertyName) {
            return BasicOptionMap.this.fetch(this.transform(propertyName));
        }

        public String propGet(String propertyName, int index) {
            return BasicOptionMap.this.fetch((Object)this.transform(propertyName), index);
        }

        public int propLength(String propertyName) {
            return BasicOptionMap.this.length(this.transform(propertyName));
        }

        public String propSet(String propertyName, String value) {
            return BasicOptionMap.this.put(this.transform(propertyName), value);
        }

        public String propSet(String propertyName, String value, int index) {
            return BasicOptionMap.this.put(this.transform(propertyName), value, index);
        }

        private String transform(String orig) {
            String ret = orig;
            if ((this._prefix != null || BasicOptionMap.this.isPropertyFirstUpper()) && orig != null) {
                StringBuilder buff = new StringBuilder();
                if (this._prefix != null) {
                    buff.append(this._prefix);
                }
                if (BasicOptionMap.this.isPropertyFirstUpper()) {
                    buff.append(Character.toUpperCase(orig.charAt(0)));
                    buff.append(orig.substring(1));
                } else {
                    buff.append(orig);
                }
                ret = buff.toString();
            }
            return ret;
        }
    }
}

