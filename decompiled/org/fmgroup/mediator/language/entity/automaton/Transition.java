/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.automaton;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.automaton.TransitionGroup;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public interface Transition
extends RawElement {
    public static Transition parse(MediatorLangParser.TransitionContext context, RawElement parent) throws ValidationException {
        if (context instanceof MediatorLangParser.TransitionSingleContext) {
            return new TransitionSingle().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.TransitionGroupContext) {
            return new TransitionGroup().fromContext(context, parent);
        }
        throw ValidationException.UnregisteredTransition(context.getClass().toString());
    }

    public Term getGuard() throws ValidationException;

    default public Automaton getAutomaton() throws ValidationException {
        Scope currScope = this.getCurrentScope();
        if (currScope instanceof Automaton) {
            return (Automaton)currScope;
        }
        throw ValidationException.UnexpectedElement(Automaton.class, currScope.getClass(), "Automaton", "scope");
    }

    default public Transition refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap, RawElement parent) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }
}

