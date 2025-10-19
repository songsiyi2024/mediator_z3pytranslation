/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.net.URL;
import java.util.ArrayList;
import java.util.prefs.AbstractPreferences;
import java.util.prefs.BackingStoreException;
import org.ini4j.Ini;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.Profile;

public class IniPreferences
extends AbstractPreferences {
    private static final String[] EMPTY = new String[0];
    private final Ini _ini;

    public IniPreferences(Ini ini) {
        super(null, "");
        this._ini = ini;
    }

    public IniPreferences(Reader input) throws IOException, InvalidFileFormatException {
        super(null, "");
        this._ini = new Ini(input);
    }

    public IniPreferences(InputStream input) throws IOException, InvalidFileFormatException {
        super(null, "");
        this._ini = new Ini(input);
    }

    public IniPreferences(URL input) throws IOException, InvalidFileFormatException {
        super(null, "");
        this._ini = new Ini(input);
    }

    protected Ini getIni() {
        return this._ini;
    }

    protected String getSpi(String key) throws UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    protected String[] childrenNamesSpi() throws BackingStoreException {
        ArrayList<String> names = new ArrayList<String>();
        for (String name : this._ini.keySet()) {
            if (name.indexOf(this._ini.getPathSeparator()) >= 0) continue;
            names.add(name);
        }
        return names.toArray(EMPTY);
    }

    protected SectionPreferences childSpi(String name) {
        boolean isNew;
        Profile.Section sec = (Profile.Section)this._ini.get(name);
        boolean bl = isNew = sec == null;
        if (isNew) {
            sec = this._ini.add(name);
        }
        return new SectionPreferences(this, sec, isNew);
    }

    protected void flushSpi() throws BackingStoreException {
    }

    protected String[] keysSpi() throws BackingStoreException {
        return EMPTY;
    }

    protected void putSpi(String key, String value) throws UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    protected void removeNodeSpi() throws BackingStoreException, UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    protected void removeSpi(String key) throws UnsupportedOperationException {
        throw new UnsupportedOperationException();
    }

    protected void syncSpi() throws BackingStoreException {
    }

    protected class SectionPreferences
    extends AbstractPreferences {
        private final Profile.Section _section;

        SectionPreferences(AbstractPreferences parent, Profile.Section section, boolean isNew) {
            super(parent, section.getSimpleName());
            this._section = section;
            this.newNode = isNew;
        }

        public void flush() throws BackingStoreException {
            this.parent().flush();
        }

        public void sync() throws BackingStoreException {
            this.parent().sync();
        }

        protected String getSpi(String key) {
            return this._section.fetch(key);
        }

        protected String[] childrenNamesSpi() throws BackingStoreException {
            return this._section.childrenNames();
        }

        protected SectionPreferences childSpi(String name) throws UnsupportedOperationException {
            boolean isNew;
            Profile.Section child = this._section.getChild(name);
            boolean bl = isNew = child == null;
            if (isNew) {
                child = this._section.addChild(name);
            }
            return new SectionPreferences(this, child, isNew);
        }

        protected void flushSpi() throws BackingStoreException {
        }

        protected String[] keysSpi() throws BackingStoreException {
            return this._section.keySet().toArray(EMPTY);
        }

        protected void putSpi(String key, String value) {
            this._section.put(key, value);
        }

        protected void removeNodeSpi() throws BackingStoreException {
            IniPreferences.this._ini.remove(this._section);
        }

        protected void removeSpi(String key) {
            this._section.remove(key);
        }

        protected void syncSpi() throws BackingStoreException {
        }
    }
}

