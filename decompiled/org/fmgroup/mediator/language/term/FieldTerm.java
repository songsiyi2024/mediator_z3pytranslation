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

public class FieldTerm
implements Term {
    private RawElement parent;
    private Term owner;
    private String field;

    @Override
    public FieldTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.FieldTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "FieldTermContext", context.toString());
        }
        this.setParent(parent);
        this.setOwner(Term.parse(((MediatorLangParser.FieldTermContext)context).structure, this));
        this.setField(((MediatorLangParser.FieldTermContext)context).key.getText());
        return this;
    }

    public String toString() {
        return String.format(this.owner.getPrecedence() < this.getPrecedence() ? "(%s).%s" : "%s.%s", this.owner.toString(), this.field);
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

    public Term getOwner() {
        return this.owner;
    }

    public FieldTerm setOwner(Term owner) {
        this.owner = owner;
        owner.setParent(this);
        return this;
    }

    public String getField() {
        return this.field;
    }

    public FieldTerm setField(String field) {
        this.field = field;
        return this;
    }

    @Override
    public FieldTerm copy(RawElement parent) throws ValidationException {
        FieldTerm nft = new FieldTerm();
        nft.setParent(parent);
        nft.setField(this.getField());
        nft.setOwner(this.getOwner().copy(nft));
        return nft;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setOwner(this.getOwner().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return 12;
    }
}

