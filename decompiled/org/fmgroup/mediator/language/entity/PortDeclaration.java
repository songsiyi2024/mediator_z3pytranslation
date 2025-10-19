/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity;

import java.util.ArrayList;
import java.util.List;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.TerminalNode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortDirection;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.type.Type;

public class PortDeclaration
implements RawElement,
Declaration {
    private List<String> identifiers = new ArrayList<String>();
    private PortDirection direction;
    private Type type;
    private RawElement parent;

    public PortDirection getDirection() {
        return this.direction;
    }

    public PortDeclaration setDirection(PortDirection direction) {
        this.direction = direction;
        return this;
    }

    public Type getType() {
        return this.type;
    }

    public PortDeclaration setType(Type type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    @Override
    public PortDeclaration fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.PortsDeclContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "PortsDeclContext", context.toString());
        }
        this.setParent(parent);
        for (TerminalNode portName : ((MediatorLangParser.PortsDeclContext)context).ID()) {
            if (this.identifiers.contains(portName.getText()) || this.getCurrentScope().existsDeclaration(portName.getText())) {
                throw ValidationException.DumplicatedIdentifier(portName.getText(), "symbol");
            }
            this.addIdentifier(portName.getText());
        }
        if (((MediatorLangParser.PortsDeclContext)context).direction.getText().equals("IN")) {
            this.setDirection(PortDirection.IN);
        } else {
            this.setDirection(PortDirection.OUT);
        }
        this.setType(Type.parse(((MediatorLangParser.PortsDeclContext)context).type(), this));
        return this;
    }

    public String toString() {
        return String.format("%s: %s %s", String.join((CharSequence)", ", this.identifiers), this.direction.toString(), this.type.toString());
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public PortDeclaration setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public PortDeclaration copy(RawElement parent) throws ValidationException {
        PortDeclaration newdecl = new PortDeclaration();
        newdecl.setParent(parent);
        newdecl.setIdentifiers(this.identifiers);
        newdecl.setType(this.type.copy(newdecl));
        newdecl.setDirection(this.getDirection());
        return newdecl;
    }

    @Override
    public int size() {
        return this.identifiers.size();
    }

    @Override
    public List<String> getIdentifiers() {
        return this.identifiers;
    }

    public PortDeclaration setIdentifiers(List<String> identifiers) throws ValidationException {
        this.identifiers = new ArrayList<String>();
        for (String identifier : identifiers) {
            this.addIdentifier(identifier);
        }
        return this;
    }
}

