/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.termType;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class ListType
implements Type {
    private RawElement parent = null;
    private Type baseType;
    private Term capacity = null;

    public Type getBaseType() {
        return this.baseType;
    }

    public ListType setBaseType(Type baseType) {
        this.baseType = baseType;
        baseType.setParent(this);
        return this;
    }

    public Term getCapacity() {
        return this.capacity;
    }

    public ListType setCapacity(Term capacity) {
        this.capacity = capacity;
        if (capacity != null) {
            capacity.setParent(this);
        }
        return this;
    }

    @Override
    public ListType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ListTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ListTypeContext", context.toString());
        }
        this.setParent(parent);
        this.setBaseType(Type.parse(((MediatorLangParser.ListTypeContext)context).type(), this));
        if (((MediatorLangParser.ListTypeContext)context).capacity == null) {
            this.setCapacity(null);
        } else {
            this.setCapacity(Term.parse(((MediatorLangParser.ListTypeContext)context).capacity, this));
        }
        return this;
    }

    public String toString() {
        return this.baseType.toString() + " [" + (this.capacity == null ? "" : this.capacity.toString()) + "]";
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public ListType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public ListType copy(RawElement parent) throws ValidationException {
        ListType nlt = new ListType();
        nlt.setParent(parent);
        nlt.setCapacity(this.getCapacity().copy(nlt));
        nlt.setBaseType(this.getBaseType().copy(nlt));
        return nlt;
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setBaseType(this.getBaseType().refactor(typeRewriteMap, termRewriteMap));
        this.setCapacity(this.getCapacity().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }
}

