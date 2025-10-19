/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.termType;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class UnionType
implements Type {
    private RawElement parent = null;
    private List<Type> baseTypes = new ArrayList<Type>();

    public List<Type> getBaseTypes() {
        return this.baseTypes;
    }

    public UnionType setBaseTypes(List<Type> baseTypes) {
        this.baseTypes = new ArrayList<Type>();
        baseTypes.forEach(this::addBaseType);
        return this;
    }

    public UnionType addBaseType(Type baseType) {
        this.baseTypes.add(baseType);
        baseType.setParent(this);
        return this;
    }

    @Override
    public UnionType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.UnionTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "UnionTypeContext", context.toString());
        }
        this.setParent(parent);
        for (MediatorLangParser.TypeContext baseType : ((MediatorLangParser.UnionTypeContext)context).type()) {
            this.addBaseType(Type.parse(baseType, this));
        }
        return this;
    }

    public String toString() {
        String str = "";
        for (int i = 0; i < this.baseTypes.size(); ++i) {
            if (i > 0) {
                str = str + " | ";
            }
            str = str + this.baseTypes.get(i).toString();
        }
        return str;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public UnionType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public UnionType copy(RawElement parent) throws ValidationException {
        UnionType nut = new UnionType();
        nut.setParent(parent);
        for (Type t : this.getBaseTypes()) {
            nut.addBaseType(t.copy(nut));
        }
        return nut;
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        for (int i = 0; i < this.getBaseTypes().size(); ++i) {
            this.getBaseTypes().set(i, this.getBaseTypes().get(i).refactor(typeRewriteMap, termRewriteMap));
        }
        return this;
    }
}

