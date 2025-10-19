/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.system.ComponentDeclaration;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.DeclarationCollection;

public class ComponentDeclarationCollection
implements DeclarationCollection<ComponentDeclaration> {
    private RawElement parent = null;
    private List<ComponentDeclaration> declarationList = new ArrayList<ComponentDeclaration>();

    @Override
    public ComponentDeclarationCollection fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ComponentSegmentContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ComponentSegmentContext", context.toString());
        }
        if (this.parent != null && !this.parent.equals(parent)) {
            throw ValidationException.FromMessage("Cannot combine component segment from different systems.");
        }
        this.setParent(parent);
        for (MediatorLangParser.ComponentDeclContext comp : ((MediatorLangParser.ComponentSegmentContext)context).componentDecl()) {
            this.addDeclaration(new ComponentDeclaration().fromContext(comp, this));
        }
        return this;
    }

    public String toString() {
        if (this.declarationList.size() == 0) {
            return "";
        }
        return String.format("declarationList {\n%s}\n", UtilCode.addIndent(this.declarationList.stream().map(componentDeclaration -> componentDeclaration.toString() + ";\n").collect(Collectors.joining()), 1));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public ComponentDeclarationCollection setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public List<ComponentDeclaration> getDeclarationList() {
        return this.declarationList;
    }

    @Override
    public DeclarationCollection<ComponentDeclaration> addDeclaration(ComponentDeclaration declaration) {
        this.declarationList.add(declaration);
        declaration.setParent(this);
        return this;
    }

    @Override
    public DeclarationCollection<ComponentDeclaration> setDeclarationList(List<ComponentDeclaration> declarationList) {
        this.declarationList = new ArrayList<ComponentDeclaration>();
        declarationList.forEach(this::addDeclaration);
        return this;
    }
}

