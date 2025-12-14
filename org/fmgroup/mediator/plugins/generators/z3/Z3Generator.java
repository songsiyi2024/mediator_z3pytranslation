package org.fmgroup.mediator.plugins.generators.z3;

import org.fmgroup.mediator.language.function.Function;
import org.fmgroup.mediator.language.statement.ReturnStatement;
import org.fmgroup.mediator.language.Program;
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
import org.fmgroup.mediator.language.property.PathFormulae.AllPathFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.ExistsPathFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.GloballyStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.FinallyStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.NextStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.UntilStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;
import org.fmgroup.mediator.language.property.BinaryOperatorFormulae;
import org.fmgroup.mediator.language.property.NotFormulae;
import org.fmgroup.mediator.language.property.Formulae;
import org.fmgroup.mediator.language.property.EnumBinaryOperatorTemporal;
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
import org.fmgroup.mediator.language.term.TupleTerm;
import org.fmgroup.mediator.language.term.ListTerm;
import org.fmgroup.mediator.language.term.ElementTerm;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.language.term.DoubleValue;
import org.fmgroup.mediator.language.term.CallTerm;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.termType.StructType;
import org.fmgroup.mediator.language.type.termType.TupleType;
import org.fmgroup.mediator.language.type.termType.ListType;
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
    private Map<String, Type> varTypes = new HashMap<>();

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
            e.printStackTrace();
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
        generateFunctions(sb, autom);
        generateVariableDeclarations(sb, k);
        generateInitConstraints(sb, autom);
        generateTransitionConstraints(sb, autom, k);
        generatePropertyVerification(sb, autom, k);
        generateTypeSafetyVerification(sb, k);
        generateFooter(sb);

        return sb.toString();
    }

    private void generateTypeSafetyVerification(StringBuilder sb, int k) throws ValidationException {
        List<String> typeViolations = new ArrayList<>();
        for (int t = 0; t <= k; t++) {
            for (Map.Entry<String, Map<String, Type>> e : varFields.entrySet()) {
                String base = e.getKey();
                for (Map.Entry<String, Type> fe : e.getValue().entrySet()) {
                    String path = fe.getKey();
                    Type type = fe.getValue();
                    String atomName = path.isEmpty() ? base : (base + "_" + path);
                    String varExpr = String.format("%s_%d", atomName, t);
                    
                    Type resolved = resolveType(type);
                    if (resolved instanceof BoundedIntType) {
                        BoundedIntType bit = (BoundedIntType) resolved;
                        Term lower = bit.getLowerBound();
                        Term upper = bit.getUpperBound();
                        
                        try {
                            String lowerStr = termToZ3(lower, t);
                            String upperStr = termToZ3(upper, t);
                            
                            // Violation: var < lower OR var > upper
                            String violation = String.format("Or(%s < %s, %s > %s)", varExpr, lowerStr, varExpr, upperStr);
                            typeViolations.add(violation);
                        } catch (ValidationException ex) {
                            // Ignore if bounds cannot be evaluated
                        }
                    }
                }
            }
        }

        if (!typeViolations.isEmpty()) {
            sb.append("\n# ===============================================================================\n");
            sb.append("# Implicit type safety verification (bounded integers)\n");
            sb.append("# To check for integer overflows/underflows, uncomment the following block.\n");
            sb.append("# NOTE: This checks if ANY variable violates its bounds. If 'sat', a violation exists.\n");
            sb.append("# You may want to comment out other property checks to isolate this verification.\n");
            sb.append("# ===============================================================================\n");
            sb.append("# s.add(Or(\n");
            for (int i = 0; i < typeViolations.size(); i++) {
                sb.append("#   " + typeViolations.get(i));
                if (i < typeViolations.size() - 1) sb.append(",\n");
            }
            sb.append("\n# ))\n");
        }
    }

    private boolean isPrimitiveType(Type t) {
        Type resolved = resolveType(t);
        return resolved instanceof IntType || 
               resolved instanceof DoubleType || 
               resolved instanceof BoolType || 
               resolved instanceof EnumType ||
               resolved instanceof BoundedIntType;
    }

    private void generateFunctions(StringBuilder sb, Automaton autom) throws ValidationException {
        Program prog = RawElement.getRoot(autom);
        if (prog == null) return;
        
        Map<String, Function> funcs = prog.getFunctions();
        if (funcs == null || funcs.isEmpty()) return;
        
        sb.append("# Custom Functions\n");
        for (Function f : funcs.values()) {
            String name = f.getName();
            List<String> argVars = new ArrayList<>();
            Map<String, String> env = new HashMap<>();
            
            // Check arguments
            for (VariableDeclaration arg : f.getFuncInterface().getArgs()) {
                if (!isPrimitiveType(arg.getType())) {
                    throw new ValidationException(null, "Z3Generator: Complex types in functions are not supported yet. Argument: " + arg.getIdentifiers());
                }
                for (String id : arg.getIdentifiers()) {
                    varTypes.put(id, arg.getType());
                    argVars.add(id);
                    env.put(id, id);
                }
            }

            // Check return type
            if (f.getReturnType() != null && !isPrimitiveType(f.getReturnType())) {
                throw new ValidationException(null, "Z3Generator: Complex return types in functions are not supported yet. Function: " + name);
            }
            
            sb.append(String.format("def %s(%s):\n", name, String.join(", ", argVars)));
            
            // Local variables
            if (f.getVariables() != null) {
                for (VariableDeclaration vd : f.getVariables().getDeclarationList()) {
                    if (!isPrimitiveType(vd.getType())) {
                        throw new ValidationException(null, "Z3Generator: Complex local variables in functions are not supported yet. Variable: " + vd.getIdentifiers());
                    }
                    for (String id : vd.getIdentifiers()) {
                        varTypes.put(id, vd.getType());
                        Term init = createDefaultInit(vd.getType());
                        String initVal = termToZ3(init, 0); 
                        sb.append(String.format("    %s = %s\n", id, initVal));
                        env.put(id, id);
                    }
                }
            }
            
            // Statements
            for (Statement st : f.getStatements()) {
                if (st instanceof AssignmentStatement) {
                    processFunctionAssignment(sb, (AssignmentStatement) st, env);
                } else if (st instanceof ReturnStatement) {
                    ReturnStatement rs = (ReturnStatement) st;
                    Term retTerm = rs.getReturnedValue();
                    String retVal = termToZ3(retTerm, 0, env);
                    sb.append(String.format("    return %s\n", retVal));
                }
            }
            sb.append("\n");
        }
    }

    private void processFunctionAssignment(StringBuilder sb, AssignmentStatement as, Map<String, String> env) throws ValidationException {
        Term target = as.getTarget();
        Term expr = as.getExpr();
        
        if (target == null) {
            termToZ3(expr, 0, env);
            return;
        }
        
        String targetName = resolveAtomName(target);
        String valExpr = termToZ3(expr, 0, env);
        sb.append(String.format("    %s = %s\n", targetName, valExpr));
        env.put(targetName, targetName);
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

    private int getMatchingVariantIndex(UnionType ut, Term term) {
        List<Type> baseTypes = ut.getBaseTypes();
        for (int i = 0; i < baseTypes.size(); i++) {
            Type t = resolveType(baseTypes.get(i));
            if (isTypeCompatible(t, term)) {
                return i;
            }
        }
        return -1; // Return -1 if no match found
    }

    private int getMatchingVariantIndex(UnionType ut, Type targetType) {
        List<Type> baseTypes = ut.getBaseTypes();
        Type resolvedTarget = resolveType(targetType);
        for (int i = 0; i < baseTypes.size(); i++) {
            Type t = resolveType(baseTypes.get(i));
            // Simple type equality check for now. 
            // In a real system, we should check isSubtypeOf or similar.
            if (t.getClass().equals(resolvedTarget.getClass())) {
                return i;
            }
        }
        return -1;
    }

    private boolean isTypeCompatible(Type type, Term term) {
        if (type instanceof IntType || type instanceof BoundedIntType) {
            return term instanceof IntValue;
        }
        if (type instanceof DoubleType) {
            return term instanceof DoubleValue; // Or IntValue if implicit conversion allowed?
        }
        if (type instanceof BoolType) {
            return term instanceof BoolValue;
        }
        // Add more checks as needed
        return false;
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
                varTypes.put(id, vt);
                Map<String, Type> fields = new LinkedHashMap<>();
                try {
                    collectLeafFields("", vt, fields);
                    varFields.put(id, fields);
                } catch (ValidationException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    private void collectLeafFields(String prefix, Type type, Map<String, Type> collector) throws ValidationException {
        Type resolved = resolveType(type);
        
        if (resolved instanceof StructType) {
            StructType st = (StructType) resolved;
            for (Map.Entry<String, Type> e : st.getFields().entrySet()) {
                String newPrefix = prefix.isEmpty() ? e.getKey() : prefix + "_" + e.getKey();
                collectLeafFields(newPrefix, e.getValue(), collector);
            }
        } else if (resolved instanceof TupleType) {
            TupleType tt = (TupleType) resolved;
            int idx = 0;
            for (Type subT : tt.getBaseTypes()) {
                String newPrefix = prefix.isEmpty() ? String.valueOf(idx) : prefix + "_" + idx;
                collectLeafFields(newPrefix, subT, collector);
                idx++;
            }
        } else if (resolved instanceof ListType) {
            ListType lt = (ListType) resolved;
            Term capacity = lt.getCapacity();
            if (capacity instanceof IntValue) {
                int len = ((IntValue) capacity).getValue();
                Type baseType = lt.getBaseType();
                for (int i = 0; i < len; i++) {
                    String newPrefix = prefix.isEmpty() ? String.valueOf(i) : prefix + "_" + i;
                    collectLeafFields(newPrefix, baseType, collector);
                }
            } else {
                throw ValidationException.UnderDevelopment();
            }
        } else if (resolved instanceof EnumType) {
            EnumType et = (EnumType) resolved;
            if (!enumItemConstMap.containsKey(et)) {
                Map<String, String> itemMap = new LinkedHashMap<>();
                String enumPrefix = String.format("ENUM_%d", enumGlobalCounter++);
                int idx = 0;
                for (String item : et.getItems()) {
                    String constName = String.format("%s_%s", enumPrefix, item.replaceAll("[^A-Za-z0-9_]", "_"));
                    itemMap.put(item, constName);
                    globalEnumAliasMap.put(item, constName);
                    idx++;
                }
                enumItemConstMap.put(et, itemMap);
            }
            collector.put(prefix, resolved);
        } else if (resolved instanceof UnionType) {
            UnionType ut = (UnionType) resolved;
            // Tag
            String tagPrefix = prefix.isEmpty() ? "tag" : prefix + "_tag";
            collector.put(tagPrefix, new IntType()); 
            
            int idx = 0;
            for (Type subT : ut.getBaseTypes()) {
                String valPrefix = prefix.isEmpty() ? "val_" + idx : prefix + "_val_" + idx;
                collectLeafFields(valPrefix, subT, collector);
                idx++;
            }
        } else {
            // Leaf
            // We want to preserve BoundedIntType if possible, but resolveType unwraps IdType.
            // If 'type' was IdType -> BoundedIntType, 'resolved' is BoundedIntType.
            // If 'type' was BoundedIntType, 'resolved' is BoundedIntType.
            // So 'resolved' is correct.
            collector.put(prefix, resolved);
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
                    String atomName = field.isEmpty() ? base : (base + "_" + field);
                    Type ftype = e.getValue().get(field);
                    
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

    private Term createDefaultInit(Type t) {
        Type resolved = resolveType(t);
        if (resolved instanceof IntType) return new IntValue().setValue(0);
        if (resolved instanceof BoundedIntType) return ((BoundedIntType) resolved).getLowerBound();
        if (resolved instanceof DoubleType) return new DoubleValue().setValue(0.0);
        if (resolved instanceof BoolType) return new BoolValue().setValue(false);
        
        if (resolved instanceof TupleType) {
             TupleTerm tt = new TupleTerm();
             List<Term> vals = new ArrayList<>();
             for(Type sub : ((TupleType)resolved).getBaseTypes()) vals.add(createDefaultInit(sub));
             tt.setValues(vals);
             return tt;
        }
        if (resolved instanceof StructType) {
            StructTerm st = new StructTerm();
            Map<String, Term> fields = new HashMap<>();
            for(Map.Entry<String, Type> e : ((StructType)resolved).getFields().entrySet()) {
                fields.put(e.getKey(), createDefaultInit(e.getValue()));
            }
            st.setFields(fields);
            return st;
        }
        // ListType, UnionType, etc. defaults can be added as needed
        return new IntValue().setValue(0);
    }

    private Term extractValue(Term root, String path, Type rootType) throws ValidationException {
        if (path.isEmpty()) return root;
        
        Type resolvedType = resolveType(rootType);
        
        if (resolvedType instanceof UnionType) {
            UnionType ut = (UnionType) resolvedType;
            if (path.equals("tag")) {
                int tag = getMatchingVariantIndex(ut, root);
                return new IntValue().setValue(tag);
            } else if (path.startsWith("val")) {
                // path is like "val_0" or "val_0_rest"
                String sub = path.substring(4); // remove "val_"
                String[] parts = sub.split("_", 2);
                int idx = Integer.parseInt(parts[0]);
                String rest = parts.length > 1 ? parts[1] : "";
                
                int activeTag = getMatchingVariantIndex(ut, root);
                if (idx == activeTag) {
                    return extractValue(root, rest, ut.getBaseTypes().get(idx));
                } else {
                    return createDefaultInit(ut.getBaseTypes().get(idx));
                }
            }
        }
        
        String[] parts = path.split("_", 2);
        String head = parts[0];
        String tail = parts.length > 1 ? parts[1] : "";

        if (resolvedType instanceof StructType) {
            if (root instanceof StructTerm) {
                return extractValue(((StructTerm) root).getFields().get(head), tail, ((StructType) resolvedType).getFields().get(head));
            }
        } else if (resolvedType instanceof TupleType) {
            if (root instanceof TupleTerm) {
                int idx = Integer.parseInt(head);
                return extractValue(((TupleTerm) root).getValues().get(idx), tail, ((TupleType) resolvedType).getBaseTypes().get(idx));
            }
        } else if (resolvedType instanceof ListType) {
            if (root instanceof ListTerm) {
                int idx = Integer.parseInt(head);
                return extractValue(((ListTerm) root).getValues().get(idx), tail, ((ListType) resolvedType).getBaseType());
            }
        }
        
        return root;
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
                
                if (init == null && vd.getType() instanceof UnionType) {
                    UnionType ut = (UnionType) vd.getType();
                    for (Type base : ut.getBaseTypes()) {
                        if (base instanceof InitType) {
                            init = ((InitType) base).getDefaultValue();
                            break;
                        }
                    }
                }
                
                if (init == null) {
                    init = createDefaultInit(vd.getType());
                }

                if (init != null) {
                    Map<String, Type> fields = varFields.get(id);
                    for (Map.Entry<String, Type> entry : fields.entrySet()) {
                        String path = entry.getKey();
                        String atom = path.isEmpty() ? id : (id + "_" + path);
                        
                        Term val = extractValue(init, path, vd.getType());
                        String expr0 = termToZ3(val, 0);
                        sb.append(String.format("s.add(%s_0 == %s)\n", atom, expr0));
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
                        String atom = field.isEmpty() ? base : (base + "_" + field);
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

    private String resolveAtomName(Term term) throws ValidationException {
        if (term instanceof IdValue) {
            return ((IdValue) term).getIdentifier();
        } else if (term instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) term;
            String owner = resolveAtomName(ft.getOwner());
            return owner + "_" + ft.getField();
        } else if (term instanceof ElementTerm) {
            ElementTerm et = (ElementTerm) term;
            String container = resolveAtomName(et.getContainer());
            Term key = et.getKey();
            if (key instanceof IntValue) {
                return container + "_" + ((IntValue) key).getValue();
            }
            throw new ValidationException(null, "Z3Generator: Dynamic array indexing is not supported. Only constant integer indices are allowed. Found key: " + key);
        }
        throw new ValidationException(null, "Z3Generator: Unsupported term type for atom resolution: " + term.getClass().getSimpleName());
    }

    private String getRootVar(Term term) throws ValidationException {
        if (term instanceof IdValue) return ((IdValue) term).getIdentifier();
        if (term instanceof FieldTerm) return getRootVar(((FieldTerm) term).getOwner());
        if (term instanceof ElementTerm) return getRootVar(((ElementTerm) term).getContainer());
        throw new ValidationException(null, "Z3Generator: Could not determine root variable from term: " + term.getClass().getSimpleName());
    }

    private Type getSubType(Type root, String path) {
        if (path.isEmpty()) return root;
        Type resolved = resolveType(root);
        String[] parts = path.split("_", 2);
        String head = parts[0];
        String tail = parts.length > 1 ? parts[1] : "";
        
        if (resolved instanceof StructType) {
            return getSubType(((StructType) resolved).getFields().get(head), tail);
        } else if (resolved instanceof TupleType) {
            int idx = Integer.parseInt(head);
            return getSubType(((TupleType) resolved).getBaseTypes().get(idx), tail);
        } else if (resolved instanceof ListType) {
            return getSubType(((ListType) resolved).getBaseType(), tail);
        } else if (resolved instanceof UnionType) {
            if (head.equals("tag")) return new IntType();
            if (head.startsWith("val")) {
                // Format: val_i_rest
                // But head is just "val" if split by "_"? No, split logic in getSubType uses split("_", 2).
                // If path is "val_0_x", head="val", tail="0_x".
                // But collectLeafFields generates "val_0" as prefix.
                // Wait, collectLeafFields: prefix + "_val_" + idx.
                // If prefix is empty: "val_" + idx.
                // So path is "val_0".
                // split("_", 2) -> "val", "0".
                // So head is "val".
                
                // However, if I have nested union?
                // Let's assume standard format.
                
                // Actually, let's look at how I implemented extractValue.
                // It parses "val_i" manually.
                
                // In getSubType, I need to match the structure.
                // If head is "val", then tail starts with index.
                String[] tailParts = tail.split("_", 2);
                int idx = Integer.parseInt(tailParts[0]);
                String subTail = tailParts.length > 1 ? tailParts[1] : "";
                return getSubType(((UnionType) resolved).getBaseTypes().get(idx), subTail);
            }
        }
        return root;
    }

    private Type getTermType(Term term) {
        if (term instanceof IdValue) {
            return varTypes.get(((IdValue) term).getIdentifier());
        } else if (term instanceof FieldTerm) {
            FieldTerm ft = (FieldTerm) term;
            Type ownerType = getTermType(ft.getOwner());
            if (ownerType == null) return null;
            Type resolved = resolveType(ownerType);
            if (resolved instanceof StructType) {
                return ((StructType) resolved).getFields().get(ft.getField());
            }
        } else if (term instanceof ElementTerm) {
            ElementTerm et = (ElementTerm) term;
            Type containerType = getTermType(et.getContainer());
            if (containerType == null) return null;
            Type resolved = resolveType(containerType);
            if (resolved instanceof TupleType) {
                Term key = et.getKey();
                if (key instanceof IntValue) {
                    int idx = ((IntValue) key).getValue();
                    return ((TupleType) resolved).getBaseTypes().get(idx);
                }
            } else if (resolved instanceof ListType) {
                return ((ListType) resolved).getBaseType();
            }
        }
        return null;
    }

    private void processAssignment(AssignmentStatement as, int t, Map<String, String> currentEnv, Map<String, String> nextStateValues) throws ValidationException {
        Term target = as.getTarget();
        Term expr = as.getExpr();

        if (target == null) {
            termToZ3(expr, t, currentEnv);
            return;
        }

        String targetPrefix = resolveAtomName(target);
        String rootVar = getRootVar(target);
        
        Map<String, Type> fields = varFields.get(rootVar);
        Type rootType = varTypes.get(rootVar);
        
        String relativePath = targetPrefix.equals(rootVar) ? "" : targetPrefix.substring(rootVar.length() + 1);
        
        for (Map.Entry<String, Type> entry : fields.entrySet()) {
            String path = entry.getKey();
            
            if (path.equals(relativePath) || path.startsWith(relativePath + "_") || relativePath.isEmpty()) {
                String atom = path.isEmpty() ? rootVar : (rootVar + "_" + path);
                
                String rhsPath = "";
                if (!relativePath.isEmpty()) {
                    if (path.equals(relativePath)) rhsPath = "";
                    else rhsPath = path.substring(relativePath.length() + 1);
                } else {
                    rhsPath = path;
                }
                
                String val = null;
                if (expr instanceof IdValue) {
                    String rhsVar = ((IdValue) expr).getIdentifier();
                    
                    Type rhsType = varTypes.get(rhsVar);
                    Type targetContainerType = getSubType(rootType, relativePath);
                    
                    if (rhsType instanceof UnionType && !(targetContainerType instanceof UnionType)) {
                         boolean explicitUnionAccess = rhsPath.equals("tag") || rhsPath.startsWith("val_");
                         if (!explicitUnionAccess) {
                             int variantIdx = getMatchingVariantIndex((UnionType) rhsType, targetContainerType);
                             if (variantIdx != -1) {
                                 String prefix = "val_" + variantIdx;
                                 rhsPath = prefix + (rhsPath.isEmpty() ? "" : "_" + rhsPath);
                             } else {
                                 throw new ValidationException(null, "Z3Generator: Cannot assign Union type '" + rhsVar + "' to '" + targetPrefix + "'. No matching variant found for type " + targetContainerType.getClass().getSimpleName());
                             }
                         }
                    }

                    String rhsAtom = rhsPath.isEmpty() ? rhsVar : (rhsVar + "_" + rhsPath);
                    if (currentEnv.containsKey(rhsAtom)) {
                        val = currentEnv.get(rhsAtom);
                    } else {
                        val = String.format("%s_%d", rhsAtom, t);
                    }
                } else {
                    // Pass the type of the container (rootType at relativePath) to extractValue
                    // so it can handle implicit union conversions.
                    Type containerType = getSubType(rootType, relativePath);
                    Term extracted = extractValue(expr, rhsPath, containerType);
                    val = termToZ3(extracted, t, currentEnv);
                }
                
                currentEnv.put(atom, val);
                nextStateValues.put(atom, val);
            }
        }
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

        List<String> varsToPrint = new ArrayList<>();
        for (Map.Entry<String, Map<String, Type>> e : varFields.entrySet()) {
            String base = e.getKey();
            for (String field : e.getValue().keySet()) {
                String atomName = field.isEmpty() ? base : (base + "_" + field);
                varsToPrint.add(atomName);
            }
        }

        sb.append("    vars_to_print = [\n");
        for (String v : varsToPrint) {
            sb.append("        '" + v + "',\n");
        }
        sb.append("    ]\n\n");

        sb.append("    for i in range(" + (this.k + 1) + "):\n");
        sb.append("        print(f\"Step {i}:\")\n");
        sb.append("        for base_name in vars_to_print:\n");
        sb.append("            var_name = f\"{base_name}_{i}\"\n");
        sb.append("            if var_name in globals():\n");
        sb.append("                val = m.evaluate(globals()[var_name])\n");
        sb.append("                print(f\"  {base_name} : {val}\")\n");
        sb.append("        print(\"-\" * 20)\n");
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
        if (term instanceof TupleTerm) return handleTupleTerm((TupleTerm) term, t, env);
        if (term instanceof ListTerm) return handleListTerm((ListTerm) term, t, env);
        if (term instanceof ElementTerm) return handleElementTerm((ElementTerm) term, t, env);
        if (term instanceof IteTerm) return handleIteTerm((IteTerm) term, t, env);
        if (term instanceof BinaryOperatorTerm) return handleBinaryOperator((BinaryOperatorTerm) term, t, env);
        if (term instanceof SingleOperatorTerm) return handleSingleOperator((SingleOperatorTerm) term, t, env);
        if (term instanceof CallTerm) return handleCallTerm((CallTerm) term, t, env);

        throw new ValidationException(null, "Z3Generator: Unsupported term type in expression: " + term.getClass().getSimpleName());
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
        String atom = resolveAtomName(ft);
        if (atom != null) {
            if (env != null && env.containsKey(atom)) return env.get(atom);
            return String.format("%s_%d", atom, t);
        }
        
        // Fallback for cases where resolveAtomName fails (e.g. dynamic access not supported in flattened model)
        throw ValidationException.UnderDevelopment();
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

    private String handleTupleTerm(TupleTerm tt, int t, Map<String, String> env) throws ValidationException {
        StringBuilder sb = new StringBuilder();
        sb.append("(");
        boolean first = true;
        for (Term elem : tt.getValues()) {
            if (!first) sb.append(", ");
            sb.append(termToZ3(elem, t, env));
            first = false;
        }
        sb.append(")");
        return sb.toString();
    }

    private String handleListTerm(ListTerm lt, int t, Map<String, String> env) throws ValidationException {
        // For Z3, we might not need to construct a full array object if we are flattening.
        // But if it's used in an expression, we might need to return something.
        // However, in the flattened model, array literals usually appear in assignments or init.
        // If it appears elsewhere, it's complex.
        // For now, let's return a tuple-like representation or throw if not supported in expression context.
        // Actually, if we treat it like a tuple, it might work for some cases.
        StringBuilder sb = new StringBuilder();
        sb.append("["); // Python list syntax
        boolean first = true;
        for (Term elem : lt.getValues()) {
            if (!first) sb.append(", ");
            sb.append(termToZ3(elem, t, env));
            first = false;
        }
        sb.append("]");
        return sb.toString();
    }

    private String handleElementTerm(ElementTerm et, int t, Map<String, String> env) throws ValidationException {
        String atom = resolveAtomName(et);
        if (atom != null) {
            if (env != null && env.containsKey(atom)) return env.get(atom);
            return String.format("%s_%d", atom, t);
        }
        // Variable index or complex container - not supported in flattened model yet
        throw ValidationException.UnderDevelopment();
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
        
        // Custom function call
        List<String> args = new ArrayList<>();
        for (Term arg : ct.getArgs()) {
            // For now, we assume arguments are expressions that evaluate to primitive types
            // or flattened variables.
            // If we need to pass a struct, we would need to pass all its flattened fields.
            // But termToZ3 returns a single string.
            // If the argument is a struct variable 'p', termToZ3 might fail or return {...}.
            // We need to detect if 'arg' is a struct and expand it.
            
            // Simple heuristic: if arg is IdValue and it's a struct, expand it.
            if (arg instanceof IdValue) {
                String id = ((IdValue) arg).getIdentifier();
                if (varTypes.containsKey(id)) {
                    Type type = varTypes.get(id);
                    Type resolved = resolveType(type);
                    if (resolved instanceof StructType || resolved instanceof TupleType || resolved instanceof UnionType) {
                        // Expand
                        Map<String, Type> leafFields = new LinkedHashMap<>();
                        collectLeafFields("", type, leafFields);
                        for (String path : leafFields.keySet()) {
                            String flatName = path.isEmpty() ? id : id + "_" + path;
                            String val = env != null && env.containsKey(flatName) ? env.get(flatName) : flatName + "_" + t;
                            args.add(val);
                        }
                        continue;
                    }
                }
            }
            
            // Default: treat as single expression
            args.add(termToZ3(arg, t, env));
        }
        
        return String.format("%s(%s)", funcName, String.join(", ", args));
    }

    // =================================================================================================
    // Section: Property Translation (LTL / CTL*)
    // =================================================================================================

    private String propertyToCheckExpr(StateFormulae formula, int k) {
        try {
            String translated = translate(formula, 0, k);
            return String.format("Not(%s)", translated);
        } catch (ValidationException e) {
            e.printStackTrace();
            return null;
        }
    }

    private String translate(Formulae f, int t, int k) throws ValidationException {
        if (f instanceof AllPathFormulae) {
            return translate(((AllPathFormulae) f).getFormula(), t, k);
        }
        if (f instanceof ExistsPathFormulae) {
            return translate(((ExistsPathFormulae) f).getFormula(), t, k);
        }
        if (f instanceof AtomicPathFormulae) {
            return termToZ3(((AtomicPathFormulae) f).getTerm(), t);
        }
        if (f instanceof NotFormulae) {
            return String.format("Not(%s)", translate(((NotFormulae) f).getFormulae(), t, k));
        }
        if (f instanceof BinaryOperatorFormulae) {
            return translateBinary((BinaryOperatorFormulae) f, t, k);
        }
        if (f instanceof NextStateFormulae) {
            if (t >= k) return "False"; 
            return translate(((NextStateFormulae) f).getFormula(), t + 1, k);
        }
        if (f instanceof GloballyStateFormulae) {
            return translateGlobally((GloballyStateFormulae) f, t, k);
        }
        if (f instanceof FinallyStateFormulae) {
            return translateFinally((FinallyStateFormulae) f, t, k);
        }
        if (f instanceof UntilStateFormulae) {
            return translateUntil((UntilStateFormulae) f, t, k);
        }
        
        throw new ValidationException(null, "Unsupported formula type: " + f.getClass().getSimpleName());
    }

    private String translateBinary(BinaryOperatorFormulae bf, int t, int k) throws ValidationException {
        String left = translate(bf.getLeft(), t, k);
        String right = translate(bf.getRight(), t, k);
        String op = bf.getOpr().oprString;
        switch (op) {
            case "&&": return String.format("And(%s, %s)", left, right);
            case "||": return String.format("Or(%s, %s)", left, right);
            case "->": return String.format("Implies(%s, %s)", left, right);
            case "<->": return String.format("(%s == %s)", left, right);
            default: throw new ValidationException(null, "Unknown binary operator: " + op);
        }
    }

    private String translateGlobally(GloballyStateFormulae gf, int t, int k) throws ValidationException {
        List<String> parts = new ArrayList<>();
        Formulae inner = gf.getFormula();
        for (int i = t; i <= k; i++) {
            parts.add(translate(inner, i, k));
        }
        return String.format("And(%s)", String.join(", ", parts));
    }

    private String translateFinally(FinallyStateFormulae ff, int t, int k) throws ValidationException {
        List<String> parts = new ArrayList<>();
        Formulae inner = ff.getFormula();
        for (int i = t; i <= k; i++) {
            parts.add(translate(inner, i, k));
        }
        return String.format("Or(%s)", String.join(", ", parts));
    }

    private String translateUntil(UntilStateFormulae uf, int t, int k) throws ValidationException {
        Formulae p = uf.getKeep();
        Formulae q = uf.getUntil();
        List<String> options = new ArrayList<>();
        for (int i = t; i <= k; i++) {
            String q_i = translate(q, i, k);
            if (i == t) {
                options.add(q_i);
            } else {
                List<String> p_parts = new ArrayList<>();
                for (int j = t; j < i; j++) {
                    p_parts.add(translate(p, j, k));
                }
                p_parts.add(q_i);
                options.add(String.format("And(%s)", String.join(", ", p_parts)));
            }
        }
        return String.format("Or(%s)", String.join(", ", options));
    }
}

