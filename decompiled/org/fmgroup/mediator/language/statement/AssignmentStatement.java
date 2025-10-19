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

public class AssignmentStatement
implements Statement {
    private Term expr;
    private Term target;
    private RawElement parent;

    public Term getTarget() {
        return this.target;
    }

    public AssignmentStatement setTarget(Term target) throws ValidationException {
        this.target = target;
        target.setParent(this);
        return this;
    }

    public Term getExpr() {
        return this.expr;
    }

    public AssignmentStatement setExpr(Term expr) throws ValidationException {
        this.expr = expr;
        expr.setParent(this);
        return this;
    }

    @Override
    public AssignmentStatement fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.AssignmentStatementContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "AssignmentStatementContext", context.toString());
        }
        this.setParent(parent);
        this.setExpr(Term.parse(((MediatorLangParser.AssignmentStatementContext)context).expr, this));
        if (((MediatorLangParser.AssignmentStatementContext)context).target != null) {
            this.setTarget(Term.parse(((MediatorLangParser.AssignmentStatementContext)context).target, this));
        }
        return this;
    }

    public String toString() {
        if (this.target != null) {
            return this.target.toString() + " = " + this.expr.toString() + ";";
        }
        return this.expr.toString() + ";";
    }

    public boolean equals(Object obj) {
        return this.toString().equals(obj.toString()) && obj instanceof Statement;
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
        AssignmentStatement nas = new AssignmentStatement();
        nas.setParent(parent);
        nas.setExpr(this.getExpr().copy(nas));
        if (this.target != null) {
            nas.setTarget(this.getTarget().copy(nas));
        }
        return nas;
    }

    @Override
    public Statement refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setExpr(this.getExpr().refactor(typeRewriteMap, termRewriteMap));
        if (this.getTarget() != null) {
            this.setTarget(this.getTarget().refactor(typeRewriteMap, termRewriteMap));
        }
        return this;
    }
}

