/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

public enum PortVariableType {
    VALUE("value"),
    REQREAD("reqRead"),
    REQWRITE("reqWrite");

    private String value;

    private PortVariableType(String value) {
        this.value = value;
    }

    public static PortVariableType fromString(String value) {
        if (value.equals(PortVariableType.VALUE.value)) {
            return VALUE;
        }
        if (value.equals(PortVariableType.REQREAD.value)) {
            return REQREAD;
        }
        if (value.equals(PortVariableType.REQWRITE.value)) {
            return REQWRITE;
        }
        return null;
    }

    public String toString() {
        return this.value;
    }
}

