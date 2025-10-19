/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property.PathFormulae;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class ExistsPathFormulae
implements PathFormulae {
    private RawElement parent;
    private StateFormulae formula;

    public StateFormulae getFormula() {
        return this.formula;
    }

    public ExistsPathFormulae setFormula(StateFormulae formula) {
        this.formula = formula;
        formula.setParent(this);
        return this;
    }

    @Override
    public ExistsPathFormulae fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ExistsPathFormulaeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ExistsPathFormulaeContext", context.toString());
        }
        this.setParent(parent);
        this.setFormula(StateFormulae.parse(((MediatorLangParser.ExistsPathFormulaeContext)context).stateFormulae(), (RawElement)this));
        return this;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return null;
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

    public String toString() {
        return "E " + this.formula.toString();
    }
}

