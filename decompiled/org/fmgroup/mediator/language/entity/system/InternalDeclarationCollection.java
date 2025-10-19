/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.system.InternalDeclaration;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.DeclarationCollection;

public class InternalDeclarationCollection
implements DeclarationCollection<InternalDeclaration> {
    private RawElement parent;
    private List<InternalDeclaration> declarationList = new ArrayList<InternalDeclaration>();

    @Override
    public InternalDeclarationCollection fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.InternalSegmentContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "InternalSegmentContext", context.toString());
        }
        ((MediatorLangParser.InternalSegmentContext)context).ID().forEach(terminalNode -> this.addDeclaration(new InternalDeclaration(terminalNode.toString(), this)));
        return this;
    }

    public String toString() {
        if (this.declarationList.size() == 0) {
            return "";
        }
        return String.format("internals %s;\n", this.declarationList.stream().map(Object::toString).collect(Collectors.joining(", ")));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public InternalDeclarationCollection setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public List<InternalDeclaration> getDeclarationList() {
        return this.declarationList;
    }

    @Override
    public DeclarationCollection<InternalDeclaration> addDeclaration(InternalDeclaration declaration) {
        this.declarationList.add(declaration);
        declaration.setParent(this);
        return this;
    }

    @Override
    public DeclarationCollection<InternalDeclaration> setDeclarationList(List<InternalDeclaration> declarationList) {
        this.declarationList = new ArrayList<InternalDeclaration>();
        declarationList.forEach(this::addDeclaration);
        return this;
    }
}

