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

public class ElementTerm
implements Term {
    private RawElement parent;
    private Term container;
    private Term key;

    @Override
    public ElementTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ElementTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ElementTermContext", context.toString());
        }
        this.setParent(parent);
        this.setContainer(Term.parse(((MediatorLangParser.ElementTermContext)context).container, this));
        this.setKey(Term.parse(((MediatorLangParser.ElementTermContext)context).key, this));
        return this;
    }

    public String toString() {
        return String.format(this.container.getPrecedence() < this.getPrecedence() ? "(%s)[%s]" : "%s[%s]", this.container.toString(), this.key.toString());
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

    public Term getContainer() {
        return this.container;
    }

    public ElementTerm setContainer(Term container) {
        this.container = container;
        container.setParent(this);
        return this;
    }

    public Term getKey() {
        return this.key;
    }

    public ElementTerm setKey(Term key) {
        this.key = key;
        key.setParent(this);
        return this;
    }

    @Override
    public ElementTerm copy(RawElement parent) throws ValidationException {
        ElementTerm net = new ElementTerm();
        net.setParent(parent);
        net.setContainer(this.container.copy(net));
        net.setKey(this.key.copy(net));
        return net;
    }

    @Override
    public ElementTerm refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setContainer(this.getContainer().refactor(typeRewriteMap, termRewriteMap));
        this.setKey(this.getKey().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return 13;
    }
}

