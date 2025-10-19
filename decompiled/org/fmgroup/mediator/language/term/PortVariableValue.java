/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortIdentifier;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.PortVariableType;
import org.fmgroup.mediator.language.term.Value;

public class PortVariableValue
implements RawElement,
Value {
    private RawElement parent;
    private PortIdentifier portIdentifier;
    private PortVariableType portVariableType;

    public PortIdentifier getPortIdentifier() {
        return this.portIdentifier;
    }

    public PortVariableValue setPortIdentifier(PortIdentifier portIdentifier) {
        this.portIdentifier = portIdentifier;
        portIdentifier.setParent(this);
        return this;
    }

    public PortVariableType getPortVariableType() {
        return this.portVariableType;
    }

    public PortVariableValue setPortVariableType(PortVariableType portVariableType) {
        this.portVariableType = portVariableType;
        return this;
    }

    @Override
    public PortVariableValue fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.PortVarValueContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "PortVarValueContext", context.toString());
        }
        this.setParent(parent);
        this.setPortIdentifier(new PortIdentifier().fromContext(((MediatorLangParser.PortVarValueContext)context).scopedID(), this));
        this.setPortVariableType(PortVariableType.fromString(((MediatorLangParser.PortVarValueContext)context).PORTVAR_SUFFIX().getText()));
        return this;
    }

    @Override
    public PortVariableValue copy(RawElement parent) throws ValidationException {
        PortVariableValue npv = new PortVariableValue();
        npv.setParent(parent);
        npv.setPortVariableType(this.portVariableType);
        npv.setPortIdentifier(this.getPortIdentifier().copy(npv));
        return npv;
    }

    public String toString() {
        return this.portIdentifier.toString() + "." + this.portVariableType.toString();
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public PortVariableValue setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public int getPrecedence() {
        return 14;
    }
}

