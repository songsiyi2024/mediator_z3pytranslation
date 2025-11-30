package org.fmgroup.mediator.plugins.generators.z3;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.LinkedHashMap;
import java.util.HashMap;
import java.lang.reflect.Field;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
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
import org.fmgroup.mediator.language.term.FieldTerm;
import org.fmgroup.mediator.language.term.IteTerm;
import org.fmgroup.mediator.language.term.StructTerm;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.language.term.DoubleValue;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.termType.StructType;
import org.fmgroup.mediator.language.type.termType.EnumType;
import org.fmgroup.mediator.language.type.termType.UnionType;
import org.fmgroup.mediator.language.type.termType.BoolType;
import org.fmgroup.mediator.language.type.termType.IntType;
import org.fmgroup.mediator.language.type.termType.DoubleType;
import org.fmgroup.mediator.language.type.termType.BoundedIntType;
import org.fmgroup.mediator.language.type.termType.InitType;
import org.fmgroup.mediator.language.type.termType.InitType;
import org.fmgroup.mediator.language.type.termType.IdType;
import org.fmgroup.mediator.language.entity.system.System;
import org.fmgroup.mediator.plugins.scheduler.Scheduler;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugin.generator.Generator;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoGeneratorException;
import org.fmgroup.mediator.language.entity.system.ComponentDeclaration;
import org.fmgroup.mediator.language.entity.PortDeclaration;
import org.fmgroup.mediator.language.term.PortVariableType;
import org.fmgroup.mediator.language.term.PortVariableValue;
import org.fmgroup.mediator.language.entity.PortIdentifier;
import org.fmgroup.mediator.language.Templated;

/**
 * A simple Z3 generator that emits a Z3 Python script performing bounded-safety check (k steps).
 * Minimal support: Automaton, integer and boolean local variables, simple guards and assignments.
 */
public class Z3Generator implements Generator {

    private int k = 20;

    public void setBound(int k) {
        this.k = k;
    }

    // enum mapping used during generation: EnumType -> (item -> constName)
    private Map<org.fmgroup.mediator.language.type.termType.EnumType, Map<String, String>> enumItemConstMap = new HashMap<>();
    // global reverse mapping: item name -> constName (to resolve IdValue that are actually enum constants)
    private Map<String, String> globalEnumAliasMap = new HashMap<>();
    private int enumGlobalCounter = 0;

    @Override
    public FileSet generate(RawElement elem) throws ArduinoGeneratorException {
        try {
            Automaton autom;
            if (elem instanceof System) {
                autom = Scheduler.Schedule((System) elem);
                // Fix: Scheduler drops properties, so we manually collect them from sub-components
                collectProperties((System) elem, autom, "");
            } else if (elem instanceof Automaton) {
                autom = (Automaton) elem;
            } else {
                throw new ArduinoGeneratorException("Z3Generator supports Automaton or System elements");
            }
            
            String name = autom.getName();
            String py = renderZ3Script(autom, this.k);
            FileSet fs = new FileSet();
            fs.add(name + "_z3_check.py", py);

            // Output flattened automaton
            // We add it to the FileSet with a relative path prefix.
            // The consumer (ParseExample) will write it relative to its output root.
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

    private Type resolveType(Type t) {
        if (t instanceof IdType) {
            return resolveType(((IdType) t).getReference().getType());
        }
        if (t instanceof InitType) {
            return resolveType(((InitType) t).getBaseType());
        }
        return t;
    }

    private String renderZ3Script(Automaton autom, int k) throws ValidationException {
        StringBuilder sb = new StringBuilder();
        sb.append("from z3 import *\n\n");
        sb.append("def to_real(x):\n");
        sb.append("    if isinstance(x, int):\n");
        sb.append("        return RealVal(x)\n");
        sb.append("    if isinstance(x, float):\n");
        sb.append("        return RealVal(x)\n");
        sb.append("    if is_int(x):\n");
        sb.append("        return ToReal(x)\n");
        sb.append("    return x\n\n");

        // --- Prepare flattened variable declarations (support struct, enum, union tag+payload) ---
        VariableDeclarationCollection vars = autom.getLocalVars();

        // map base variable -> map(fieldName -> fieldType)
        Map<String, Map<String, Type>> varFields = new LinkedHashMap<>();

        // enum type mapping: EnumType -> (itemName -> constName)
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
                    // create enum constant names for this enum type if not exist
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
                    // treat enum variable as single int field named id
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id, resolved);
                    varFields.put(id, fields);
                } else if (resolved instanceof UnionType) {
                    // tag + payload (payload as Int by default)
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id + "_tag", null);
                    fields.put(id + "_val", null);
                    varFields.put(id, fields);
                } else {
                    // primitive or other: single field named id
                    Map<String, Type> fields = new LinkedHashMap<>();
                    fields.put(id, resolved);
                    varFields.put(id, fields);
                }
            }
        }

        // emit enum constant definitions
        for (Map.Entry<EnumType, Map<String, String>> e : enumItemConstMap.entrySet()) {
            int idx = 0;
            for (Map.Entry<String, String> it : e.getValue().entrySet()) {
                sb.append(String.format("%s = %d\n", it.getValue(), idx));
                idx++;
            }
            sb.append("\n");
        }

        // declare per-step flattened variables
        for (int t = 0; t <= k; t++) {
            for (Map.Entry<String, Map<String, Type>> e : varFields.entrySet()) {
                String base = e.getKey();
                for (String field : e.getValue().keySet()) {
                    String atomName = field.equals(base) ? base : (base + "_" + field);
                    Type ftype = e.getValue().get(field);
                    if (t == 0) {
                         java.lang.System.out.println("DEBUG: Variable " + atomName + " type is " + ftype.getClass().getName());
                    }
                    // choose Bool or Int or Real by type
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

        // initial constraints: use init values from variable declarations when available
        sb.append("s = Solver()\n");
        for (VariableDeclaration vd : vars.getDeclarationList()) {
            for (String id : vd.getIdentifiers()) {
                Term init = null;
                try {
                    init = vd.getType().getInitValue();
                } catch (ValidationException e) {
                    // ignore, type not initialized or does not support initialization
                }
                
                java.lang.System.out.println("DEBUG: Variable " + id + " init is " + (init==null?"null":init.toString()));

                // If no explicit init, provide default for primitive types to avoid unconstrained variables
                if (init == null) {
                    Type t = resolveType(vd.getType());
                    if (t instanceof IntType) {
                        init = new IntValue().setValue(0);
                    } else if (t instanceof BoundedIntType) {
                        init = ((BoundedIntType) t).getLowerBound();
                    } else if (t instanceof DoubleType) {
                        init = new DoubleValue().setValue(0.0);
                    } else if (t instanceof BoolType) {
                        init = new BoolValue().setValue(false);
                    }
                }

                if (init != null) {
                    // if struct init, expand to field inits
                    if (init instanceof StructTerm) {
                        StructTerm st = (StructTerm) init;
                        for (Map.Entry<String, Term> e : st.getFields().entrySet()) {
                            String atom = e.getKey().equals(id) ? id : (id + "_" + e.getKey());
                            String expr0 = termToZ3(e.getValue(), 0);
                            sb.append(String.format("s.add(%s_0 == %s)\n", atom, expr0));
                        }
                    } else {
                        String expr0 = termToZ3(init, 0);
                        // if enum initial: init may refer to enum literal; termToZ3 will return const name
                        sb.append(String.format("s.add(%s_0 == %s)\n", id, expr0));
                    }
                }
            }
        }
        sb.append("\n");

        // encode transitions as per-step constraints: build disjunction of possible transitions
        List<TransitionSingle> transitions = flattenTransitions(autom.getTransitions());
        for (int t = 0; t < k; t++) {
            StringBuilder stepCond = new StringBuilder();
            stepCond.append("Or(");
            boolean firstTrans = true;
            for (TransitionSingle ts : transitions) {
                String guard = termToZ3(ts.getGuard(), t);

                List<Statement> stmts = ts.getStatements();
                
                // Track imperative updates within the transition
                Map<String, String> currentEnv = new HashMap<>();
                // Track final values for next state
                Map<String, String> nextStateValues = new HashMap<>();

                for (Statement st : stmts) {
                    if (!(st instanceof AssignmentStatement)) continue;
                    AssignmentStatement as = (AssignmentStatement) st;
                    Term target = as.getTarget();
                    Term expr = as.getExpr();

                    // Evaluate RHS using current environment (imperative)
                    String rhs = termToZ3(expr, t, currentEnv);

                    // target is a plain identifier (variable)
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
                            // copy struct from another variable
                            String rhsId = ((IdValue) expr).getIdentifier();
                            for (String fld : fields.keySet()) {
                                String atom = fld.equals(var) ? var : (var + "_" + fld);
                                String rhsAtom = fld.equals(rhsId) ? rhsId : (rhsId + "_" + fld);
                                // resolve rhsAtom in currentEnv if possible
                                String val = currentEnv.containsKey(rhsAtom) ? currentEnv.get(rhsAtom) : String.format("%s_%d", rhsAtom, t);
                                currentEnv.put(atom, val);
                                nextStateValues.put(atom, val);
                            }
                        } else {
                            // atomic assignment
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
                }

                List<String> updates = new ArrayList<>();
                // Generate constraints for modified variables
                for (Map.Entry<String, String> e : nextStateValues.entrySet()) {
                    updates.add(String.format("%s_%d == (%s)", e.getKey(), t+1, e.getValue()));
                }

                // default: copy unchanged atoms
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
                stepCond.append("\n    "); // Add newline and indent
                stepCond.append(transExpr);
                firstTrans = false;
            }
            stepCond.append("\n)\n");
            sb.append(String.format("s.add(%s)\n", stepCond.toString()));
            sb.append("\n");
        }

        // Generate property verification constraints
        generateProperties(autom, sb, k);

        sb.append("print(s.check())\n");
    sb.append("if s.check() == sat:\n");
    sb.append("    m = s.model()\n");
    sb.append("    print(\"counterexample model:\")\n");
    sb.append("    print(m)\n");
        return sb.toString();
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
        if (term == null) {
            // unknown term -> produce a boolean false by default to avoid producing integer 0 in guards
            // If it is a guard (missing guard), it implies True.
            return "True";
        }

        // Identifier (variable or enum constant)
        if (term instanceof IdValue) {
            IdValue id = (IdValue) term;
            String name = id.getIdentifier();
            if ("null".equals(name)) {
                // use -1 as a NULL sentinel for integer/optional fields
                return String.valueOf(-1);
            }
            
            // Check local environment (imperative updates)
            if (env != null && env.containsKey(name)) {
                return env.get(name);
            }

            // check if it is an enum constant
            if (globalEnumAliasMap.containsKey(name)) {
                return globalEnumAliasMap.get(name);
            }
            
            return String.format("%s_%d", name, t);
        }

        // Integer literal
        if (term instanceof IntValue) {
            IntValue iv = (IntValue) term;
            return String.valueOf(iv.getValue());
        }

        // Double literal
        if (term instanceof DoubleValue) {
            DoubleValue dv = (DoubleValue) term;
            return String.valueOf(dv.getValue());
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
            org.fmgroup.mediator.language.type.termType.EnumType ref = ev.getReference();
            if (ref != null && enumItemConstMap.containsKey(ref)) {
                Map<String, String> m = enumItemConstMap.get(ref);
                if (m.containsKey(ev.getIdentifier())) {
                    return m.get(ev.getIdentifier());
                }
            }
            // fallback: check global alias map
            if (globalEnumAliasMap.containsKey(ev.getIdentifier())) {
                return globalEnumAliasMap.get(ev.getIdentifier());
            }
            // fallback: quoted name
            return String.format("\"%s\"", ev.getIdentifier());
        }

        // Field access: <owner>.<field> -> translate to flattened name owner_field_t
        if (term instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) term;
            Term owner = ft.getOwner();
            String field = ft.getField();
            String atom;
            if (owner instanceof IdValue) {
                String ownerName = ((IdValue) owner).getIdentifier();
                atom = field.equals(ownerName) ? ownerName : (ownerName + "_" + field);
            } else {
                // fallback: try to render owner and append field (may contain a time suffix)
                String ownerStr = termToZ3(owner, t, env);
                // strip trailing _<t> if present
                ownerStr = ownerStr.replaceAll("_(\\d+)$", "");
                atom = String.format("%s_%s", ownerStr, field);
            }
            
            if (env != null && env.containsKey(atom)) {
                return env.get(atom);
            }
            return String.format("%s_%d", atom, t);
        }

        // Struct literal: produce a Python dict of field->expr (caller must handle assignment expansion)
        if (term instanceof StructTerm) {
            StructTerm st = (StructTerm) term;
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

        // ITE (cond ? then : else)
        if (term instanceof IteTerm) {
            IteTerm it = (IteTerm) term;
            String c = termToZ3(it.getCondition(), t, env);
            String th = termToZ3(it.getThenTerm(), t, env);
            String el = termToZ3(it.getElseTerm(), t, env);
            return String.format("If(%s, %s, %s)", c, th, el);
        }

        // Binary operator (logical, comparison, arithmetic)
        if (term instanceof BinaryOperatorTerm) {
            BinaryOperatorTerm bt = (BinaryOperatorTerm) term;
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
            }
        }

        // Unary operator (logical not)
        if (term instanceof SingleOperatorTerm) {
            SingleOperatorTerm st = (SingleOperatorTerm) term;
            EnumSingleOperator opr = st.getOpr();
            String inner = termToZ3(st.getTerm(), t, env);
            if (opr == EnumSingleOperator.LNOT) return String.format("Not(%s)", inner);
            if (opr == EnumSingleOperator.NEGATIVE) return String.format("-(%s)", inner);
        }

        // fallback: unsupported term -> raise explicit error so user knows to extend generator
        throw ValidationException.UnderDevelopment();
    }

    private void generateProperties(Automaton autom, StringBuilder sb, int k) {
        PropertyCollection pc = autom.getProperties();
        if (pc == null) return;

        Map<String, Property> props = getPropertiesMap(pc);
        if (props == null || props.isEmpty()) {
            return;
        }

        sb.append("# Properties verification\n");
        // We want to check if ANY property is violated.
        // Violation of G(P) is Exists t: Not(P)
        
        List<String> violations = new ArrayList<>();

        for (Map.Entry<String, Property> entry : props.entrySet()) {
            String propName = entry.getKey();
            Property prop = entry.getValue();
            PathFormulae pf = getPathFormulae(prop);
            
            if (pf == null) {
                continue;
            }

            String checkExpr = propertyToCheckExpr((StateFormulae) pf, k);
            if (checkExpr != null) {
                sb.append(String.format("# Property %s violation condition:\n", propName));
                // sb.append(String.format("prop_%s_violation = %s\n", propName, checkExpr));
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

    private void collectProperties(System sys, Automaton target, String prefix) throws ValidationException {
        if (sys.getComponentCollection() == null) return;
        
        for (ComponentDeclaration cd : sys.getComponentCollection().getDeclarationList()) {
            for (String instanceName : cd.getIdentifiers()) {
                String newPrefix = prefix.isEmpty() ? instanceName : prefix + "_" + instanceName;
                Templated type = cd.getType().getProviderWithNoTemplate();
                
                if (type instanceof Automaton) {
                    Automaton autom = (Automaton) type;
                    addPropertiesFromAutomaton(autom, target, newPrefix);
                } else if (type instanceof System) {
                    collectProperties((System) type, target, newPrefix);
                }
            }
        }
    }

    private void addPropertiesFromAutomaton(Automaton source, Automaton target, String prefix) throws ValidationException {
        try {
        PropertyCollection pc = source.getProperties();
        if (pc == null) return;

        Map<String, Term> termRewriteMap = new HashMap<>();
        
        // 1. Local variables
        if (source.getLocalVars() != null) {
            for (VariableDeclaration vd : source.getLocalVars().getDeclarationList()) {
                for (String id : vd.getIdentifiers()) {
                    String newId = prefix + "_" + id;
                    termRewriteMap.put(id, new IdValue().setParent(target).setIdentifier(newId));
                }
            }
        }
        
        // 2. Ports
        if (source.getEntityInterface() != null) {
            for (PortDeclaration pd : source.getEntityInterface().getDeclarationList()) {
                for (String id : pd.getIdentifiers()) {
                    // PortVariableType.VALUE -> "value"
                    termRewriteMap.put(id + ".value", new IdValue().setParent(target).setIdentifier(prefix + "_" + id + "_value"));
                    termRewriteMap.put(id + ".reqRead", new IdValue().setParent(target).setIdentifier(prefix + "_" + id + "_reqRead"));
                    termRewriteMap.put(id + ".reqWrite", new IdValue().setParent(target).setIdentifier(prefix + "_" + id + "_reqWrite"));
                }
            }
        }
        
        Map<String, Property> props = getPropertiesMap(pc);
        if (props == null) return;

        for (Map.Entry<String, Property> entry : props.entrySet()) {
             String propName = entry.getKey();
             Property p = entry.getValue();
             
             PathFormulae pf = p.getFormulae();
             if (pf instanceof AtomicPathFormulae) {
                 Term t = ((AtomicPathFormulae) pf).getTerm();
                 
                 // We DO NOT clone the term here because copy(null) crashes on PortVariableValue.
                 // rewriteTerm will create a copy with replacements.
                 
                 Term newT = rewriteTerm(t, termRewriteMap, target);
                 
                 Property newP = new Property();
                 AtomicPathFormulae newPf = new AtomicPathFormulae();
                 newPf.setTerm(newT);
                 newP.setFormulae(newPf);
                 
                 if (target.getProperties() == null) {
                     target.setProperties(new PropertyCollection());
                 }
                 
                 String newPropName = prefix + "_" + propName;
                 target.getProperties().putProperty(newPropName, newP);
             }
        }
        } catch (Exception e) {
            e.printStackTrace();
            if (e instanceof ValidationException) throw (ValidationException) e;
            throw new RuntimeException(e);
        }
    }

    private Term rewriteTerm(Term t, Map<String, Term> map, RawElement parent) throws ValidationException {
        if (t == null) return null;

        if (t instanceof PortVariableValue) {
            PortVariableValue pvv = (PortVariableValue) t;
            String portName = pvv.getPortIdentifier().getPortName();
            String type = pvv.getPortVariableType().toString();
            
            String key = portName + "." + type;
            if (map.containsKey(key)) {
                return map.get(key).copy(parent);
            }
            return t.copy(parent);
        }

        if (t instanceof IdValue) {
            String id = ((IdValue) t).getIdentifier();
            if (map.containsKey(id)) {
                return map.get(id).copy(parent);
            }
            return t.copy(parent);
        }

        if (t instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) t;
            String field = ft.getField();
            Term owner = ft.getOwner();
            
            if (owner instanceof IdValue) {
                String ownerId = ((IdValue) owner).getIdentifier();
                String key = ownerId + "." + field;
                if (map.containsKey(key)) {
                    return map.get(key).copy(parent);
                }
            }
            
            FieldTerm newFt = new FieldTerm();
            newFt.setParent(parent);
            newFt.setField(field);
            newFt.setOwner(rewriteTerm(owner, map, newFt));
            return newFt;
        }

        if (t instanceof BinaryOperatorTerm) {
            BinaryOperatorTerm bt = (BinaryOperatorTerm) t;
            BinaryOperatorTerm newBt = new BinaryOperatorTerm();
            newBt.setParent(parent);
            newBt.setOpr(bt.getOpr());
            newBt.setLeft(rewriteTerm(bt.getLeft(), map, newBt));
            newBt.setRight(rewriteTerm(bt.getRight(), map, newBt));
            return newBt;
        }

        if (t instanceof SingleOperatorTerm) {
            SingleOperatorTerm st = (SingleOperatorTerm) t;
            SingleOperatorTerm newSt = new SingleOperatorTerm();
            newSt.setParent(parent);
            newSt.setOpr(st.getOpr());
            newSt.setTerm(rewriteTerm(st.getTerm(), map, newSt));
            return newSt;
        }
        
        if (t instanceof IteTerm) {
            IteTerm it = (IteTerm) t;
            IteTerm newIt = new IteTerm();
            newIt.setParent(parent);
            newIt.setCondition(rewriteTerm(it.getCondition(), map, newIt));
            newIt.setThenTerm(rewriteTerm(it.getThenTerm(), map, newIt));
            newIt.setElseTerm(rewriteTerm(it.getElseTerm(), map, newIt));
            return newIt;
        }

        return t.copy(parent);
    }


    @SuppressWarnings("unchecked")
    private Map<String, Property> getPropertiesMap(PropertyCollection pc) {
        try {
            Field f = PropertyCollection.class.getDeclaredField("properties");
            f.setAccessible(true);
            return (Map<String, Property>) f.get(pc);
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

    private PathFormulae getPathFormulae(Property prop) {
        try {
            Field f = Property.class.getDeclaredField("formulae");
            f.setAccessible(true);
            return (PathFormulae) f.get(prop);
        } catch (Exception e) {
            // e.printStackTrace();
            return null;
        }
    }

    private String propertyToCheckExpr(StateFormulae formula, int k) {
        // Returns the Z3 expression that is True if the property is VIOLATED.
        
        if (formula instanceof GloballyStateFormulae) {
            // G(phi) violated if Exists t: Not(phi)
            StateFormulae inner = ((GloballyStateFormulae) formula).getFormula();
            StringBuilder sb = new StringBuilder();
            sb.append("Or(");
            for (int t = 0; t <= k; t++) {
                try {
                    // We need Not(phi) at time t
                    // If inner is Atomic, we can use termToZ3
                    if (inner instanceof AtomicPathFormulae) {
                        Term term = ((AtomicPathFormulae) inner).getTerm();
                        String termZ3 = termToZ3(term, t);
                        sb.append(String.format("Not(%s)", termZ3));
                    } else {
                        // Nested temporal operators not supported yet
                        return "False"; // Ignore
                    }
                } catch (ValidationException e) {
                    return "False";
                }
                if (t < k) sb.append(", ");
            }
            sb.append(")");
            return sb.toString();
        } else if (formula instanceof AtomicPathFormulae) {
            // Atomic P. Treated as Invariant G(P).
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

