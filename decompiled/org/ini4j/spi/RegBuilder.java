/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.Config;
import org.ini4j.Profile;
import org.ini4j.Reg;
import org.ini4j.Registry;
import org.ini4j.spi.AbstractProfileBuilder;
import org.ini4j.spi.RegEscapeTool;
import org.ini4j.spi.ServiceFinder;
import org.ini4j.spi.TypeValuesPair;

public class RegBuilder
extends AbstractProfileBuilder {
    private Reg _reg;

    public static RegBuilder newInstance(Reg reg) {
        RegBuilder instance = RegBuilder.newInstance();
        instance.setReg(reg);
        return instance;
    }

    public void setReg(Reg value) {
        this._reg = value;
    }

    public void handleOption(String rawName, String rawValue) {
        String name = rawName.charAt(0) == '\"' ? RegEscapeTool.getInstance().unquote(rawName) : rawName;
        TypeValuesPair tv = RegEscapeTool.getInstance().decode(rawValue);
        if (tv.getType() != Registry.Type.REG_SZ) {
            ((Registry.Key)this.getCurrentSection()).putType(name, tv.getType());
        }
        for (String value : tv.getValues()) {
            super.handleOption(name, value);
        }
    }

    Config getConfig() {
        return this._reg.getConfig();
    }

    Profile getProfile() {
        return this._reg;
    }

    private static RegBuilder newInstance() {
        return ServiceFinder.findService(RegBuilder.class);
    }
}

