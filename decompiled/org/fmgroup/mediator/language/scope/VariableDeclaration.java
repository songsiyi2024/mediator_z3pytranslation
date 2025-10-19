/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.type.Type;

public class VariableDeclaration
implements RawElement,
Declaration {
    private RawElement parent = null;
    private List<String> identifiers = new ArrayList<String>();
    private Type type = null;

    public Type getType() {
        return this.type;
    }

    public VariableDeclaration setType(Type type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    @Override
    public VariableDeclaration fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.LocalVariableDefContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "LocalVariableDefContext", context.toString());
        }
        this.setParent(parent);
        for (TerminalNode tn : ((MediatorLangParser.LocalVariableDefContext)context).ID()) {
            this.addIdentifier(tn.getText());
        }
        this.setType(Type.parse(((MediatorLangParser.LocalVariableDefContext)context).type(), this));
        return this;
    }

    public String toString() {
        if (this.identifiers.size() == 0) {
            return "";
        }
        return String.join((CharSequence)", ", this.getIdentifiers()) + ": " + this.type.toString();
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public VariableDeclaration setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public VariableDeclaration copy(RawElement parent) throws ValidationException {
        VariableDeclaration nvd = new VariableDeclaration();
        nvd.setParent(parent);
        nvd.setIdentifiers(this.identifiers);
        nvd.setType(this.type.copy(nvd));
        return nvd;
    }

    @Override
    public int size() {
        return this.identifiers.size();
    }

    @Override
    public List<String> getIdentifiers() {
        return this.identifiers;
    }

    public VariableDeclaration setIdentifiers(List<String> identifiers) {
        this.identifiers = identifiers;
        return this;
    }

    public VariableDeclaration addPrefix(String prefix) {
        this.setIdentifiers(this.getIdentifiers().stream().map(s -> prefix + s).collect(Collectors.toList()));
        return this;
    }
}

