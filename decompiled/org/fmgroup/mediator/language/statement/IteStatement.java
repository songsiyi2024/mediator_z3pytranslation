/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.statement;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.statement.Statements;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class IteStatement
implements Statement,
Statements {
    private RawElement parent;
    private Term condition;
    private List<Statement> thenStmts = new ArrayList<Statement>();
    private List<Statement> elseStmts = new ArrayList<Statement>();

    public Term getCondition() {
        return this.condition;
    }

    public IteStatement setCondition(Term condition) {
        this.condition = condition;
        condition.setParent(this);
        return this;
    }

    public List<Statement> getThenStmts() {
        return this.thenStmts;
    }

    public IteStatement setThenStmts(List<Statement> thenStmts) {
        this.thenStmts = new ArrayList<Statement>();
        thenStmts.forEach(this::addThenStmt);
        return this;
    }

    public IteStatement addThenStmt(Statement statement) {
        this.thenStmts.add(statement);
        statement.setParent(this);
        return this;
    }

    public List<Statement> getElseStmts() {
        return this.elseStmts;
    }

    public IteStatement setElseStmts(List<Statement> elseStmts) {
        this.elseStmts = new ArrayList<Statement>();
        elseStmts.forEach(this::addElseStmt);
        return this;
    }

    public IteStatement addElseStmt(Statement statement) {
        this.elseStmts.add(statement);
        statement.setParent(this);
        return this;
    }

    @Override
    public IteStatement fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.IteStatementContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "IteStatementContext", context.toString());
        }
        this.setParent(parent);
        this.setCondition(Term.parse(((MediatorLangParser.IteStatementContext)context).condition, this));
        if (((MediatorLangParser.IteStatementContext)context).thenstmt != null) {
            this.addThenStmt(Statement.parse(((MediatorLangParser.IteStatementContext)context).thenstmt, this));
        }
        if (((MediatorLangParser.IteStatementContext)context).thenstmts != null) {
            for (MediatorLangParser.StatementContext sc : ((MediatorLangParser.IteStatementContext)context).thenstmts.statement()) {
                this.addThenStmt(Statement.parse(sc, this));
            }
        }
        if (((MediatorLangParser.IteStatementContext)context).elsestmt != null) {
            this.addElseStmt(Statement.parse(((MediatorLangParser.IteStatementContext)context).elsestmt, this));
        }
        if (((MediatorLangParser.IteStatementContext)context).elsestmts != null) {
            for (MediatorLangParser.StatementContext sc : ((MediatorLangParser.IteStatementContext)context).elsestmts.statement()) {
                this.addElseStmt(Statement.parse(sc, this));
            }
        }
        return this;
    }

    public boolean equals(Object obj) {
        return this.toString().equals(obj.toString()) && obj instanceof Statement;
    }

    public String toString() {
        String rel = String.format("if (%s) ", this.condition.toString());
        if (this.thenStmts.size() == 1) {
            rel = rel + this.thenStmts.get(0).toString();
        } else {
            rel = rel + "{\n";
            for (Statement s : this.thenStmts) {
                rel = rel + UtilCode.addIndent(s.toString(), 1) + "\n";
            }
            rel = rel + "}";
        }
        if (this.elseStmts.size() > 0) {
            rel = rel + "\nelse ";
            if (this.elseStmts.size() == 1) {
                rel = rel + this.elseStmts.get(0).toString() + "\n";
            } else {
                rel = rel + "{\n";
                for (Statement s : this.elseStmts) {
                    rel = rel + UtilCode.addIndent(s.toString(), 1) + "\n";
                }
                rel = rel + "}";
            }
        }
        return rel;
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
        IteStatement nis = new IteStatement();
        nis.setParent(parent);
        nis.setCondition(this.condition.copy(nis));
        for (Statement st : this.thenStmts) {
            nis.addThenStmt((Statement)st.copy(nis));
        }
        for (Statement st : this.elseStmts) {
            nis.addElseStmt((Statement)st.copy(nis));
        }
        return nis;
    }

    @Override
    public Statement refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setCondition(this.getCondition().refactor(typeRewriteMap, termRewriteMap));
        for (Statement s : this.getThenStmts()) {
            s.refactor(typeRewriteMap, termRewriteMap);
        }
        for (Statement s : this.getElseStmts()) {
            s.refactor(typeRewriteMap, termRewriteMap);
        }
        return this;
    }

    @Override
    public Statement nextStatement(Statement s) {
        if (this.thenStmts.contains(s)) {
            if (this.thenStmts.indexOf(s) + 1 < this.thenStmts.size()) {
                return this.thenStmts.get(this.thenStmts.indexOf(s) + 1);
            }
            return null;
        }
        if (this.elseStmts.contains(s)) {
            if (this.elseStmts.indexOf(s) + 1 < this.elseStmts.size()) {
                return this.elseStmts.get(this.elseStmts.indexOf(s) + 1);
            }
            return null;
        }
        return null;
    }
}

