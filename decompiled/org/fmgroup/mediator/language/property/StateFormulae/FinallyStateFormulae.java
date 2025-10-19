/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property.StateFormulae;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class FinallyStateFormulae
implements StateFormulae {
    private RawElement parent;
    private StateFormulae formula;

    public StateFormulae getFormula() {
        return this.formula;
    }

    public FinallyStateFormulae setFormula(StateFormulae formula) {
        this.formula = formula;
        formula.setParent(this);
        return this;
    }

    @Override
    public FinallyStateFormulae fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.FinallyStateFormulaeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "FinallyStateFormulaeContext", context.toString());
        }
        this.setParent(parent);
        this.setFormula(StateFormulae.parse(((MediatorLangParser.FinallyStateFormulaeContext)context).stateFormulae(), (RawElement)this));
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
    public FinallyStateFormulae setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public String toString() {
        return "F " + this.formula.toString();
    }
}

