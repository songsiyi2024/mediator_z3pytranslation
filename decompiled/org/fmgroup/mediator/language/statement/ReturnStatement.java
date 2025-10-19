/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.statement;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class ReturnStatement
implements Statement {
    private RawElement parent;
    private Term returnedValue;

    public Term getReturnedValue() {
        return this.returnedValue;
    }

    public ReturnStatement setReturnedValue(Term returnedValue) {
        this.returnedValue = returnedValue;
        returnedValue.setParent(this);
        return this;
    }

    @Override
    public ReturnStatement fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ReturnStatementContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ReturnStatementContext", context.toString());
        }
        this.setParent(parent);
        this.setReturnedValue(Term.parse(((MediatorLangParser.ReturnStatementContext)context).term(), this));
        return this;
    }

    public boolean equals(Object obj) {
        return this.toString().equals(obj.toString()) && obj instanceof Statement;
    }

    public String toString() {
        return "return " + this.returnedValue.toString() + ";";
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
    public RawElement copy(RawElement parent) throws ValidationException {
        ReturnStatement nrs = new ReturnStatement();
        nrs.setParent(parent);
        nrs.setReturnedValue(this.getReturnedValue().copy(nrs));
        return nrs;
    }

    @Override
    public Statement refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setReturnedValue(this.getReturnedValue().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }
}

