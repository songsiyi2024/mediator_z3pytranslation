/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.simulator;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.entity.automaton.TransitionGroup;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.statement.AssignmentStatement;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.statement.Statements;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.plugin.Plugin;
import org.fmgroup.mediator.plugins.simulator.Evaluation;
import org.fmgroup.mediator.plugins.simulator.EvaluationAutomaton;
import org.fmgroup.mediator.plugins.simulator.SimulatorException;
import org.fmgroup.mediator.plugins.simulator.SimulatorState;

public class Simulator
implements Plugin {
    private Entity entity;
    private List<SimulatorState> trace = new ArrayList<SimulatorState>();
    private int position;

    public Simulator() {
    }

    public Simulator(Entity entity) throws SimulatorException, ValidationException {
        this.entity = entity;
        this.initialization();
    }

    public void initialization() throws SimulatorException, ValidationException {
        EvaluationAutomaton ev;
        SimulatorState s = new SimulatorState();
        if (this.entity instanceof Automaton) {
            ev = new EvaluationAutomaton();
            s.setEvaluation(ev);
            for (VariableDeclaration vardecl : ((Automaton)this.entity).getLocalVars().getDeclarationList()) {
                for (String identifier : vardecl.getIdentifiers()) {
                    ev.set(identifier, vardecl.getType().getInitValue());
                }
            }
        } else {
            throw SimulatorException.UnderDevelopment();
        }
        s.setSelectedTransition(this.nextTransition(ev));
        this.trace.add(s);
    }

    public void stepForward() throws SimulatorException, ValidationException {
        assert (this.trace.size() > 0);
        if (this.entity instanceof Automaton) {
            SimulatorState ss = this.trace.get(this.trace.size() - 1);
            SimulatorState ssNext = new SimulatorState();
            EvaluationAutomaton ev = (EvaluationAutomaton)ss.getEvaluation();
            EvaluationAutomaton bufev = (EvaluationAutomaton)ss.getBufferedEvaluation();
            Statement stmt = ss.getSelectedStatement();
            if (stmt == null) {
                if (ss.getBufferedEvaluation() != null) {
                    ssNext.setEvaluation(bufev.copy());
                    ssNext.setBufferedEvaluation(null);
                    ssNext.setSelectedTransition(this.nextTransition(ev));
                    ssNext.setSelectedStatement(null);
                } else {
                    ssNext.setEvaluation(ev.copy());
                    ssNext.setBufferedEvaluation(ev.copy());
                    ssNext.setSelectedStatement(this.nextStatement(ev, ss));
                    ssNext.setSelectedTransition(ss.getSelectedTransition());
                }
            } else if (stmt instanceof AssignmentStatement) {
                Term evresult = bufev.eval(((AssignmentStatement)stmt).getExpr());
                ssNext.setEvaluation(ev);
                ssNext.setBufferedEvaluation(bufev.update(((AssignmentStatement)stmt).getTarget(), evresult));
                ssNext.setSelectedTransition(ss.getSelectedTransition());
                ssNext.setSelectedStatement(this.nextStatement(bufev, ss));
            } else {
                throw SimulatorException.UnderDevelopment();
            }
            this.trace.add(ssNext);
        }
    }

    public void restartFrom(int position) {
    }

    private TransitionSingle nextTransition(Evaluation ev) throws SimulatorException, ValidationException {
        if (this.entity instanceof Automaton && ev instanceof EvaluationAutomaton) {
            for (Transition t : ((Automaton)this.entity).getTransitions()) {
                if (t instanceof TransitionSingle) {
                    if (!((EvaluationAutomaton)ev).eval(t.getGuard()).equals(Boolean.TRUE)) continue;
                    return (TransitionSingle)t;
                }
                if (!(t instanceof TransitionGroup)) continue;
                ArrayList<TransitionSingle> options = new ArrayList<TransitionSingle>();
                for (Transition st : ((TransitionGroup)t).getTransitions()) {
                    assert (st instanceof TransitionSingle);
                    if (!((EvaluationAutomaton)ev).eval(st.getGuard()).equals(Boolean.TRUE)) continue;
                    options.add((TransitionSingle)st);
                }
                if (options.size() <= 0) continue;
                Random rand = new Random();
                return (TransitionSingle)options.get(rand.nextInt(options.size()));
            }
        } else {
            throw SimulatorException.UnderDevelopment();
        }
        return null;
    }

    private Statement nextStatement(Evaluation ev, SimulatorState ss) throws SimulatorException, ValidationException {
        Statement curr = ss.getSelectedStatement();
        if (curr == null) {
            if (ss.getSelectedTransition().getStatements().size() > 0) {
                return ss.getSelectedTransition().getStatements().get(0);
            }
            return null;
        }
        if (curr.getParent() instanceof Statements) {
            return ((Statements)((Object)curr.getParent())).nextStatement(curr);
        }
        throw SimulatorException.UnderDevelopment();
    }

    @Override
    public String getName() {
        return "Simulator";
    }

    @Override
    public String getVersion() {
        return "0.0.1";
    }

    @Override
    public String getDescription() {
        return "a simple simulator based on parallel semantics";
    }
}

