/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.beans.IntrospectionException;
import java.beans.Introspector;
import java.beans.PropertyDescriptor;
import java.io.File;
import java.lang.reflect.Array;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.net.URI;
import java.net.URL;
import java.util.TimeZone;
import org.ini4j.spi.AbstractBeanInvocationHandler;
import org.ini4j.spi.BeanAccess;
import org.ini4j.spi.ServiceFinder;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public class BeanTool {
    private static final String PARSE_METHOD = "valueOf";
    private static final BeanTool INSTANCE = ServiceFinder.findService(BeanTool.class);

    public static final BeanTool getInstance() {
        return INSTANCE;
    }

    public void inject(Object bean, BeanAccess props) {
        for (PropertyDescriptor pd : this.getPropertyDescriptors(bean.getClass())) {
            try {
                Object value;
                Method method = pd.getWriteMethod();
                String name = pd.getName();
                if (method == null || props.propLength(name) == 0) continue;
                if (pd.getPropertyType().isArray()) {
                    value = Array.newInstance(pd.getPropertyType().getComponentType(), props.propLength(name));
                    for (int i = 0; i < props.propLength(name); ++i) {
                        Array.set(value, i, this.parse(props.propGet(name, i), pd.getPropertyType().getComponentType()));
                    }
                } else {
                    value = this.parse(props.propGet(name), pd.getPropertyType());
                }
                method.invoke(bean, value);
            }
            catch (Exception x) {
                throw (IllegalArgumentException)new IllegalArgumentException("Failed to set property: " + pd.getDisplayName()).initCause(x);
            }
        }
    }

    public void inject(BeanAccess props, Object bean) {
        for (PropertyDescriptor pd : this.getPropertyDescriptors(bean.getClass())) {
            try {
                Object value;
                Method method = pd.getReadMethod();
                if (method == null || "class".equals(pd.getName()) || (value = method.invoke(bean, (Object[])null)) == null) continue;
                if (pd.getPropertyType().isArray()) {
                    for (int i = 0; i < Array.getLength(value); ++i) {
                        Object v = Array.get(value, i);
                        if (v != null && !v.getClass().equals(String.class)) {
                            v = v.toString();
                        }
                        props.propAdd(pd.getName(), (String)v);
                    }
                    continue;
                }
                props.propSet(pd.getName(), value.toString());
            }
            catch (Exception x) {
                throw new IllegalArgumentException("Failed to set property: " + pd.getDisplayName(), x);
            }
        }
    }

    public <T> T parse(String value, Class<T> clazz) throws IllegalArgumentException {
        if (clazz == null) {
            throw new IllegalArgumentException("null argument");
        }
        Object o = null;
        o = value == null ? (Object)this.zero(clazz) : (clazz.isPrimitive() ? this.parsePrimitiveValue(value, clazz) : (clazz == String.class ? value : (clazz == Character.class ? new Character(value.charAt(0)) : this.parseSpecialValue(value, clazz))));
        return (T)o;
    }

    public <T> T proxy(Class<T> clazz, BeanAccess props) {
        return clazz.cast(Proxy.newProxyInstance(Thread.currentThread().getContextClassLoader(), new Class[]{clazz}, (InvocationHandler)new BeanInvocationHandler(props)));
    }

    public <T> T zero(Class<T> clazz) {
        Comparable<Boolean> o = null;
        if (clazz.isPrimitive()) {
            if (clazz == Boolean.TYPE) {
                o = Boolean.FALSE;
            } else if (clazz == Byte.TYPE) {
                o = (byte)0;
            } else if (clazz == Character.TYPE) {
                o = new Character('\u0000');
            } else if (clazz == Double.TYPE) {
                o = new Double(0.0);
            } else if (clazz == Float.TYPE) {
                o = new Float(0.0f);
            } else if (clazz == Integer.TYPE) {
                o = 0;
            } else if (clazz == Long.TYPE) {
                o = 0L;
            } else if (clazz == Short.TYPE) {
                o = (short)0;
            }
        }
        return (T)o;
    }

    protected Object parseSpecialValue(String value, Class clazz) throws IllegalArgumentException {
        Object o;
        try {
            if (clazz == File.class) {
                o = new File(value);
            } else if (clazz == URL.class) {
                o = new URL(value);
            } else if (clazz == URI.class) {
                o = new URI(value);
            } else if (clazz == Class.class) {
                o = Class.forName(value);
            } else if (clazz == TimeZone.class) {
                o = TimeZone.getTimeZone(value);
            } else {
                Method parser = clazz.getMethod(PARSE_METHOD, String.class);
                o = parser.invoke(null, value);
            }
        }
        catch (Exception x) {
            throw (IllegalArgumentException)new IllegalArgumentException().initCause(x);
        }
        return o;
    }

    private PropertyDescriptor[] getPropertyDescriptors(Class clazz) {
        try {
            return Introspector.getBeanInfo(clazz).getPropertyDescriptors();
        }
        catch (IntrospectionException x) {
            throw new IllegalArgumentException(x);
        }
    }

    private Object parsePrimitiveValue(String value, Class clazz) throws IllegalArgumentException {
        Comparable<Boolean> o = null;
        try {
            if (clazz == Boolean.TYPE) {
                o = Boolean.valueOf(value);
            } else if (clazz == Byte.TYPE) {
                o = Byte.valueOf(value);
            } else if (clazz == Character.TYPE) {
                o = new Character(value.charAt(0));
            } else if (clazz == Double.TYPE) {
                o = Double.valueOf(value);
            } else if (clazz == Float.TYPE) {
                o = Float.valueOf(value);
            } else if (clazz == Integer.TYPE) {
                o = Integer.valueOf(value);
            } else if (clazz == Long.TYPE) {
                o = Long.valueOf(value);
            } else if (clazz == Short.TYPE) {
                o = Short.valueOf(value);
            }
        }
        catch (Exception x) {
            throw (IllegalArgumentException)new IllegalArgumentException().initCause(x);
        }
        return o;
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    static class BeanInvocationHandler
    extends AbstractBeanInvocationHandler {
        private final BeanAccess _backend;

        BeanInvocationHandler(BeanAccess backend) {
            this._backend = backend;
        }

        @Override
        protected Object getPropertySpi(String property, Class<?> clazz) {
            String[] ret = null;
            if (clazz.isArray()) {
                int length = this._backend.propLength(property);
                if (length != 0) {
                    String[] all = new String[length];
                    for (int i = 0; i < all.length; ++i) {
                        all[i] = this._backend.propGet(property, i);
                    }
                    ret = all;
                }
            } else {
                ret = this._backend.propGet(property);
            }
            return ret;
        }

        @Override
        protected void setPropertySpi(String property, Object value, Class<?> clazz) {
            if (clazz.isArray()) {
                this._backend.propDel(property);
                for (int i = 0; i < Array.getLength(value); ++i) {
                    this._backend.propAdd(property, Array.get(value, i).toString());
                }
            } else {
                this._backend.propSet(property, value.toString());
            }
        }

        @Override
        protected boolean hasPropertySpi(String property) {
            return this._backend.propLength(property) != 0;
        }
    }
}

