/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import org.fmgroup.mediator.language.ValidationException;

public enum EnumBinaryOperator {
    NEQ("!=", 6),
    EQ("==", 6),
    LT("<", 6),
    LEQ("<=", 6),
    GT(">", 6),
    GEQ(">=", 6),
    ADD("+", 7),
    MINUS("-", 7),
    TIMES("*", 8),
    DIV("/", 8),
    MOD("%", 9),
    LAND("&&", 4),
    LOR("||", 3),
    LXOR("^^", 5),
    BITAND("&", 4),
    BITOR("|", 3),
    BITXOR("^", 5);

    public String oprString;
    public int oprLevel;

    private EnumBinaryOperator(String oprString, int oprLevel) {
        this.oprLevel = oprLevel;
        this.oprString = oprString;
    }

    public static EnumBinaryOperator fromString(String str) throws ValidationException {
        for (EnumBinaryOperator opr : EnumBinaryOperator.values()) {
            if (!opr.oprString.equals(str)) continue;
            return opr;
        }
        throw ValidationException.UnregisteredOperator(str);
    }

    public String toString() {
        return this.oprString;
    }
}

