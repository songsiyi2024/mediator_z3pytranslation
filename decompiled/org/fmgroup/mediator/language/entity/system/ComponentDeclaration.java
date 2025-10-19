/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.ArrayList;
import java.util.List;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.type.paramType.TemplateType;

public class ComponentDeclaration
implements RawElement,
Declaration {
    private RawElement parent = null;
    private List<String> identifiers = new ArrayList<String>();
    private TemplateType type = null;

    public TemplateType getType() {
        return this.type;
    }

    public ComponentDeclaration setType(TemplateType type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    @Override
    public List<String> getIdentifiers() {
        return this.identifiers;
    }

    public ComponentDeclaration setIdentifiers(List<String> identifiers) {
        this.identifiers = identifiers;
        return this;
    }

    @Override
    public ComponentDeclaration fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ComponentDeclContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ComponentDeclContext", context.toString());
        }
        this.setParent(parent);
        this.setType(new TemplateType().fromContext(((MediatorLangParser.ComponentDeclContext)context).type(), this));
        for (TerminalNode name : ((MediatorLangParser.ComponentDeclContext)context).ID()) {
            this.addIdentifier(name.getText());
        }
        return this;
    }

    public String toString() {
        return String.join((CharSequence)", ", this.getIdentifiers()) + ": " + this.getType().toString();
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public ComponentDeclaration setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

