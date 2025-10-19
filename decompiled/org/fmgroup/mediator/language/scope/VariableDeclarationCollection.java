/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.VariableDeclaration;

public class VariableDeclarationCollection
implements DeclarationCollection<VariableDeclaration> {
    private RawElement parent = null;
    private List<VariableDeclaration> declarationList = new ArrayList<VariableDeclaration>();

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public VariableDeclarationCollection setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public VariableDeclarationCollection copy(RawElement parent) throws ValidationException {
        VariableDeclarationCollection newCollection = new VariableDeclarationCollection();
        newCollection.setParent(parent);
        for (VariableDeclaration vardecl : this.getDeclarationList()) {
            newCollection.addDeclaration(vardecl.copy(newCollection));
        }
        return newCollection;
    }

    @Override
    public List<VariableDeclaration> getDeclarationList() {
        return this.declarationList;
    }

    public VariableDeclarationCollection setDeclarationList(List<VariableDeclaration> declarationList) {
        declarationList = new ArrayList<VariableDeclaration>();
        declarationList.forEach(this::addDeclaration);
        return this;
    }

    public VariableDeclarationCollection addDeclaration(VariableDeclaration declaration) {
        this.declarationList.add(declaration);
        declaration.setParent(this);
        return this;
    }

    public String toString() {
        if (this.declarationList.size() > 0) {
            return String.format("variables {\n %s}\n", UtilCode.addIndent(this.declarationList.stream().map(vardecl -> vardecl.toString() + ";\n").collect(Collectors.joining("")), 1));
        }
        return "";
    }
}

