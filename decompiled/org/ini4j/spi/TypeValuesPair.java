/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.Registry;

public class TypeValuesPair {
    private final Registry.Type _type;
    private final String[] _values;

    public TypeValuesPair(Registry.Type type, String[] values) {
        this._type = type;
        this._values = values;
    }

    public Registry.Type getType() {
        return this._type;
    }

    public String[] getValues() {
        return this._values;
    }
}

