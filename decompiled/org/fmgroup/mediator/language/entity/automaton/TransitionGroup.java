/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.automaton;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.BinaryOperatorTerm;
import org.fmgroup.mediator.language.term.EnumBinaryOperator;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class TransitionGroup
implements Transition,
RawElement {
    private RawElement parent;
    private List<Transition> transitions = new ArrayList<Transition>();

    public List<Transition> getTransitions() {
        return this.transitions;
    }

    public TransitionGroup setTransitions(List<Transition> transitions) throws ValidationException {
        this.transitions = new ArrayList<Transition>();
        for (Transition t : transitions) {
            this.addTransition(t);
        }
        return this;
    }

    public TransitionGroup addTransition(Transition transition) throws ValidationException {
        if (transition instanceof TransitionGroup) {
            throw ValidationException.UnexpectedElement(this.getClass(), transition.getClass(), "TransitionSingle", "sub-transitions");
        }
        this.transitions.add((TransitionSingle)transition);
        transition.setParent(this);
        return this;
    }

    @Override
    public TransitionGroup fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.TransitionGroupContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "TransitionGroupContext", context.toString());
        }
        this.setParent(parent);
        for (MediatorLangParser.TransitionContext tc : ((MediatorLangParser.TransitionGroupContext)context).transition()) {
            this.addTransition(Transition.parse(tc, this));
        }
        return this;
    }

    public String toString() {
        return String.format("group {\n%s\n}", UtilCode.addIndent(this.getTransitions().stream().map(Object::toString).collect(Collectors.joining("\n")), 1));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public TransitionGroup setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public TransitionGroup copy(RawElement parent) throws ValidationException {
        TransitionGroup transG = new TransitionGroup();
        transG.setParent(parent);
        for (Transition t : this.getTransitions()) {
            transG.addTransition((Transition)t.copy(transG));
        }
        return transG;
    }

    @Override
    public Term getGuard() throws ValidationException {
        Term guard = null;
        for (Transition t : this.transitions) {
            if (guard == null) {
                guard = t.getGuard();
                continue;
            }
            guard = new BinaryOperatorTerm().setOpr(EnumBinaryOperator.LOR).setLeft(guard).setRight(t.getGuard());
        }
        return guard;
    }

    @Override
    public TransitionGroup refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap, RawElement parent) throws ValidationException {
        this.setParent(parent);
        for (int i = 0; i < this.transitions.size(); ++i) {
            this.transitions.set(i, this.transitions.get(i).refactor(typeRewriteMap, termRewriteMap, this));
        }
        return this;
    }
}

