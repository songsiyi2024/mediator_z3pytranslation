/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.io.InputStream;
import java.net.URI;
import java.net.URL;
import java.util.Properties;
import java.util.prefs.Preferences;
import java.util.prefs.PreferencesFactory;
import org.ini4j.Config;
import org.ini4j.Ini;
import org.ini4j.IniPreferences;

public class IniPreferencesFactory
implements PreferencesFactory {
    public static final String PROPERTIES = "ini4j.properties";
    public static final String KEY_USER = "org.ini4j.prefs.user";
    public static final String KEY_SYSTEM = "org.ini4j.prefs.system";
    private Preferences _system;
    private Preferences _user;

    public synchronized Preferences systemRoot() {
        if (this._system == null) {
            this._system = this.newIniPreferences(KEY_SYSTEM);
        }
        return this._system;
    }

    public synchronized Preferences userRoot() {
        if (this._user == null) {
            this._user = this.newIniPreferences(KEY_USER);
        }
        return this._user;
    }

    String getIniLocation(String key) {
        String location = Config.getSystemProperty(key);
        if (location == null) {
            try {
                Properties props = new Properties();
                props.load(Thread.currentThread().getContextClassLoader().getResourceAsStream(PROPERTIES));
                location = props.getProperty(key);
            }
            catch (Exception exception) {
                // empty catch block
            }
        }
        return location;
    }

    URL getResource(String location) throws IllegalArgumentException {
        try {
            URI uri = new URI(location);
            URL url = uri.getScheme() == null ? Thread.currentThread().getContextClassLoader().getResource(location) : uri.toURL();
            return url;
        }
        catch (Exception x) {
            throw (IllegalArgumentException)new IllegalArgumentException().initCause(x);
        }
    }

    InputStream getResourceAsStream(String location) throws IllegalArgumentException {
        try {
            return this.getResource(location).openStream();
        }
        catch (Exception x) {
            throw (IllegalArgumentException)new IllegalArgumentException().initCause(x);
        }
    }

    Preferences newIniPreferences(String key) {
        Ini ini = new Ini();
        String location = this.getIniLocation(key);
        if (location != null) {
            try {
                ini.load(this.getResourceAsStream(location));
            }
            catch (Exception x) {
                throw (IllegalArgumentException)new IllegalArgumentException().initCause(x);
            }
        }
        return new IniPreferences(ini);
    }
}

