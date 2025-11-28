/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;

public class Property
implements RawElement {
    private RawElement parent;
    private PathFormulae formulae;

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public Property setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public Property fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.PropertyContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "PropertyContext", context.toString());
        }
        this.formulae = PathFormulae.parse(((MediatorLangParser.PropertyContext)context).pathFormulae(), (RawElement)this);
        return this;
    }

    public String toString() {
        return this.formulae.toString();
    }

    public PathFormulae getFormulae() {
        return this.formulae;
    }

    public Property setFormulae(PathFormulae formulae) {
        this.formulae = formulae;
        formulae.setParent(this);
        return this;
    }

    @Override
    public Property copy(RawElement parent) throws ValidationException {
        Property copy = new Property();
        copy.setParent(parent);
        copy.setFormulae((PathFormulae) this.formulae.copy(copy));
        return copy;
    }
}

