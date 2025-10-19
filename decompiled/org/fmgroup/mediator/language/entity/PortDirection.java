/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity;

public enum PortDirection {
    IN("in"),
    OUT("out");

    private String value;

    private PortDirection(String value) {
        this.value = value;
    }

    public String toString() {
        return this.value;
    }
}

