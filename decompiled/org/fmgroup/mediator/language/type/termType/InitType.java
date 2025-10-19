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

public class InitType
implements Type {
    private RawElement parent = null;
    private Term defaultValue = null;
    private Type baseType = null;

    public Term getDefaultValue() {
        return this.defaultValue;
    }

    public InitType setDefaultValue(Term value) {
        this.defaultValue = value;
        value.setParent(this);
        return this;
    }

    public Type getBaseType() {
        return this.baseType;
    }

    public InitType setBaseType(Type baseType) {
        this.baseType = baseType;
        baseType.setParent(this);
        return this;
    }

    @Override
    public InitType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.InitTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "InitTypeContext", context.toString());
        }
        this.setParent(parent);
        this.setDefaultValue(Term.parse(((MediatorLangParser.InitTypeContext)context).term(), this));
        this.setBaseType(Type.parse(((MediatorLangParser.InitTypeContext)context).type(), this));
        return this;
    }

    @Override
    public Term getInitValue() throws ValidationException {
        return this.getDefaultValue().copy();
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setBaseType(this.getBaseType().refactor(typeRewriteMap, termRewriteMap));
        this.setDefaultValue(this.getDefaultValue().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }

    public String toString() {
        return this.baseType.toString() + " init " + this.defaultValue.toString();
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public InitType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public InitType copy(RawElement parent) throws ValidationException {
        InitType nit = new InitType();
        nit.setParent(parent);
        nit.setBaseType(this.getBaseType().copy(nit));
        nit.setDefaultValue(this.getDefaultValue().copy(nit));
        return nit;
    }

    @Override
    public Type extractRawType() throws ValidationException {
        return this.baseType;
    }
}

