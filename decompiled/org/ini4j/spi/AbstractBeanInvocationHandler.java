/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.beans.Introspector;
import java.beans.PropertyChangeListener;
import java.beans.PropertyChangeSupport;
import java.beans.PropertyVetoException;
import java.beans.VetoableChangeListener;
import java.beans.VetoableChangeSupport;
import java.lang.reflect.Array;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import org.ini4j.spi.BeanTool;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public abstract class AbstractBeanInvocationHandler
implements InvocationHandler {
    private static final String PROPERTY_CHANGE_LISTENER = "PropertyChangeListener";
    private static final String VETOABLE_CHANGE_LISTENER = "VetoableChangeListener";
    private static final String ADD_PREFIX = "add";
    private static final String READ_PREFIX = "get";
    private static final String REMOVE_PREFIX = "remove";
    private static final String READ_BOOLEAN_PREFIX = "is";
    private static final String WRITE_PREFIX = "set";
    private static final String HAS_PREFIX = "has";
    private PropertyChangeSupport _pcSupport;
    private Object _proxy;
    private VetoableChangeSupport _vcSupport;

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws PropertyVetoException {
        Object ret = null;
        Prefix prefix = Prefix.parse(method.getName());
        if (prefix != null) {
            String tail = prefix.getTail(method.getName());
            this.updateProxy(proxy);
            switch (prefix) {
                case READ: {
                    ret = this.getProperty(prefix.getTail(method.getName()), method.getReturnType());
                    break;
                }
                case READ_BOOLEAN: {
                    ret = this.getProperty(prefix.getTail(method.getName()), method.getReturnType());
                    break;
                }
                case WRITE: {
                    this.setProperty(tail, args[0], method.getParameterTypes()[0]);
                    break;
                }
                case HAS: {
                    ret = this.hasProperty(prefix.getTail(method.getName()));
                    break;
                }
                case ADD_CHANGE: {
                    this.addPropertyChangeListener((String)args[0], (PropertyChangeListener)args[1]);
                    break;
                }
                case ADD_VETO: {
                    this.addVetoableChangeListener((String)args[0], (VetoableChangeListener)args[1]);
                    break;
                }
                case REMOVE_CHANGE: {
                    this.removePropertyChangeListener((String)args[0], (PropertyChangeListener)args[1]);
                    break;
                }
                case REMOVE_VETO: {
                    this.removeVetoableChangeListener((String)args[0], (VetoableChangeListener)args[1]);
                    break;
                }
            }
        }
        return ret;
    }

    protected abstract Object getPropertySpi(String var1, Class<?> var2);

    protected abstract void setPropertySpi(String var1, Object var2, Class<?> var3);

    protected abstract boolean hasPropertySpi(String var1);

    protected synchronized Object getProperty(String property, Class<?> clazz) {
        Object o;
        try {
            o = this.getPropertySpi(property, clazz);
            if (o == null) {
                o = this.zero(clazz);
            } else if (clazz.isArray() && o instanceof String[] && !clazz.equals(String[].class)) {
                String[] str = (String[])o;
                o = Array.newInstance(clazz.getComponentType(), str.length);
                for (int i = 0; i < str.length; ++i) {
                    Array.set(o, i, this.parse(str[i], clazz.getComponentType()));
                }
            } else if (o instanceof String && !clazz.equals(String.class)) {
                o = this.parse((String)o, clazz);
            }
        }
        catch (Exception x) {
            o = this.zero(clazz);
        }
        return o;
    }

    protected synchronized void setProperty(String property, Object value, Class<?> clazz) throws PropertyVetoException {
        Object newVal;
        boolean pc = this._pcSupport != null && this._pcSupport.hasListeners(property);
        boolean vc = this._vcSupport != null && this._vcSupport.hasListeners(property);
        Object oldVal = null;
        Object object = newVal = value != null && clazz.equals(String.class) && !(value instanceof String) ? value.toString() : value;
        if (pc || vc) {
            oldVal = this.getProperty(property, clazz);
        }
        if (vc) {
            this.fireVetoableChange(property, oldVal, value);
        }
        this.setPropertySpi(property, newVal, clazz);
        if (pc) {
            this.firePropertyChange(property, oldVal, value);
        }
    }

    protected synchronized Object getProxy() {
        return this._proxy;
    }

    protected synchronized void addPropertyChangeListener(String property, PropertyChangeListener listener) {
        if (this._pcSupport == null) {
            this._pcSupport = new PropertyChangeSupport(this._proxy);
        }
        this._pcSupport.addPropertyChangeListener(property, listener);
    }

    protected synchronized void addVetoableChangeListener(String property, VetoableChangeListener listener) {
        if (this._vcSupport == null) {
            this._vcSupport = new VetoableChangeSupport(this._proxy);
        }
        this._vcSupport.addVetoableChangeListener(property, listener);
    }

    protected synchronized void firePropertyChange(String property, Object oldValue, Object newValue) {
        if (this._pcSupport != null) {
            this._pcSupport.firePropertyChange(property, oldValue, newValue);
        }
    }

    protected synchronized void fireVetoableChange(String property, Object oldValue, Object newValue) throws PropertyVetoException {
        if (this._vcSupport != null) {
            this._vcSupport.fireVetoableChange(property, oldValue, newValue);
        }
    }

    protected synchronized boolean hasProperty(String property) {
        boolean ret;
        try {
            ret = this.hasPropertySpi(property);
        }
        catch (Exception x) {
            ret = false;
        }
        return ret;
    }

    protected Object parse(String value, Class<?> clazz) throws IllegalArgumentException {
        return BeanTool.getInstance().parse(value, clazz);
    }

    protected synchronized void removePropertyChangeListener(String property, PropertyChangeListener listener) {
        if (this._pcSupport != null) {
            this._pcSupport.removePropertyChangeListener(property, listener);
        }
    }

    protected synchronized void removeVetoableChangeListener(String property, VetoableChangeListener listener) {
        if (this._vcSupport != null) {
            this._vcSupport.removeVetoableChangeListener(property, listener);
        }
    }

    protected Object zero(Class<?> clazz) {
        return BeanTool.getInstance().zero(clazz);
    }

    private synchronized void updateProxy(Object value) {
        if (this._proxy == null) {
            this._proxy = value;
        }
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    private static enum Prefix {
        READ("get"),
        READ_BOOLEAN("is"),
        WRITE("set"),
        ADD_CHANGE("addPropertyChangeListener"),
        ADD_VETO("addVetoableChangeListener"),
        REMOVE_CHANGE("removePropertyChangeListener"),
        REMOVE_VETO("removeVetoableChangeListener"),
        HAS("has");

        private int _len;
        private String _value;

        private Prefix(String value) {
            this._value = value;
            this._len = value.length();
        }

        public static Prefix parse(String str) {
            Prefix ret = null;
            for (Prefix p : Prefix.values()) {
                if (!str.startsWith(p.getValue())) continue;
                ret = p;
                break;
            }
            return ret;
        }

        public String getTail(String input) {
            return Introspector.decapitalize(input.substring(this._len));
        }

        public String getValue() {
            return this._value;
        }
    }
}

