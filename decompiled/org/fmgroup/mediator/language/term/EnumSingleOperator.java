/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import org.fmgroup.mediator.language.ValidationException;

public enum EnumSingleOperator {
    LNOT("!", 10),
    NEGATIVE("-", 10);

    public String oprString;
    public int oprLevel;

    private EnumSingleOperator(String oprString, int oprLevel) {
        this.oprLevel = oprLevel;
        this.oprString = oprString;
    }

    public static EnumSingleOperator fromString(String str) throws ValidationException {
        for (EnumSingleOperator opr : EnumSingleOperator.values()) {
            if (!opr.oprString.equals(str)) continue;
            return opr;
        }
        throw ValidationException.UnregisteredOperator(str);
    }

    public String toString() {
        return this.oprString;
    }
}

