/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.automaton;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.statement.Statements;
import org.fmgroup.mediator.language.statement.SynchronizingStatement;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class TransitionSingle
implements Transition,
Statements {
    private RawElement parent;
    private Term guard;
    private List<Statement> statements = new ArrayList<Statement>();
    private boolean isInternal = true;

    public List<Statement> getStatements() {
        return this.statements;
    }

    public TransitionSingle setStatements(List<Statement> statements) {
        this.statements = new ArrayList<Statement>();
        statements.forEach(this::addStatement);
        return this;
    }

    public int size() {
        return this.statements.size();
    }

    public Statement getStatement(int i) {
        return this.statements.get(i);
    }

    public TransitionSingle addStatement(Statement statement) {
        this.statements.add(statement);
        statement.setParent(this);
        if (statement instanceof SynchronizingStatement) {
            this.isInternal = false;
        }
        return this;
    }

    public boolean isInternal() {
        return this.isInternal;
    }

    @Override
    public TransitionSingle fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.TransitionSingleContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "TransitionSingleContext", context.toString());
        }
        this.setParent(parent);
        this.setGuard(Term.parse(((MediatorLangParser.TransitionSingleContext)context).term(), this));
        if (((MediatorLangParser.TransitionSingleContext)context).statement() != null) {
            this.addStatement(Statement.parse(((MediatorLangParser.TransitionSingleContext)context).statement(), this));
        } else {
            for (MediatorLangParser.StatementContext sc : ((MediatorLangParser.TransitionSingleContext)context).statements().statement()) {
                this.addStatement(Statement.parse(sc, this));
            }
        }
        return this;
    }

    public String toString() {
        String rel = this.guard.toString() + " -> ";
        if (this.statements.size() == 1) {
            return rel + this.statements.get(0).toString();
        }
        rel = rel + "{\n";
        for (Statement statement : this.statements) {
            rel = rel + UtilCode.addIndent(statement.toString(), 1) + "\n";
        }
        rel = rel + "}";
        return rel;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public TransitionSingle setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public TransitionSingle copy(RawElement parent) throws ValidationException {
        TransitionSingle nt = new TransitionSingle();
        nt.setParent(parent);
        nt.setGuard(this.guard.copy(nt));
        for (Statement st : this.statements) {
            nt.addStatement((Statement)st.copy(nt));
        }
        return nt;
    }

    @Override
    public Term getGuard() {
        return this.guard;
    }

    public TransitionSingle setGuard(Term guard) throws ValidationException {
        this.guard = guard;
        guard.setParent(this);
        return this;
    }

    @Override
    public TransitionSingle refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap, RawElement parent) throws ValidationException {
        this.parent = parent;
        this.setGuard(this.getGuard().refactor(typeRewriteMap, termRewriteMap));
        ArrayList<Statement> newStatements = new ArrayList<Statement>();
        for (Statement s : this.getStatements()) {
            newStatements.add(s.refactor(typeRewriteMap, termRewriteMap));
        }
        this.setStatements(newStatements);
        return this;
    }

    @Override
    public Statement nextStatement(Statement s) {
        if (this.statements.contains(s) && this.statements.indexOf(s) + 1 < this.statements.size()) {
            return this.statements.get(this.statements.indexOf(s) + 1);
        }
        return null;
    }
}

