/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import org.ini4j.BasicProfile;
import org.ini4j.BasicRegistryKey;
import org.ini4j.Profile;
import org.ini4j.Registry;
import org.ini4j.spi.IniHandler;
import org.ini4j.spi.RegEscapeTool;
import org.ini4j.spi.TypeValuesPair;

public class BasicRegistry
extends BasicProfile
implements Registry {
    private static final long serialVersionUID = -6432826330714504802L;
    private String _version = "Windows Registry Editor Version 5.00";

    public String getVersion() {
        return this._version;
    }

    public void setVersion(String value) {
        this._version = value;
    }

    public Registry.Key add(String name) {
        return (Registry.Key)super.add(name);
    }

    public Registry.Key get(Object key) {
        return (Registry.Key)super.get(key);
    }

    public Registry.Key get(Object key, int index) {
        return (Registry.Key)super.get(key, index);
    }

    public Registry.Key put(String key, Profile.Section value) {
        return (Registry.Key)super.put(key, value);
    }

    public Registry.Key put(String key, Profile.Section value, int index) {
        return (Registry.Key)super.put(key, value, index);
    }

    public Registry.Key remove(Profile.Section section) {
        return (Registry.Key)super.remove(section);
    }

    public Registry.Key remove(Object key) {
        return (Registry.Key)super.remove(key);
    }

    public Registry.Key remove(Object key, int index) {
        return (Registry.Key)super.remove(key, index);
    }

    Registry.Key newSection(String name) {
        return new BasicRegistryKey(this, name);
    }

    void store(IniHandler formatter, Profile.Section section, String option) {
        this.store(formatter, section.getComment(option));
        Registry.Type type = ((Registry.Key)section).getType(option, Registry.Type.REG_SZ);
        String rawName = option.equals("@") ? option : RegEscapeTool.getInstance().quote(option);
        String[] values = new String[section.length(option)];
        for (int i = 0; i < values.length; ++i) {
            values[i] = (String)section.get((Object)option, i);
        }
        String rawValue = RegEscapeTool.getInstance().encode(new TypeValuesPair(type, values));
        formatter.handleOption(rawName, rawValue);
    }
}

