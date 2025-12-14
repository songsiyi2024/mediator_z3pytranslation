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
        if (cond != null) cond.setParent(this);
        return this;
    }

    public Term getThenTerm() {
        return this.thenTerm;
    }

    public IteTerm setThenTerm(Term thenTerm) throws ValidationException {
        this.thenTerm = thenTerm;
        if (thenTerm != null) thenTerm.setParent(this);
        return this;
    }

    public Term getElseTerm() {
        return this.elseTerm;
    }

    public IteTerm setElseTerm(Term elseTerm) throws ValidationException {
        this.elseTerm = elseTerm;
        if (elseTerm != null) elseTerm.setParent(this);
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
        this.setThenTerm(Term.parse(((MediatorLangParser.IteTermContext)context).ifTrue, this));
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
        IteTerm copy = new IteTerm().setParent(parent);
        if (this.condition != null) copy.setCondition(this.condition.copy(copy));
        if (this.thenTerm != null) copy.setThenTerm(this.thenTerm.copy(copy));
        if (this.elseTerm != null) copy.setElseTerm(this.elseTerm.copy(copy));
        return copy;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        if (this.condition != null) this.setCondition(this.getCondition().refactor(typeRewriteMap, termRewriteMap));
        if (this.thenTerm != null) this.setThenTerm(this.getThenTerm().refactor(typeRewriteMap, termRewriteMap));
        if (this.elseTerm != null) this.setElseTerm(this.getElseTerm().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }
}
