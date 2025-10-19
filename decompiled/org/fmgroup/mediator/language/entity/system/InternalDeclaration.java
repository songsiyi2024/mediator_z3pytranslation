/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.ArrayList;
import java.util.List;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.entity.system.InternalDeclarationCollection;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.paramType.AbstractType;

public class InternalDeclaration
implements Declaration {
    private RawElement parent = null;
    private String identifier = null;
    private Type type = new AbstractType();

    public InternalDeclaration(String s, InternalDeclarationCollection internalDeclarationCollection) {
        this.setIdentifier(s);
        this.setParent(internalDeclarationCollection);
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public InternalDeclaration setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public String getIdentifier() {
        return this.identifier;
    }

    public InternalDeclaration setIdentifier(String identifier) {
        this.identifier = identifier;
        return this;
    }

    public Type getType() {
        return this.type;
    }

    public InternalDeclaration setType(Type type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    @Override
    public List<String> getIdentifiers() {
        ArrayList<String> result = new ArrayList<String>();
        result.add(this.identifier);
        return result;
    }

    public String toString() {
        return this.getIdentifier();
    }
}

