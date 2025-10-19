/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.lang.reflect.Array;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Proxy;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import org.ini4j.BasicProfileSection;
import org.ini4j.CommonMultiMap;
import org.ini4j.Config;
import org.ini4j.Profile;
import org.ini4j.spi.AbstractBeanInvocationHandler;
import org.ini4j.spi.BeanTool;
import org.ini4j.spi.IniHandler;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public class BasicProfile
extends CommonMultiMap<String, Profile.Section>
implements Profile {
    private static final String SECTION_SYSTEM_PROPERTIES = "@prop";
    private static final String SECTION_ENVIRONMENT = "@env";
    private static final Pattern EXPRESSION = Pattern.compile("(?<!\\\\)\\$\\{(([^\\[\\}]+)(\\[([0-9]+)\\])?/)?([^\\[^/\\}]+)(\\[(([0-9]+))\\])?\\}");
    private static final int G_SECTION = 2;
    private static final int G_SECTION_IDX = 4;
    private static final int G_OPTION = 5;
    private static final int G_OPTION_IDX = 7;
    private static final long serialVersionUID = -1817521505004015256L;
    private String _comment;
    private final boolean _propertyFirstUpper;
    private final boolean _treeMode;

    public BasicProfile() {
        this(false, false);
    }

    public BasicProfile(boolean treeMode, boolean propertyFirstUpper) {
        this._treeMode = treeMode;
        this._propertyFirstUpper = propertyFirstUpper;
    }

    @Override
    public String getComment() {
        return this._comment;
    }

    @Override
    public void setComment(String value) {
        this._comment = value;
    }

    @Override
    public Profile.Section add(String name) {
        String parent;
        int idx;
        if (this.isTreeMode() && (idx = name.lastIndexOf(this.getPathSeparator())) > 0 && !this.containsKey(parent = name.substring(0, idx))) {
            this.add(parent);
        }
        Profile.Section section = this.newSection(name);
        this.add(name, section);
        return section;
    }

    @Override
    public void add(String section, String option, Object value) {
        this.getOrAdd(section).add(option, value);
    }

    @Override
    public <T> T as(Class<T> clazz) {
        return this.as(clazz, null);
    }

    @Override
    public <T> T as(Class<T> clazz, String prefix) {
        return clazz.cast(Proxy.newProxyInstance(Thread.currentThread().getContextClassLoader(), new Class[]{clazz}, (InvocationHandler)new BeanInvocationHandler(prefix)));
    }

    @Override
    public String fetch(Object sectionName, Object optionName) {
        Profile.Section sec = (Profile.Section)this.get(sectionName);
        return sec == null ? null : sec.fetch(optionName);
    }

    @Override
    public <T> T fetch(Object sectionName, Object optionName, Class<T> clazz) {
        Profile.Section sec = (Profile.Section)this.get(sectionName);
        return sec == null ? BeanTool.getInstance().zero(clazz) : sec.fetch(optionName, clazz);
    }

    @Override
    public String get(Object sectionName, Object optionName) {
        Profile.Section sec = (Profile.Section)this.get(sectionName);
        return sec == null ? null : (String)sec.get(optionName);
    }

    @Override
    public <T> T get(Object sectionName, Object optionName, Class<T> clazz) {
        Profile.Section sec = (Profile.Section)this.get(sectionName);
        return sec == null ? BeanTool.getInstance().zero(clazz) : sec.get(optionName, clazz);
    }

    @Override
    public String put(String sectionName, String optionName, Object value) {
        return this.getOrAdd(sectionName).put(optionName, value);
    }

    @Override
    public Profile.Section remove(Profile.Section section) {
        return (Profile.Section)this.remove(section.getName());
    }

    @Override
    public String remove(Object sectionName, Object optionName) {
        Profile.Section sec = (Profile.Section)this.get(sectionName);
        return sec == null ? null : (String)sec.remove(optionName);
    }

    boolean isTreeMode() {
        return this._treeMode;
    }

    char getPathSeparator() {
        return '/';
    }

    boolean isPropertyFirstUpper() {
        return this._propertyFirstUpper;
    }

    Profile.Section newSection(String name) {
        return new BasicProfileSection(this, name);
    }

    void resolve(StringBuilder buffer, Profile.Section owner) {
        Matcher m = EXPRESSION.matcher(buffer);
        while (m.find()) {
            String sectionName = m.group(2);
            String optionName = m.group(5);
            int optionIndex = this.parseOptionIndex(m);
            Profile.Section section = this.parseSection(m, owner);
            String value = null;
            if (SECTION_ENVIRONMENT.equals(sectionName)) {
                value = Config.getEnvironment(optionName);
            } else if (SECTION_SYSTEM_PROPERTIES.equals(sectionName)) {
                value = Config.getSystemProperty(optionName);
            } else if (section != null) {
                String string = value = optionIndex == -1 ? section.fetch(optionName) : section.fetch((Object)optionName, optionIndex);
            }
            if (value == null) continue;
            buffer.replace(m.start(), m.end(), value);
            m.reset(buffer);
        }
    }

    void store(IniHandler formatter) {
        formatter.startIni();
        this.store(formatter, this.getComment());
        for (Profile.Section s : this.values()) {
            this.store(formatter, s);
        }
        formatter.endIni();
    }

    void store(IniHandler formatter, Profile.Section s) {
        this.store(formatter, this.getComment(s.getName()));
        formatter.startSection(s.getName());
        for (String name : s.keySet()) {
            this.store(formatter, s, name);
        }
        formatter.endSection();
    }

    void store(IniHandler formatter, String comment) {
        formatter.handleComment(comment);
    }

    void store(IniHandler formatter, Profile.Section section, String option) {
        this.store(formatter, section.getComment(option));
        int n = section.length(option);
        for (int i = 0; i < n; ++i) {
            this.store(formatter, section, option, i);
        }
    }

    void store(IniHandler formatter, Profile.Section section, String option, int index) {
        formatter.handleOption(option, (String)section.get((Object)option, index));
    }

    private Profile.Section getOrAdd(String sectionName) {
        Profile.Section section = (Profile.Section)this.get(sectionName);
        return section == null ? this.add(sectionName) : section;
    }

    private int parseOptionIndex(Matcher m) {
        return m.group(7) == null ? -1 : Integer.parseInt(m.group(7));
    }

    private Profile.Section parseSection(Matcher m, Profile.Section owner) {
        String sectionName = m.group(2);
        int sectionIndex = this.parseSectionIndex(m);
        return sectionName == null ? owner : (sectionIndex == -1 ? (Profile.Section)this.get(sectionName) : (Profile.Section)this.get((Object)sectionName, sectionIndex));
    }

    private int parseSectionIndex(Matcher m) {
        return m.group(4) == null ? -1 : Integer.parseInt(m.group(4));
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    private final class BeanInvocationHandler
    extends AbstractBeanInvocationHandler {
        private final String _prefix;

        private BeanInvocationHandler(String prefix) {
            this._prefix = prefix;
        }

        @Override
        protected Object getPropertySpi(String property, Class<?> clazz) {
            String key = this.transform(property);
            Object o = null;
            if (BasicProfile.this.containsKey(key)) {
                if (clazz.isArray()) {
                    o = Array.newInstance(clazz.getComponentType(), BasicProfile.this.length(key));
                    for (int i = 0; i < BasicProfile.this.length(key); ++i) {
                        Array.set(o, i, ((Profile.Section)BasicProfile.this.get((Object)key, i)).as(clazz.getComponentType()));
                    }
                } else {
                    o = ((Profile.Section)BasicProfile.this.get(key)).as(clazz);
                }
            }
            return o;
        }

        @Override
        protected void setPropertySpi(String property, Object value, Class<?> clazz) {
            String key = this.transform(property);
            BasicProfile.this.remove(key);
            if (value != null) {
                if (clazz.isArray()) {
                    for (int i = 0; i < Array.getLength(value); ++i) {
                        Profile.Section sec = BasicProfile.this.add(key);
                        sec.from(Array.get(value, i));
                    }
                } else {
                    Profile.Section sec = BasicProfile.this.add(key);
                    sec.from(value);
                }
            }
        }

        @Override
        protected boolean hasPropertySpi(String property) {
            return BasicProfile.this.containsKey(this.transform(property));
        }

        String transform(String property) {
            String ret;
            String string = ret = this._prefix == null ? property : this._prefix + property;
            if (BasicProfile.this.isPropertyFirstUpper()) {
                StringBuilder buff = new StringBuilder();
                buff.append(Character.toUpperCase(property.charAt(0)));
                buff.append(property.substring(1));
                ret = buff.toString();
            }
            return ret;
        }
    }
}

