/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.paramType;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class AbstractType
implements Type {
    private RawElement parent;

    @Override
    public AbstractType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.AbstractTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "AbstractTypeContext", context.toString());
        }
        this.setParent(parent);
        return this;
    }

    public String toString() {
        return "type";
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public AbstractType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public AbstractType copy(RawElement parent) throws ValidationException {
        return new AbstractType().setParent(parent);
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return this;
    }
}

