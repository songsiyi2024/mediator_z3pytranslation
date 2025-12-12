package org.fmgroup.mediator.plugins.generators.z3;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;
import java.util.HashMap;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.entity.automaton.TransitionGroup;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.property.Property;
import org.fmgroup.mediator.language.property.PropertyCollection;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.AtomicPathFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.GloballyStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;
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
import org.fmgroup.mediator.language.term.IteTerm;
import org.fmgroup.mediator.language.term.StructTerm;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.language.term.DoubleValue;
import org.fmgroup.mediator.language.term.CallTerm;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.termType.StructType;
import org.fmgroup.mediator.language.type.termType.EnumType;
import org.fmgroup.mediator.language.type.termType.UnionType;
import org.fmgroup.mediator.language.type.termType.BoolType;
import org.fmgroup.mediator.language.type.termType.IntType;
import org.fmgroup.mediator.language.type.termType.DoubleType;
import org.fmgroup.mediator.language.type.termType.BoundedIntType;
import org.fmgroup.mediator.language.type.termType.InitType;
import org.fmgroup.mediator.language.type.termType.IdType;
import org.fmgroup.mediator.language.entity.system.System;
import org.fmgroup.mediator.plugins.scheduler.Scheduler;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugin.generator.Generator;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoGeneratorException;

/**
 * A simple Z3 generator that emits a Z3 Python script performing bounded-safety check (k steps).
 * Refactored for better modularity and extensibility.
 */
public class Z3Generator implements Generator {

    private int k = 20;
    
    // Context for generation
    private Map<org.fmgroup.mediator.language.type.termType.EnumType, Map<String, String>> enumItemConstMap = new HashMap<>();
    private Map<String, String> globalEnumAliasMap = new HashMap<>();
    private int enumGlobalCounter = 0;
    private Map<String, Map<String, Type>> varFields = new LinkedHashMap<>();

    public void setBound(int k) {
        this.k = k;
    }

    @Override
    public FileSet generate(RawElement elem) throws ArduinoGeneratorException {
        try {
            Automaton autom;
            if (elem instanceof System) {
                autom = Scheduler.Schedule((System) elem);
            } else if (elem instanceof Automaton) {
                autom = (Automaton) elem;
            } else {
                throw new ArduinoGeneratorException("Z3Generator supports Automaton or System elements");
            }

            String name = autom.getName();
            String py = renderZ3Script(autom, this.k);
            FileSet fs = new FileSet();
            fs.add(name + "_z3_check.py", py);

            try {
                fs.add("../flattened_automaton/flattened_" + name + ".med", autom.toString());
            } catch (Exception e) {
                java.lang.System.err.println("Failed to add flattened automaton to FileSet: " + e.getMessage());
            }

            return fs;
        } catch (Exception e) {
            throw new ArduinoGeneratorException(e.getMessage());
        }
    }

    @Override
    public boolean available(RawElement elem) throws ArduinoGeneratorException {
        return elem instanceof Automaton || elem instanceof System;
    }

    @Override
    public String getSupportedPlatform() {
        return "Z3";
    }

    @Override
    public String getName() {
        return "Z3Generator";
    }

    @Override
    public String getVersion() {
        return "0.0.2";
    }

    @Override
    public String getDescription() {
        return "Generate Z3 Python script for bounded safety checking (Refactored)";
    }

    private String renderZ3Script(Automaton autom, int k) throws ValidationException {
        StringBuilder sb = new StringBuilder();
        
        generatePreamble(sb);
        prepareVariables(autom);
        generateEnumDefinitions(sb);
        generateVariableDeclarations(sb, k);
        generateInitConstraints(sb, autom);
        generateTransitionConstraints(sb, autom, k);
        generatePropertyVerification(sb, autom, k);
        generateFooter(sb);

        return sb.toString();
    }

    private void generatePreamble(StringBuilder sb) {
        sb.append("from z3 import *\n\n");
        sb.append("def to_real(x):\n");
        sb.append("    if isinstance(x, int):\n");
        sb.append("        return RealVal(x)\n");
        sb.append("    if isinstance(x, float):\n");
        sb.append("        return RealVal(x)\n");
        sb.append("    if is_int(x):\n");
        sb.append("        return ToReal(x)\n");
        sb.append("    return x\n\n");
    }

    private void prepareVariables(Automaton autom) {
        VariableDeclarationCollection vars = autom.getLocalVars();
        varFields.clear();
        enumItemConstMap.clear();
        globalEnumAliasMap.clear();
        enumGlobalCounter = 0;

        for (VariableDeclaration vd : vars.getDeclarationList()) {
            for (String id : vd.getIdentifiers()) {
                Type vt = vd.getType();
                Type resolved = resolveType(vt);
                
                if (resolved instanceof StructType) {
                    StructType st = (StructType) resolved;
                    Map<String, Type> fields = new LinkedHashMap<>();
                    for (Map.Entry<String, Type> e : st.getFields().entrySet()) {
                        fields.put(e.getKey(), e.getValue());
                    }
                    varFields.put(id, fields);
                } else if (resolved instanceof EnumType) {
                    EnumType et = (EnumType) resolved;
                    if (!enumItemConstMap.containsKey(et)) {
                        Map<String, String> itemMap = new LinkedHashMap<>();
                        String prefix = String.format("ENUM_%d", enumGlobalCounter++);
                        int idx = 0;
                        for (String item : et.getItems()) {
                            String constName = String.format("%s_%s", prefix, item.replaceAll("[^A-Za-z0-9_]", "_"));
                            itemMap.put(item, constName);
                            globalEnumAliasMap.put(item, constName);
                            idx++;
                        }
                        enumItemConstMap.put(et, itemMap);
                    }
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id, resolved);
                    varFields.put(id, fields);
                } else if (resolved instanceof UnionType) {
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id + "_tag", null); // TODO: proper type for tag
                    fields.put(id + "_val", null); // TODO: proper type for value
                    varFields.put(id, fields);
                } else {
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id, resolved);
                    varFields.put(id, fields);
                }
            }
        }
    }

    private void generateEnumDefinitions(StringBuilder sb) {
        for (Map.Entry<EnumType, Map<String, String>> e : enumItemConstMap.entrySet()) {
            int idx = 0;
            for (Map.Entry<String, String> it : e.getValue().entrySet()) {
                sb.append(String.format("%s = %d\n", it.getValue(), idx));
                idx++;
            }
            sb.append("\n");
        }
    }

    private void generateVariableDeclarations(StringBuilder sb, int k) {
        for (int t = 0; t <= k; t++) {
            for (Map.Entry<String, Map<String, Type>> e : varFields.entrySet()) {
                String base = e.getKey();
                for (String field : e.getValue().keySet()) {
                    String atomName = field.equals(base) ? base : (base + "_" + field);
                    Type ftype = e.getValue().get(field);
                    
                    if (t == 0) {
                         // java.lang.System.out.println("DEBUG: Variable " + atomName + " type is " + (ftype != null ? ftype.getClass().getName() : "null"));
                    }
                    
                    if (ftype instanceof BoolType) {
                        sb.append(String.format("%s_%d = Bool('%s_%d')\n", atomName, t, atomName, t));
                    } else if (ftype instanceof DoubleType) {
                        sb.append(String.format("%s_%d = Real('%s_%d')\n", atomName, t, atomName, t));
                    } else {
                        sb.append(String.format("%s_%d = Int('%s_%d')\n", atomName, t, atomName, t));
                    }
                }
            }
            sb.append("\n");
        }
    }

    private void generateInitConstraints(StringBuilder sb, Automaton autom) throws ValidationException {
        sb.append("s = Solver()\n");
        VariableDeclarationCollection vars = autom.getLocalVars();
        
        for (VariableDeclaration vd : vars.getDeclarationList()) {
            for (String id : vd.getIdentifiers()) {
                Term init = null;
                try {
                    init = vd.getType().getInitValue();
                } catch (ValidationException e) {
                    // ignore
                }
                
                if (init == null) {
                    Type t = resolveType(vd.getType());
                    if (t instanceof IntType) init = new IntValue().setValue(0);
                    else if (t instanceof BoundedIntType) init = ((BoundedIntType) t).getLowerBound();
                    else if (t instanceof DoubleType) init = new DoubleValue().setValue(0.0);
                    else if (t instanceof BoolType) init = new BoolValue().setValue(false);
                }

                if (init != null) {
                    if (init instanceof StructTerm) {
                        StructTerm st = (StructTerm) init;
                        for (Map.Entry<String, Term> e : st.getFields().entrySet()) {
                            String atom = e.getKey().equals(id) ? id : (id + "_" + e.getKey());
                            String expr0 = termToZ3(e.getValue(), 0);
                            sb.append(String.format("s.add(%s_0 == %s)\n", atom, expr0));
                        }
                    } else {
                        String expr0 = termToZ3(init, 0);
                        sb.append(String.format("s.add(%s_0 == %s)\n", id, expr0));
                    }
                }
            }
        }
        sb.append("\n");
    }

    private void generateTransitionConstraints(StringBuilder sb, Automaton autom, int k) throws ValidationException {
        List<TransitionSingle> transitions = flattenTransitions(autom.getTransitions());
        for (int t = 0; t < k; t++) {
            StringBuilder stepCond = new StringBuilder();
            stepCond.append("Or(");
            boolean firstTrans = true;
            
            for (TransitionSingle ts : transitions) {
                String guard = termToZ3(ts.getGuard(), t);
                
                // Track imperative updates within the transition
                Map<String, String> currentEnv = new HashMap<>();
                Map<String, String> nextStateValues = new HashMap<>();

                for (Statement st : ts.getStatements()) {
                    if (st instanceof AssignmentStatement) {
                        processAssignment((AssignmentStatement) st, t, currentEnv, nextStateValues);
                    }
                }

                List<String> updates = new ArrayList<>();
                // Generate constraints for modified variables
                for (Map.Entry<String, String> e : nextStateValues.entrySet()) {
                    updates.add(String.format("%s_%d == (%s)", e.getKey(), t+1, e.getValue()));
                }

                // Copy unchanged atoms
                for (Map.Entry<String, Map<String, Type>> ve : varFields.entrySet()) {
                    String base = ve.getKey();
                    for (String field : ve.getValue().keySet()) {
                        String atom = field.equals(base) ? base : (base + "_" + field);
                        if (!nextStateValues.containsKey(atom)) {
                            updates.add(String.format("%s_%d == %s_%d", atom, t+1, atom, t));
                        }
                    }
                }

                String updatesConj = String.join(", ", updates);
                String transExpr = String.format("And(%s, %s)", guard, updatesConj.isEmpty() ? "True" : updatesConj);
                
                if (!firstTrans) stepCond.append(", ");
                stepCond.append("\n    ");
                stepCond.append(transExpr);
                firstTrans = false;
            }
            stepCond.append("\n)\n");
            sb.append(String.format("s.add(%s)\n", stepCond.toString()));
            sb.append("\n");
        }
    }

    private void processAssignment(AssignmentStatement as, int t, Map<String, String> currentEnv, Map<String, String> nextStateValues) throws ValidationException {
        Term target = as.getTarget();
        Term expr = as.getExpr();

        if (target == null) {
            termToZ3(expr, t, currentEnv);
            return;
        }

        String rhs = termToZ3(expr, t, currentEnv);

        if (target instanceof IdValue) {
            String var = ((IdValue) target).getIdentifier();
            Map<String, Type> fields = varFields.get(var);

            if (expr instanceof StructTerm && fields != null && fields.size() > 1) {
                StructTerm rhsStruct = (StructTerm) expr;
                for (Map.Entry<String, Term> f : rhsStruct.getFields().entrySet()) {
                    String atom = f.getKey().equals(var) ? var : (var + "_" + f.getKey());
                    String val = termToZ3(f.getValue(), t, currentEnv);
                    currentEnv.put(atom, val);
                    nextStateValues.put(atom, val);
                }
            } else if (fields != null && fields.size() > 1 && expr instanceof IdValue) {
                String rhsId = ((IdValue) expr).getIdentifier();
                for (String fld : fields.keySet()) {
                    String atom = fld.equals(var) ? var : (var + "_" + fld);
                    String rhsAtom = fld.equals(rhsId) ? rhsId : (rhsId + "_" + fld);
                    String val = currentEnv.containsKey(rhsAtom) ? currentEnv.get(rhsAtom) : String.format("%s_%d", rhsAtom, t);
                    currentEnv.put(atom, val);
                    nextStateValues.put(atom, val);
                }
            } else {
                currentEnv.put(var, rhs);
                nextStateValues.put(var, rhs);
            }
        } else if (target instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) target;
            Term owner = ft.getOwner();
            String field = ft.getField();
            if (owner instanceof IdValue) {
                String ownerName = ((IdValue) owner).getIdentifier();
                String atom = field.equals(ownerName) ? ownerName : (ownerName + "_" + field);
                currentEnv.put(atom, rhs);
                nextStateValues.put(atom, rhs);
            } else {
                String leftStr = termToZ3(target, t).replaceAll("_(\\d+)$", "");
                currentEnv.put(leftStr, rhs);
                nextStateValues.put(leftStr, rhs);
            }
        }
        // TODO: Add support for TupleTerm assignment here
    }

    private void generatePropertyVerification(StringBuilder sb, Automaton autom, int k) {
        PropertyCollection pc = autom.getProperties();
        if (pc == null) return;

        Map<String, Property> props = pc.getPropertiesMap();
        if (props == null || props.isEmpty()) return;

        sb.append("# Properties verification\n");
        List<String> violations = new ArrayList<>();

        for (Map.Entry<String, Property> entry : props.entrySet()) {
            String propName = entry.getKey();
            Property prop = entry.getValue();
            PathFormulae pf = prop.getFormulae();
            
            if (pf == null) continue;

            String checkExpr = propertyToCheckExpr((StateFormulae) pf, k);
            if (checkExpr != null) {
                sb.append(String.format("# Property %s violation condition:\n", propName));
                violations.add(checkExpr);
            }
        }

        if (!violations.isEmpty()) {
            sb.append("s.add(Or(\n");
            for (int i = 0; i < violations.size(); i++) {
                sb.append("  " + violations.get(i));
                if (i < violations.size() - 1) sb.append(",\n");
            }
            sb.append("\n))\n");
        }
    }

    private void generateFooter(StringBuilder sb) {
        sb.append("print(s.check())\n");
        sb.append("if s.check() == sat:\n");
        sb.append("    m = s.model()\n");
        sb.append("    print(\"counterexample model:\")\n");
        sb.append("    print(m)\n");
    }

    private Type resolveType(Type t) {
        if (t instanceof IdType) {
            return resolveType(((IdType) t).getReference().getType());
        }
        if (t instanceof InitType) {
            return resolveType(((InitType) t).getBaseType());
        }
        return t;
    }

    private List<TransitionSingle> flattenTransitions(List<Transition> transitions) {
        List<TransitionSingle> result = new ArrayList<>();
        for (Transition t : transitions) {
            if (t instanceof TransitionSingle) {
                result.add((TransitionSingle) t);
            } else if (t instanceof TransitionGroup) {
                result.addAll(flattenTransitions(((TransitionGroup) t).getTransitions()));
            }
        }
        return result;
    }

    private String termToZ3(Term term, int t) throws ValidationException {
        return termToZ3(term, t, null);
    }

    private String termToZ3(Term term, int t, Map<String, String> env) throws ValidationException {
        if (term == null) return "True";

        if (term instanceof IdValue) return handleIdValue((IdValue) term, t, env);
        if (term instanceof IntValue) return String.valueOf(((IntValue) term).getValue());
        if (term instanceof DoubleValue) return String.valueOf(((DoubleValue) term).getValue());
        if (term instanceof BoolValue) return ((BoolValue) term).getValue() ? "True" : "False";
        if (term instanceof NullValue) return String.valueOf(-1);
        if (term instanceof EnumValue) return handleEnumValue((EnumValue) term);
        if (term instanceof FieldTerm) return handleFieldTerm((FieldTerm) term, t, env);
        if (term instanceof StructTerm) return handleStructTerm((StructTerm) term, t, env);
        if (term instanceof IteTerm) return handleIteTerm((IteTerm) term, t, env);
        if (term instanceof BinaryOperatorTerm) return handleBinaryOperator((BinaryOperatorTerm) term, t, env);
        if (term instanceof SingleOperatorTerm) return handleSingleOperator((SingleOperatorTerm) term, t, env);
        if (term instanceof CallTerm) return handleCallTerm((CallTerm) term, t, env);

        throw ValidationException.UnderDevelopment();
    }

    private String handleIdValue(IdValue id, int t, Map<String, String> env) {
        String name = id.getIdentifier();
        if ("null".equals(name)) return String.valueOf(-1);
        if (env != null && env.containsKey(name)) return env.get(name);
        if (globalEnumAliasMap.containsKey(name)) return globalEnumAliasMap.get(name);
        return String.format("%s_%d", name, t);
    }

    private String handleEnumValue(EnumValue ev) {
        org.fmgroup.mediator.language.type.termType.EnumType ref = ev.getReference();
        if (ref != null && enumItemConstMap.containsKey(ref)) {
            Map<String, String> m = enumItemConstMap.get(ref);
            if (m.containsKey(ev.getIdentifier())) return m.get(ev.getIdentifier());
        }
        if (globalEnumAliasMap.containsKey(ev.getIdentifier())) return globalEnumAliasMap.get(ev.getIdentifier());
        return String.format("\"%s\"", ev.getIdentifier());
    }

    private String handleFieldTerm(FieldTerm ft, int t, Map<String, String> env) throws ValidationException {
        Term owner = ft.getOwner();
        String field = ft.getField();
        String atom;
        if (owner instanceof IdValue) {
            String ownerName = ((IdValue) owner).getIdentifier();
            atom = field.equals(ownerName) ? ownerName : (ownerName + "_" + field);
        } else {
            String ownerStr = termToZ3(owner, t, env);
            ownerStr = ownerStr.replaceAll("_(\\d+)$", "");
            atom = String.format("%s_%s", ownerStr, field);
        }
        
        if (env != null && env.containsKey(atom)) return env.get(atom);
        return String.format("%s_%d", atom, t);
    }

    private String handleStructTerm(StructTerm st, int t, Map<String, String> env) throws ValidationException {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        boolean first = true;
        for (java.util.Map.Entry<String, Term> e : st.getFields().entrySet()) {
            if (!first) sb.append(", ");
            sb.append(String.format("\"%s\": %s", e.getKey(), termToZ3(e.getValue(), t, env)));
            first = false;
        }
        sb.append("}");
        return sb.toString();
    }

    private String handleIteTerm(IteTerm it, int t, Map<String, String> env) throws ValidationException {
        String c = termToZ3(it.getCondition(), t, env);
        String th = termToZ3(it.getThenTerm(), t, env);
        String el = termToZ3(it.getElseTerm(), t, env);
        return String.format("If(%s, %s, %s)", c, th, el);
    }

    private String handleBinaryOperator(BinaryOperatorTerm bt, int t, Map<String, String> env) throws ValidationException {
        String l = termToZ3(bt.getLeft(), t, env);
        String r = termToZ3(bt.getRight(), t, env);
        EnumBinaryOperator opr = bt.getOpr();
        switch (opr) {
            case LAND: return String.format("And(%s, %s)", l, r);
            case LOR: return String.format("Or(%s, %s)", l, r);
            case EQ: return String.format("(%s) == (%s)", l, r);
            case NEQ: return String.format("Not((%s) == (%s))", l, r);
            case LT: return String.format("(%s < %s)", l, r);
            case LEQ: return String.format("(%s <= %s)", l, r);
            case GT: return String.format("(%s > %s)", l, r);
            case GEQ: return String.format("(%s >= %s)", l, r);
            case ADD: return String.format("(%s + %s)", l, r);
            case MINUS: return String.format("(%s - %s)", l, r);
            case TIMES: return String.format("(%s * %s)", l, r);
            case DIV: return String.format("(to_real(%s) / to_real(%s))", l, r);
            case MOD: return String.format("(%s %% %s)", l, r);
            default: return "True";
        }
    }

    private String handleSingleOperator(SingleOperatorTerm st, int t, Map<String, String> env) throws ValidationException {
        EnumSingleOperator opr = st.getOpr();
        String inner = termToZ3(st.getTerm(), t, env);
        if (opr == EnumSingleOperator.LNOT) return String.format("Not(%s)", inner);
        if (opr == EnumSingleOperator.NEGATIVE) return String.format("-(%s)", inner);
        return inner;
    }

    private String handleCallTerm(CallTerm ct, int t, Map<String, String> env) throws ValidationException {
        String funcName = ct.getCallee().getIdentifier();
        
        if ("abs".equals(funcName)) {
            if (ct.getArgs().size() > 0) {
                String arg = termToZ3(ct.getArgs().get(0), t, env);
                return String.format("If(%s >= 0, %s, -%s)", arg, arg, arg);
            }
        }
        
        // Placeholder for future function support
        return "0"; 
    }

    private String propertyToCheckExpr(StateFormulae formula, int k) {
        if (formula instanceof GloballyStateFormulae) {
            StateFormulae inner = ((GloballyStateFormulae) formula).getFormula();
            StringBuilder sb = new StringBuilder();
            sb.append("Or(");
            for (int t = 0; t <= k; t++) {
                try {
                    if (inner instanceof AtomicPathFormulae) {
                        Term term = ((AtomicPathFormulae) inner).getTerm();
                        String termZ3 = termToZ3(term, t);
                        sb.append(String.format("Not(%s)", termZ3));
                    } else {
                        return "False";
                    }
                } catch (ValidationException e) {
                    return "False";
                }
                if (t < k) sb.append(", ");
            }
            sb.append(")");
            return sb.toString();
        } else if (formula instanceof AtomicPathFormulae) {
            Term term = ((AtomicPathFormulae) formula).getTerm();
            StringBuilder sb = new StringBuilder();
            sb.append("Or(");
            for (int t = 0; t <= k; t++) {
                try {
                    String termZ3 = termToZ3(term, t);
                    sb.append(String.format("Not(%s)", termZ3));
                } catch (ValidationException e) {
                    return "False";
                }
                if (t < k) sb.append(", ");
            }
            sb.append(")");
            return sb.toString();
        }
        return null;
    }
}

