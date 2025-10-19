/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.term.Value;
import org.fmgroup.mediator.language.type.termType.EnumType;

public class EnumValue
implements Value {
    private RawElement parent;
    private EnumType reference;
    private String identifier;

    public EnumType getReference() {
        return this.reference;
    }

    public EnumValue setReference(EnumType reference) {
        this.reference = reference;
        return this;
    }

    public String getIdentifier() {
        return this.identifier;
    }

    public EnumValue setIdentifier(String identifier) throws ValidationException {
        this.identifier = identifier;
        if (!this.getReference().getItems().contains(identifier)) {
            throw ValidationException.UnknownIdentifier(identifier, "enum item");
        }
        return this;
    }

    @Override
    public EnumValue copy(RawElement parent) throws ValidationException {
        EnumValue newev = new EnumValue().setParent(parent);
        newev.setReference(this.getReference());
        newev.setIdentifier(this.getIdentifier());
        return newev;
    }

    public String toString() {
        return this.identifier;
    }

    @Override
    public int getPrecedence() {
        return 14;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public EnumValue setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

