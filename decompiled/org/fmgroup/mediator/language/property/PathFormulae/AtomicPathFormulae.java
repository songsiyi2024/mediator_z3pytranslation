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
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class AtomicPathFormulae
implements PathFormulae {
    private RawElement parent;
    private Term term;

    public Term getTerm() {
        return this.term;
    }

    public AtomicPathFormulae setTerm(Term term) {
        this.term = term;
        term.setParent(this);
        return this;
    }

    @Override
    public AtomicPathFormulae fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.AtomicPathFormulaeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "AtomicPathFormulaeContext", context.toString());
        }
        this.setParent(parent);
        this.setTerm(Term.parse(((MediatorLangParser.AtomicPathFormulaeContext)context).term(), this));
        return this;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return null;
    }

    @Override
    public int getPrecedence() {
        return this.term.getPrecedence();
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public AtomicPathFormulae setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public String toString() {
        return this.term.toString();
    }

    @Override
    public AtomicPathFormulae copy(RawElement parent) throws ValidationException {
        AtomicPathFormulae copy = new AtomicPathFormulae();
        copy.setParent(parent);
        copy.setTerm(this.term.copy(copy));
        return copy;
    }
}

