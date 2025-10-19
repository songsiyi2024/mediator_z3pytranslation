/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import org.fmgroup.mediator.language.ValidationException;

public enum EnumBinaryOperatorTemporal {
    RIGHT_DERIVE("->", 2),
    LEFT_DERIVE("<-", 2),
    EQUAL("<->", 2),
    LAND("&&", 4),
    LOR("||", 3);

    public String oprString;
    public int oprLevel;

    private EnumBinaryOperatorTemporal(String oprString, int oprLevel) {
        this.oprLevel = oprLevel;
        this.oprString = oprString;
    }

    public static EnumBinaryOperatorTemporal fromString(String str) throws ValidationException {
        for (EnumBinaryOperatorTemporal opr : EnumBinaryOperatorTemporal.values()) {
            if (!opr.oprString.equals(str)) continue;
            return opr;
        }
        throw ValidationException.UnregisteredOperator(str);
    }

    public String toString() {
        return this.oprString;
    }
}

