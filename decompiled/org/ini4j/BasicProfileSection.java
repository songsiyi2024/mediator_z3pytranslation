/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.util.ArrayList;
import java.util.regex.Pattern;
import org.ini4j.BasicOptionMap;
import org.ini4j.BasicProfile;
import org.ini4j.Profile;

class BasicProfileSection
extends BasicOptionMap
implements Profile.Section {
    private static final long serialVersionUID = 985800697957194374L;
    private static final String[] EMPTY_STRING_ARRAY = new String[0];
    private static final char REGEXP_ESCAPE_CHAR = '\\';
    private final Pattern _childPattern;
    private final String _name;
    private final BasicProfile _profile;

    protected BasicProfileSection(BasicProfile profile, String name) {
        this._profile = profile;
        this._name = name;
        this._childPattern = this.newChildPattern(name);
    }

    public Profile.Section getChild(String key) {
        return (Profile.Section)this._profile.get(this.childName(key));
    }

    public String getName() {
        return this._name;
    }

    public Profile.Section getParent() {
        Profile.Section ret = null;
        int idx = this._name.lastIndexOf(this._profile.getPathSeparator());
        if (idx >= 0) {
            String name = this._name.substring(0, idx);
            ret = (Profile.Section)this._profile.get(name);
        }
        return ret;
    }

    public String getSimpleName() {
        int idx = this._name.lastIndexOf(this._profile.getPathSeparator());
        return idx < 0 ? this._name : this._name.substring(idx + 1);
    }

    public Profile.Section addChild(String key) {
        String name = this.childName(key);
        return this._profile.add(name);
    }

    public String[] childrenNames() {
        ArrayList<String> names = new ArrayList<String>();
        for (String key : this._profile.keySet()) {
            if (!this._childPattern.matcher(key).matches()) continue;
            names.add(key.substring(this._name.length() + 1));
        }
        return names.toArray(EMPTY_STRING_ARRAY);
    }

    public Profile.Section lookup(String ... parts) {
        StringBuilder buff = new StringBuilder();
        for (String part : parts) {
            if (buff.length() != 0) {
                buff.append(this._profile.getPathSeparator());
            }
            buff.append(part);
        }
        return (Profile.Section)this._profile.get(this.childName(buff.toString()));
    }

    public void removeChild(String key) {
        String name = this.childName(key);
        this._profile.remove(name);
    }

    boolean isPropertyFirstUpper() {
        return this._profile.isPropertyFirstUpper();
    }

    void resolve(StringBuilder buffer) {
        this._profile.resolve(buffer, this);
    }

    private String childName(String key) {
        StringBuilder buff = new StringBuilder(this._name);
        buff.append(this._profile.getPathSeparator());
        buff.append(key);
        return buff.toString();
    }

    private Pattern newChildPattern(String name) {
        StringBuilder buff = new StringBuilder();
        buff.append('^');
        buff.append(Pattern.quote(name));
        buff.append('\\');
        buff.append(this._profile.getPathSeparator());
        buff.append("[^");
        buff.append('\\');
        buff.append(this._profile.getPathSeparator());
        buff.append("]+$");
        return Pattern.compile(buff.toString());
    }
}

