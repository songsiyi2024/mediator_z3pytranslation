package org.fmgroup.mediator.plugins.generators.z3;

import java.util.ArrayList;
import java.util.List;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import org.fmgroup.mediator.language.statement.AssignmentStatement;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.term.BinaryOperatorTerm;
import org.fmgroup.mediator.language.term.EnumBinaryOperator;
import org.fmgroup.mediator.language.term.EnumSingleOperator;
import org.fmgroup.mediator.language.term.FieldTerm;
import org.fmgroup.mediator.language.term.IdValue;
import org.fmgroup.mediator.language.term.IntValue;
import org.fmgroup.mediator.language.term.SingleOperatorTerm;
import org.fmgroup.mediator.language.term.FieldTerm;
import org.fmgroup.mediator.language.term.IteTerm;
import org.fmgroup.mediator.language.term.StructTerm;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugin.generator.Generator;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoGeneratorException;

/**
 * A simple Z3 generator that emits a Z3 Python script performing bounded-safety check (k steps).
 * Minimal support: Automaton, integer and boolean local variables, simple guards and assignments.
 */
public class Z3Generator implements Generator {

    private static final int DEFAULT_K = 10;

    @Override
    public FileSet generate(RawElement elem) throws ArduinoGeneratorException {
        try {
            if (!(elem instanceof Automaton)) {
                throw new ArduinoGeneratorException("Z3Generator only supports Automaton elements");
            }
            Automaton autom = (Automaton) elem;
            String name = autom.getName();
            String py = renderZ3Script(autom, DEFAULT_K);
            FileSet fs = new FileSet();
            fs.add(name + "_z3_check.py", py);
            return fs;
        } catch (Exception e) {
            throw new ArduinoGeneratorException(e.getMessage());
        }
    }

    @Override
    public boolean available(RawElement elem) throws ArduinoGeneratorException {
        return elem instanceof Automaton;
    }

    @Override
    public String getSupportedPlatform() {
        return "z3";
    }

    @Override
    public String getName() {
        return "Z3Generator";
    }

    @Override
    public String getVersion() {
        return "0.0.1";
    }

    @Override
    public String getDescription() {
        return "Generate Z3 Python script for bounded safety checking";
    }

    private String renderZ3Script(Automaton autom, int k) throws ValidationException {
        StringBuilder sb = new StringBuilder();
        sb.append("from z3 import *\n\n");

        // collect variables
        VariableDeclarationCollection vars = autom.getLocalVars();
        List<String> varNames = new ArrayList<String>();
        for (VariableDeclaration vd : vars.getDeclarationList()) {
            for (String id : vd.getIdentifiers()) {
                varNames.add(id);
            }
        }

        // declare per-step variables
        for (int t = 0; t <= k; t++) {
            for (String v : varNames) {
                sb.append(String.format("%s_%d = Int('%s_%d')\n", v, t, v, t));
            }
            sb.append("\n");
        }

        // initial constraints: use init values from variable declarations when available
        sb.append("s = Solver()\n");
        for (VariableDeclaration vd : vars.getDeclarationList()) {
            for (String id : vd.getIdentifiers()) {
                Term init = vd.getType().getInitValue();
                if (init != null) {
                    String expr0 = termToZ3(init, 0);
                    sb.append(String.format("s.add(%s_0 == %s)\n", id, expr0));
                }
            }
        }
        sb.append("\n");

        // encode transitions as per-step constraints: for simplicity, build disjunction of possible transitions
        List<Transition> transitions = autom.getTransitions();
        for (int t = 0; t < k; t++) {
            StringBuilder stepCond = new StringBuilder();
            stepCond.append("Or(");
            boolean firstTrans = true;
            for (Transition tr : transitions) {
                if (!(tr instanceof TransitionSingle)) continue;
                TransitionSingle ts = (TransitionSingle) tr;
                String guard = termToZ3(ts.getGuard(), t);
                // build effects: assignments
                StringBuilder effects = new StringBuilder();
                List<Statement> stmts = ts.getStatements();
                List<String> updates = new ArrayList<String>();
                for (Statement s : stmts) {
                    if (s instanceof AssignmentStatement) {
                        AssignmentStatement as = (AssignmentStatement) s;
                        String left = as.getTarget().toString();
                        String right = termToZ3(as.getExpr(), t);
                        updates.add(String.format("%s_%d == %s", left, t+1, right));
                    }
                }
                // default: copy unchanged vars
                for (String v : varNames) {
                    boolean updated = false;
                    for (String up : updates) {
                        if (up.startsWith(v + "_")) { updated = true; break; }
                    }
                    if (!updated) {
                        updates.add(String.format("%s_%d == %s_%d", v, t+1, v, t));
                    }
                }
                String updatesConj = String.join(", ", updates);
                String transExpr = String.format("And(%s, %s)", guard, updatesConj.isEmpty() ? "True" : updatesConj);
                if (!firstTrans) stepCond.append(", ");
                stepCond.append(transExpr);
                firstTrans = false;
            }
            stepCond.append(")\n");
            sb.append(String.format("s.add(%s)\n", stepCond.toString()));
            sb.append("\n");
        }

        // NOTE: property handling not implemented in prototype. Users can inspect generated script and add assertions.

        sb.append("print(s.check())\n");
    sb.append("if s.check() == sat:\n");
    sb.append("    m = s.model()\n");
    sb.append("    print(\"counterexample model:\")\n");
    sb.append("    print(m)\n");
        return sb.toString();
    }

    private String termToZ3(Term term, int t) throws ValidationException {
        if (term == null) {
            // unknown term -> produce a boolean false by default to avoid producing integer 0 in guards
            return "False";
        }

        // Identifier (variable or enum constant)
        if (term instanceof IdValue) {
            IdValue id = (IdValue) term;
            String name = id.getIdentifier();
            if ("null".equals(name)) {
                // use -1 as a NULL sentinel for integer/optional fields
                return String.valueOf(-1);
            }
            return String.format("%s_%d", name, t);
        }

        // Integer literal
        if (term instanceof IntValue) {
            IntValue iv = (IntValue) term;
            return String.valueOf(iv.getValue());
        }

        // Boolean literal
        if (term instanceof BoolValue) {
            BoolValue bv = (BoolValue) term;
            return bv.getValue() ? "True" : "False";
        }

        // Null literal
        if (term instanceof NullValue) {
            return String.valueOf(-1);
        }

        // Enum literal - map to a string literal for now (generator may instead emit integer constants)
        if (term instanceof EnumValue) {
            EnumValue ev = (EnumValue) term;
            // prefer a quoted name; translation of enums to ints should be centralized in type mapping
            return String.format("\"%s\"", ev.getIdentifier());
        }

        // Field access: <owner>.<field> -> translate to flattened name owner_field_t
        if (term instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) term;
            Term owner = ft.getOwner();
            String field = ft.getField();
            if (owner instanceof IdValue) {
                String ownerName = ((IdValue) owner).getIdentifier();
                return String.format("%s_%s_%d", ownerName, field, t);
            } else {
                // fallback: try to render owner and append field (may contain a time suffix)
                String ownerStr = termToZ3(owner, t);
                // strip trailing _<t> if present
                ownerStr = ownerStr.replaceAll("_(\\d+)$", "");
                return String.format("%s_%s_%d", ownerStr, field, t);
            }
        }

        // Struct literal: produce a Python dict of field->expr (caller must handle assignment expansion)
        if (term instanceof StructTerm) {
            StructTerm st = (StructTerm) term;
            StringBuilder sb = new StringBuilder();
            sb.append("{");
            boolean first = true;
            for (java.util.Map.Entry<String, Term> e : st.getFields().entrySet()) {
                if (!first) sb.append(", ");
                sb.append(String.format("\"%s\": %s", e.getKey(), termToZ3(e.getValue(), t)));
                first = false;
            }
            sb.append("}");
            return sb.toString();
        }

        // ITE (cond ? then : else)
        if (term instanceof IteTerm) {
            IteTerm it = (IteTerm) term;
            String c = termToZ3(it.getCondition(), t);
            String th = termToZ3(it.getThenTerm(), t);
            String el = termToZ3(it.getElseTerm(), t);
            return String.format("If(%s, %s, %s)", c, th, el);
        }

        // Binary operator (logical, comparison, arithmetic)
        if (term instanceof BinaryOperatorTerm) {
            BinaryOperatorTerm bt = (BinaryOperatorTerm) term;
            String l = termToZ3(bt.getLeft(), t);
            String r = termToZ3(bt.getRight(), t);
            EnumBinaryOperator opr = bt.getOpr();
            switch (opr) {
                case LAND: return String.format("And(%s, %s)", l, r);
                case LOR: return String.format("Or(%s, %s)", l, r);
                case EQ: return String.format("%s == %s", l, r);
                case NEQ: return String.format("Not(%s == %s)", l, r);
                case LT: return String.format("%s < %s", l, r);
                case LEQ: return String.format("%s <= %s", l, r);
                case GT: return String.format("%s > %s", l, r);
                case GEQ: return String.format("%s >= %s", l, r);
                case ADD: return String.format("(%s + %s)", l, r);
                case MINUS: return String.format("(%s - %s)", l, r);
                case TIMES: return String.format("(%s * %s)", l, r);
                case DIV: return String.format("(ToReal(%s) / ToReal(%s))", l, r);
                case MOD: return String.format("Mod(%s, %s)", l, r);
            }
        }

        // Unary operator (logical not)
        if (term instanceof SingleOperatorTerm) {
            SingleOperatorTerm st = (SingleOperatorTerm) term;
            EnumSingleOperator opr = st.getOpr();
            String inner = termToZ3(st.getTerm(), t);
            if (opr == EnumSingleOperator.LNOT) return String.format("Not(%s)", inner);
        }

        // fallback: unsupported term -> raise explicit error so user knows to extend generator
        throw ValidationException.UnderDevelopment();
    }
}
