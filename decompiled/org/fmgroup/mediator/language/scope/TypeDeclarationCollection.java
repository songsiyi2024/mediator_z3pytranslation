/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.TypeDeclaration;

public class TypeDeclarationCollection
implements DeclarationCollection<TypeDeclaration> {
    public List<TypeDeclaration> typeDeclarations = new ArrayList<TypeDeclaration>();
    private RawElement parent;

    @Override
    public List<TypeDeclaration> getDeclarationList() {
        return this.typeDeclarations;
    }

    @Override
    public DeclarationCollection<TypeDeclaration> addDeclaration(TypeDeclaration declaration) {
        this.typeDeclarations.add(declaration);
        declaration.setParent(this);
        return this;
    }

    @Override
    public DeclarationCollection<TypeDeclaration> setDeclarationList(List<TypeDeclaration> declarationList) {
        this.typeDeclarations = new ArrayList<TypeDeclaration>();
        declarationList.forEach(this::addDeclaration);
        return this;
    }

    public String toString() {
        return this.typeDeclarations.stream().map(typeDeclaration -> typeDeclaration.toString() + ";\n").collect(Collectors.joining(""));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public TypeDeclarationCollection setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

