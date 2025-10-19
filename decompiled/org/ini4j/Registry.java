/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.nio.charset.Charset;
import java.util.HashMap;
import java.util.Map;
import org.ini4j.Profile;

public interface Registry
extends Profile {
    public static final char ESCAPE_CHAR = '\\';
    public static final Charset FILE_ENCODING = Charset.forName("UnicodeLittle");
    public static final char KEY_SEPARATOR = '\\';
    public static final String LINE_SEPARATOR = "\r\n";
    public static final char TYPE_SEPARATOR = ':';
    public static final String VERSION = "Windows Registry Editor Version 5.00";

    public String getVersion();

    public void setVersion(String var1);

    public Key get(Object var1);

    public Key get(Object var1, int var2);

    public Key put(String var1, Profile.Section var2);

    public Key put(String var1, Profile.Section var2, int var3);

    public Key remove(Object var1);

    public Key remove(Object var1, int var2);

    public static interface Key
    extends Profile.Section {
        public static final String DEFAULT_NAME = "@";

        public Key getChild(String var1);

        public Key getParent();

        public Type getType(Object var1);

        public Type getType(Object var1, Type var2);

        public Key addChild(String var1);

        public Key lookup(String ... var1);

        public Type putType(String var1, Type var2);

        public Type removeType(Object var1);
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    public static enum Type {
        REG_NONE("hex(0)"),
        REG_SZ(""),
        REG_EXPAND_SZ("hex(2)"),
        REG_BINARY("hex"),
        REG_DWORD("dword"),
        REG_DWORD_BIG_ENDIAN("hex(5)"),
        REG_LINK("hex(6)"),
        REG_MULTI_SZ("hex(7)"),
        REG_RESOURCE_LIST("hex(8)"),
        REG_FULL_RESOURCE_DESCRIPTOR("hex(9)"),
        REG_RESOURCE_REQUIREMENTS_LIST("hex(a)"),
        REG_QWORD("hex(b)");

        private static final Map<String, Type> MAPPING;
        public static final char SEPARATOR_CHAR = ':';
        public static final String SEPARATOR;
        public static final char REMOVE_CHAR = '-';
        public static final String REMOVE;
        private final String _prefix;

        private Type(String prefix) {
            this._prefix = prefix;
        }

        public static Type fromString(String str) {
            return MAPPING.get(str);
        }

        public String toString() {
            return this._prefix;
        }

        static {
            MAPPING = new HashMap<String, Type>();
            for (Type t : Type.values()) {
                MAPPING.put(t.toString(), t);
            }
            SEPARATOR = String.valueOf(':');
            REMOVE = String.valueOf('-');
        }
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    public static enum Hive {
        HKEY_CLASSES_ROOT,
        HKEY_CURRENT_CONFIG,
        HKEY_CURRENT_USER,
        HKEY_LOCAL_MACHINE,
        HKEY_USERS;

    }
}

