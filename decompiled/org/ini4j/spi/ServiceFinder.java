/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
final class ServiceFinder {
    private static final String SERVICES_PATH = "META-INF/services/";

    private ServiceFinder() {
    }

    static <T> T findService(Class<T> clazz) {
        try {
            return clazz.cast(ServiceFinder.findServiceClass(clazz).newInstance());
        }
        catch (Exception x) {
            throw (IllegalArgumentException)new IllegalArgumentException("Provider " + clazz.getName() + " could not be instantiated: " + x).initCause(x);
        }
    }

    static <T> Class<? extends T> findServiceClass(Class<T> clazz) throws IllegalArgumentException {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        String serviceClassName = ServiceFinder.findServiceClassName(clazz.getName());
        Class<Object> ret = clazz;
        if (serviceClassName != null) {
            try {
                ret = classLoader == null ? Class.forName(serviceClassName) : classLoader.loadClass(serviceClassName);
            }
            catch (ClassNotFoundException x) {
                throw (IllegalArgumentException)new IllegalArgumentException("Provider " + serviceClassName + " not found").initCause(x);
            }
        }
        return ret;
    }

    static String findServiceClassName(String serviceId) throws IllegalArgumentException {
        String serviceClassName = null;
        try {
            String systemProp = System.getProperty(serviceId);
            if (systemProp != null) {
                serviceClassName = systemProp;
            }
        }
        catch (SecurityException securityException) {
            // empty catch block
        }
        if (serviceClassName == null) {
            serviceClassName = ServiceFinder.loadLine(SERVICES_PATH + serviceId);
        }
        return serviceClassName;
    }

    private static String loadLine(String servicePath) {
        String ret = null;
        try {
            InputStream is = null;
            ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
            is = classLoader == null ? ClassLoader.getSystemResourceAsStream(servicePath) : classLoader.getResourceAsStream(servicePath);
            if (is != null) {
                BufferedReader rd = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                String line = rd.readLine();
                rd.close();
                if (line != null && (line = line.trim()).length() != 0) {
                    ret = line.split("\\s|#")[0];
                }
            }
        }
        catch (Exception exception) {
            // empty catch block
        }
        return ret;
    }
}

