/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.EnumSingleOperator;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class SingleOperatorTerm
implements Term {
    private RawElement parent;
    private EnumSingleOperator opr;
    private Term term;

    public EnumSingleOperator getOpr() {
        return this.opr;
    }

    public SingleOperatorTerm setOpr(EnumSingleOperator opr) {
        this.opr = opr;
        return this;
    }

    public Term getTerm() {
        return this.term;
    }

    public SingleOperatorTerm setTerm(Term term) throws ValidationException {
        this.term = term;
        term.setParent(this);
        return this;
    }

    @Override
    public SingleOperatorTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.SingleOprTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "SingleOprContext", context.toString());
        }
        this.setParent(parent);
        this.setOpr(EnumSingleOperator.fromString(((MediatorLangParser.SingleOprTermContext)context).opr.getText()));
        this.setTerm(Term.parse(((MediatorLangParser.SingleOprTermContext)context).term(), this));
        return this;
    }

    public String toString() {
        return String.format(this.term.getPrecedence() < this.getPrecedence() ? "%s(%s)" : "%s%s", this.opr.toString(), this.term.toString());
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
    public SingleOperatorTerm copy(RawElement parent) throws ValidationException {
        SingleOperatorTerm nsot = new SingleOperatorTerm();
        nsot.setParent(parent);
        nsot.setOpr(this.opr);
        nsot.setTerm(this.getTerm().copy(nsot));
        return nsot;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setTerm(this.getTerm().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return this.opr.oprLevel;
    }
}

