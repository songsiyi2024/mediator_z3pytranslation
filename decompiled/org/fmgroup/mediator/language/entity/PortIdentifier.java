/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity;

import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortDeclaration;
import org.fmgroup.mediator.language.entity.system.ComponentDeclaration;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Scope;

public class PortIdentifier
implements RawElement {
    private RawElement parent = null;
    private String portName;
    private String owner;
    private ComponentDeclaration componentReference = null;
    private PortDeclaration reference = null;

    public ComponentDeclaration getComponentReference() {
        return this.componentReference;
    }

    public String getOwner() {
        return this.owner;
    }

    public PortIdentifier setOwner(String owner) {
        this.owner = owner;
        return this;
    }

    public String getPortName() {
        return this.portName;
    }

    public PortIdentifier setPortName(String portName) throws ValidationException {
        return this.setPortName(portName, false);
    }

    public PortIdentifier setPortName(String portName, boolean noChecking) throws ValidationException {
        this.portName = portName;
        if (!noChecking) {
            if (this.owner == null) {
                Scope scope = this.getCurrentScope();
                this.reference = scope.getPort(portName);
            } else {
                Scope scope = this.getCurrentScope();
                this.componentReference = scope.getComponent(this.owner);
                if (this.componentReference != null) {
                    this.reference = this.componentReference.getType().getProvider().getPort(portName);
                }
            }
        }
        return this;
    }

    public PortDeclaration getReference() {
        return this.reference;
    }

    public PortIdentifier setReference(PortDeclaration reference) {
        this.reference = reference;
        return this;
    }

    @Override
    public PortIdentifier fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.PortIdentifierContext) && !(context instanceof MediatorLangParser.ScopedIDContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "PortIdentifierContext", context.getClass().getName());
        }
        this.setParent(parent);
        if (context instanceof MediatorLangParser.PortIdentifierContext) {
            if (((MediatorLangParser.PortIdentifierContext)context).owner != null) {
                this.setOwner(((MediatorLangParser.PortIdentifierContext)context).owner.getText());
            }
            this.setPortName(((MediatorLangParser.PortIdentifierContext)context).identifier.getText());
        } else {
            if (((MediatorLangParser.ScopedIDContext)context).scopes.size() > 1) {
                throw ValidationException.FromMessage("unknown port");
            }
            if (((MediatorLangParser.ScopedIDContext)context).scopes.size() == 1) {
                this.setOwner(((MediatorLangParser.ScopedIDContext)context).scopes.get(0).getText());
            }
            this.setPortName(((MediatorLangParser.ScopedIDContext)context).identifier.getText());
        }
        return this;
    }

    public String toString() {
        if (this.owner == null) {
            return this.portName;
        }
        return this.owner + "." + this.portName;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public PortIdentifier setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public PortIdentifier copy(RawElement parent) throws ValidationException {
        PortIdentifier portid = new PortIdentifier();
        portid.setParent(parent);
        portid.setOwner(this.owner);
        portid.setPortName(this.portName);
        return portid;
    }
}

