/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.simulator;

import java.util.HashMap;
import java.util.Map;
import org.fmgroup.mediator.environment.operators.BinaryOperatorEQ;
import org.fmgroup.mediator.environment.operators.BinaryOperatorLAND;
import org.fmgroup.mediator.environment.operators.BinaryOperatorLOR;
import org.fmgroup.mediator.environment.operators.SingleOperatorLNOT;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.term.BinaryOperatorTerm;
import org.fmgroup.mediator.language.term.EnumBinaryOperator;
import org.fmgroup.mediator.language.term.EnumSingleOperator;
import org.fmgroup.mediator.language.term.IdValue;
import org.fmgroup.mediator.language.term.SingleOperatorTerm;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.term.Value;
import org.fmgroup.mediator.plugins.simulator.Evaluation;
import org.fmgroup.mediator.plugins.simulator.SimulatorException;

public class EvaluationAutomaton
implements Evaluation {
    private Map<String, Term> valueMap = new HashMap<String, Term>();

    public void set(String identifier, Term val) {
        this.valueMap.put(identifier, val);
    }

    public Term get(String identifier) {
        return this.valueMap.get(identifier);
    }

    @Override
    public EvaluationAutomaton copy() throws ValidationException {
        EvaluationAutomaton result = new EvaluationAutomaton();
        for (String var : this.valueMap.keySet()) {
            result.set(var, this.get(var).copy());
        }
        return result;
    }

    public EvaluationAutomaton update(Term target, Term value) throws ValidationException {
        EvaluationAutomaton newev = this.copy();
        if (target instanceof IdValue && ((IdValue)target).getScopeIdentifiers().size() == 0) {
            newev.set(((IdValue)target).getIdentifier(), value);
        }
        return newev;
    }

    public Term eval(Term raw) throws SimulatorException {
        if (raw instanceof IdValue) {
            return this.valueMap.get(((IdValue)raw).getIdentifier());
        }
        if (raw instanceof Value) {
            return raw;
        }
        if (raw instanceof BinaryOperatorTerm) {
            Term left = this.eval(((BinaryOperatorTerm)raw).getLeft());
            Term right = this.eval(((BinaryOperatorTerm)raw).getRight());
            if (((BinaryOperatorTerm)raw).getOpr() == EnumBinaryOperator.LAND) {
                return BinaryOperatorLAND.compute(left, right);
            }
            if (((BinaryOperatorTerm)raw).getOpr() == EnumBinaryOperator.LOR) {
                return BinaryOperatorLOR.compute(left, right);
            }
            if (((BinaryOperatorTerm)raw).getOpr() == EnumBinaryOperator.NEQ) {
                return SingleOperatorLNOT.compute(BinaryOperatorEQ.compute(left, right));
            }
            if (((BinaryOperatorTerm)raw).getOpr() == EnumBinaryOperator.EQ) {
                return BinaryOperatorEQ.compute(left, right);
            }
        }
        if (raw instanceof SingleOperatorTerm) {
            Term t = this.eval(((SingleOperatorTerm)raw).getTerm());
            if (((SingleOperatorTerm)raw).getOpr() == EnumSingleOperator.LNOT) {
                return SingleOperatorLNOT.compute(t);
            }
        }
        throw SimulatorException.UnderDevelopment();
    }
}

