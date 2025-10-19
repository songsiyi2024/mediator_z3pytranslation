/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.statement;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.statement.AssignmentStatement;
import org.fmgroup.mediator.language.statement.IteStatement;
import org.fmgroup.mediator.language.statement.ReturnStatement;
import org.fmgroup.mediator.language.statement.SynchronizingStatement;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public interface Statement
extends RawElement {
    public static Statement parse(MediatorLangParser.StatementContext sc, RawElement parent) throws ValidationException {
        if (sc instanceof MediatorLangParser.AssignmentStatementContext) {
            return new AssignmentStatement().fromContext(sc, parent);
        }
        if (sc instanceof MediatorLangParser.SynchronizingStatementContext) {
            return new SynchronizingStatement().fromContext(sc, parent);
        }
        if (sc instanceof MediatorLangParser.IteStatementContext) {
            return new IteStatement().fromContext(sc, parent);
        }
        if (sc instanceof MediatorLangParser.ReturnStatementContext) {
            return new ReturnStatement().fromContext(sc, parent);
        }
        throw ValidationException.UnregisteredStatement(sc.getClass().toString());
    }

    public Statement refactor(Map<String, Type> var1, Map<String, Term> var2) throws ValidationException;
}

