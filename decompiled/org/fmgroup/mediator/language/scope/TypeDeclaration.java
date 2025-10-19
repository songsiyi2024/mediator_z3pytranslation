/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.ArrayList;
import java.util.List;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.type.Type;

public class TypeDeclaration
implements RawElement,
Declaration {
    private RawElement parent;
    private List<String> identifiers = new ArrayList<String>();
    private Type type;
    private boolean isTypedef = true;

    public Type getType() {
        return this.type;
    }

    public TypeDeclaration setType(Type type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    public boolean isTypedef() {
        return this.isTypedef;
    }

    public TypeDeclaration setTypedef(boolean typedef) {
        this.isTypedef = typedef;
        return this;
    }

    @Override
    public TypeDeclaration fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.TypedefContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "TypedefContext", context.toString());
        }
        this.setParent(parent);
        for (TerminalNode tn : ((MediatorLangParser.TypedefContext)context).ID()) {
            this.addIdentifier(tn.getText());
        }
        this.setType(Type.parse(((MediatorLangParser.TypedefContext)context).type(), this));
        return this;
    }

    public String toString() {
        if (this.isTypedef) {
            return String.format("typedef %s as %s", this.type.toString(), String.join((CharSequence)", ", this.identifiers));
        }
        return String.format("%s : %s", String.join((CharSequence)", ", this.identifiers), this.type.toString());
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public RawElement setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public int size() {
        return this.identifiers.size();
    }

    @Override
    public List<String> getIdentifiers() {
        return this.identifiers;
    }

    public TypeDeclaration setIdentifiers(List<String> identifiers) throws ValidationException {
        this.identifiers = new ArrayList<String>();
        for (String identifier : identifiers) {
            this.addIdentifier(identifier);
        }
        return this;
    }
}

