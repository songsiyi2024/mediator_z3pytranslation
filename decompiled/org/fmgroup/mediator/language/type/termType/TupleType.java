/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.termType;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class TupleType
implements Type {
    private RawElement parent = null;
    private List<Type> baseTypes = new ArrayList<Type>();

    public List<Type> getBaseTypes() {
        return this.baseTypes;
    }

    public TupleType setBaseTypes(List<Type> baseTypes) {
        this.baseTypes = baseTypes;
        return this;
    }

    public TupleType addBaseType(Type baseType) {
        this.baseTypes.add(baseType);
        baseType.setParent(this);
        return this;
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        for (int i = 0; i < this.baseTypes.size(); ++i) {
            this.baseTypes.set(i, this.baseTypes.get(i).refactor(typeRewriteMap, termRewriteMap));
        }
        return this;
    }

    @Override
    public TupleType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        this.setParent(parent);
        if (!(context instanceof MediatorLangParser.TupleTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "TupleTypeContext", context.toString());
        }
        for (MediatorLangParser.TypeContext baseType : ((MediatorLangParser.TupleTypeContext)context).type()) {
            this.addBaseType(Type.parse(baseType, this));
        }
        return this;
    }

    public String toString() {
        return String.format("(%s)", this.baseTypes.stream().map(Object::toString).collect(Collectors.joining(", ")));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public TupleType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

