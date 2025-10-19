/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class IteTerm
implements Term {
    private RawElement parent = null;
    private Term condition = null;
    private Term thenTerm = null;
    private Term elseTerm = null;

    public Term getCondition() {
        return this.condition;
    }

    public IteTerm setCondition(Term cond) throws ValidationException {
        this.condition = cond;
        cond.setParent(this);
        return this;
    }

    public Term getThenTerm() {
        return this.thenTerm;
    }

    public IteTerm setThenTerm(Term thenTerm) throws ValidationException {
        this.thenTerm = thenTerm;
        thenTerm.setParent(this);
        return this;
    }

    public Term getElseTerm() {
        return this.elseTerm;
    }

    public IteTerm setElseTerm(Term elseTerm) throws ValidationException {
        this.elseTerm = elseTerm;
        elseTerm.setParent(this);
        return this;
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return 2;
    }

    @Override
    public IteTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.IteTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "IteTermContext", context.toString());
        }
        this.setParent(parent);
        this.setCondition(Term.parse(((MediatorLangParser.IteTermContext)context).condition, this));
        this.setCondition(Term.parse(((MediatorLangParser.IteTermContext)context).ifTrue, this));
        this.setElseTerm(Term.parse(((MediatorLangParser.IteTermContext)context).ifFalse, this));
        return this;
    }

    public String toString() {
        return String.format((this.condition.getPrecedence() < this.getPrecedence() ? "(%s)" : "%s") + " ? %s : " + (this.elseTerm.getPrecedence() < this.getPrecedence() ? "(%s)" : "%s"), this.condition.toString(), this.thenTerm.toString(), this.elseTerm.toString());
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public IteTerm setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public IteTerm copy(RawElement parent) throws ValidationException {
        return new IteTerm().setParent(parent).setCondition(this.condition).setThenTerm(this.thenTerm).setElseTerm(this.elseTerm);
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setCondition(this.getCondition().refactor(typeRewriteMap, termRewriteMap));
        this.setThenTerm(this.getThenTerm().refactor(typeRewriteMap, termRewriteMap));
        this.setElseTerm(this.getElseTerm().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }
}

