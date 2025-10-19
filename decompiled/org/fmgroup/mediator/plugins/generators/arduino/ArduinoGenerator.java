/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.generators.arduino;

import java.nio.file.FileAlreadyExistsException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.entity.automaton.TransitionGroup;
import org.fmgroup.mediator.language.entity.automaton.TransitionSingle;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.scope.TypeDeclaration;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.statement.AssignmentStatement;
import org.fmgroup.mediator.language.statement.IteStatement;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.statement.SynchronizingStatement;
import org.fmgroup.mediator.language.term.BinaryOperatorTerm;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.language.term.CallTerm;
import org.fmgroup.mediator.language.term.DoubleValue;
import org.fmgroup.mediator.language.term.ElementTerm;
import org.fmgroup.mediator.language.term.EnumBinaryOperator;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.FieldTerm;
import org.fmgroup.mediator.language.term.IdValue;
import org.fmgroup.mediator.language.term.IntValue;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.SingleOperatorTerm;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.termType.BoolType;
import org.fmgroup.mediator.language.type.termType.BoundedIntType;
import org.fmgroup.mediator.language.type.termType.DoubleType;
import org.fmgroup.mediator.language.type.termType.EnumType;
import org.fmgroup.mediator.language.type.termType.IdType;
import org.fmgroup.mediator.language.type.termType.InitType;
import org.fmgroup.mediator.language.type.termType.IntType;
import org.fmgroup.mediator.language.type.termType.ListType;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugin.generator.Generator;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoGeneratorException;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoPinDirection;
import org.fmgroup.mediator.plugins.scheduler.Scheduler;

public class ArduinoGenerator
implements Generator {
    private Map<Integer, ArduinoPinDirection> pinStatus = new HashMap<Integer, ArduinoPinDirection>();

    public String entityGenerate(Entity elem) throws ArduinoGeneratorException {
        this.pinStatus = new HashMap<Integer, ArduinoPinDirection>();
        if (elem instanceof Automaton) {
            try {
                return String.format("%s\n%s", this.typedefGenerate((Program)elem.getParent()), this.automatonGenerate((Automaton)elem));
            }
            catch (ValidationException e) {
                e.printStackTrace();
            }
        } else if (elem instanceof org.fmgroup.mediator.language.entity.system.System) {
            try {
                return this.entityGenerate(Scheduler.Schedule((org.fmgroup.mediator.language.entity.system.System)elem));
            }
            catch (ValidationException e) {
                e.printStackTrace();
            }
        }
        return null;
    }

    @Override
    public FileSet generate(RawElement elem) throws ArduinoGeneratorException {
        FileSet files = new FileSet();
        if (elem instanceof Entity) {
            try {
                files.add(((Entity)elem).getName() + ".c", this.entityGenerate((Entity)elem));
            }
            catch (FileAlreadyExistsException e) {
                e.printStackTrace();
            }
            return files;
        }
        throw new ArduinoGeneratorException(String.format("unsupport language element %s", elem.getClass().getName()));
    }

    @Override
    public String getSupportedPlatform() {
        return "arduino";
    }

    private String typedefGenerate(Program p) throws ArduinoGeneratorException {
        String code = "";
        for (Declaration declaration : p.getTypedefs().getDeclarationList()) {
            assert (declaration instanceof TypeDeclaration);
            code = code + String.format("typedef %s %s;\n", this.typeGenerate(((TypeDeclaration)declaration).getType()), String.join((CharSequence)",", declaration.getIdentifiers()));
        }
        return code;
    }

    /*
     * WARNING - void declaration
     */
    private String automatonGenerate(Automaton a) throws ArduinoGeneratorException, ValidationException {
        void var7_11;
        if (a.getEntityInterface().getDeclarationList().size() > 0) {
            throw ArduinoGeneratorException.UnclosedEntity(a);
        }
        String prog = "";
        String globalDeclarations = "";
        String setup = "";
        String loop = "";
        for (Declaration declaration : a.getLocalVars().getDeclarationList()) {
            assert (declaration instanceof VariableDeclaration);
            String strType = this.typeGenerate(((VariableDeclaration)declaration).getType());
            for (String name : declaration.getIdentifiers()) {
                if (!strType.contains("%s")) {
                    strType = strType + " %s";
                }
                strType = strType + ";\n";
                globalDeclarations = globalDeclarations + String.format(strType, name);
            }
        }
        globalDeclarations = globalDeclarations + String.format("\nint cmd_activated[%d];\nint cmd_activated_counter;\n", ((TransitionGroup)a.getTransitions().get(0)).getTransitions().size());
        globalDeclarations = globalDeclarations + "int cmd;\n";
        for (Declaration declaration : a.getLocalVars().getDeclarationList()) {
            assert (declaration instanceof VariableDeclaration);
            for (String name : declaration.getIdentifiers()) {
                setup = setup + String.format("%s = %s;\n", name, this.termGenerate(((VariableDeclaration)declaration).getType().getInitValue(), 0));
            }
        }
        assert (a.getTransitions().size() == 1);
        assert (a.getTransitions().get(0) instanceof TransitionGroup);
        loop = loop + String.format("cmd_activated_counter = 0;\n", ((TransitionGroup)a.getTransitions().get(0)).getTransitions().size());
        String conditionCheck = "";
        String string = "";
        for (Transition t : ((TransitionGroup)a.getTransitions().get(0)).getTransitions()) {
            assert (t instanceof TransitionSingle);
            int index = ((TransitionGroup)a.getTransitions().get(0)).getTransitions().indexOf(t);
            conditionCheck = conditionCheck + String.format("if (%s) {\n\tcmd_activated[cmd_activated_counter] = %d;\n\tcmd_activated_counter ++;\n}\n", this.termGenerate(((TransitionSingle)t).getGuard(), 0), index);
            String string2 = (String)var7_11 + String.format("if (cmd == %d) {\n%s\n}\n", index, UtilCode.addIndent(this.statementGenerate(((TransitionSingle)t).getStatements()), 1));
        }
        loop = loop + conditionCheck;
        loop = loop + "cmd = cmd_activated[random(cmd_activated_counter)];\n";
        loop = loop + (String)var7_11;
        for (Integer pin : this.pinStatus.keySet()) {
            if (this.pinStatus.get(pin).equals((Object)ArduinoPinDirection.IN)) {
                setup = setup + String.format("pinMode(%d, INPUT);\n", pin);
                continue;
            }
            setup = setup + String.format("pinMode(%d, OUTPUT);\n", pin);
        }
        prog = String.format("%s\nvoid setup() {\n%s}\n\nvoid loop() {\n%s}\n", globalDeclarations, UtilCode.addIndent(setup, 1), UtilCode.addIndent(loop, 1));
        return prog;
    }

    private String statementGenerate(List<Statement> statements) throws ArduinoGeneratorException, ValidationException {
        String rel = "";
        for (Statement s : statements) {
            if (rel.length() > 0) {
                rel = rel + "\n";
            }
            if (s instanceof SynchronizingStatement) {
                System.err.println("A sync statement is not supposed to show up when generating codes.");
                continue;
            }
            if (s instanceof AssignmentStatement) {
                if (((AssignmentStatement)s).getTarget() == null) {
                    rel = rel + this.termGenerate(((AssignmentStatement)s).getExpr(), 0) + ";";
                    continue;
                }
                rel = rel + this.termGenerate(((AssignmentStatement)s).getTarget(), 0) + " = " + this.termGenerate(((AssignmentStatement)s).getExpr(), 0) + ";";
                String assertion = this.termAssertionGenerate(((AssignmentStatement)s).getTarget());
                if (assertion.length() <= 0) continue;
                rel = rel + "\n" + assertion;
                continue;
            }
            if (s instanceof IteStatement) {
                rel = rel + String.format("if (%s) {\n%s\n}", this.termGenerate(((IteStatement)s).getCondition(), 0), UtilCode.addIndent(this.statementGenerate(((IteStatement)s).getThenStmts()), 1));
                if (((IteStatement)s).getElseStmts().size() <= 0) continue;
                rel = rel + String.format(" else {\n%s\n}", UtilCode.addIndent(this.statementGenerate(((IteStatement)s).getElseStmts()), 1));
                continue;
            }
            throw ArduinoGeneratorException.UnhandledStatement(s);
        }
        return rel;
    }

    private String typeGenerate(Type t) throws ArduinoGeneratorException {
        if (t instanceof BoundedIntType || t instanceof IntType) {
            return "int";
        }
        if (t instanceof DoubleType) {
            return "double";
        }
        if (t instanceof ListType) {
            if (((ListType)t).getCapacity() != null) {
                return this.typeGenerate(((ListType)t).getBaseType()) + " %s[" + this.termGenerate(((ListType)t).getCapacity(), 0) + "]";
            }
            return this.typeGenerate(((ListType)t).getBaseType()) + " * %s";
        }
        if (t instanceof InitType) {
            return this.typeGenerate(((InitType)t).getBaseType());
        }
        if (t instanceof IdType) {
            return ((IdType)t).getIdentifier();
        }
        if (t instanceof EnumType) {
            return String.format("enum {%s}", String.join((CharSequence)",", ((EnumType)t).getItems()));
        }
        if (t instanceof BoolType) {
            return "bool";
        }
        throw ArduinoGeneratorException.UnhandledType(t);
    }

    private String termGenerate(Term t, int parentPrecedence) throws ArduinoGeneratorException {
        if (t instanceof IntValue) {
            return String.valueOf(((IntValue)t).getValue());
        }
        if (t instanceof NullValue) {
            return "NULL";
        }
        if (t instanceof BoolValue) {
            return ((BoolValue)t).getValue() ? "1" : "0";
        }
        if (t instanceof IdValue) {
            return ((IdValue)t).getIdentifier();
        }
        if (t instanceof DoubleValue) {
            return String.valueOf(((DoubleValue)t).getValue());
        }
        if (t instanceof BinaryOperatorTerm) {
            return String.format("%s %s %s", this.termGenerate(((BinaryOperatorTerm)t).getLeft(), t.getPrecedence()), ((BinaryOperatorTerm)t).getOpr().toString(), this.termGenerate(((BinaryOperatorTerm)t).getRight(), t.getPrecedence()));
        }
        if (t instanceof FieldTerm) {
            return String.format("%s.%s", this.termGenerate(((FieldTerm)t).getOwner(), t.getPrecedence()), ((FieldTerm)t).getField());
        }
        if (t instanceof CallTerm) {
            ArrayList<String> args = new ArrayList<String>();
            for (Term arg : ((CallTerm)t).getArgs()) {
                args.add(this.termGenerate(arg, 0));
            }
            String calleeName = ((CallTerm)t).getCallee().toString();
            Integer pin = null;
            ArduinoPinDirection pinDirection = null;
            if (calleeName.equals("digitalWrite") || calleeName.equals("analogWrite")) {
                pin = Integer.parseInt(((CallTerm)t).getArg(0).toString());
                pinDirection = ArduinoPinDirection.OUT;
            } else if (calleeName.equals("digitalRead") || calleeName.equals("analogRead")) {
                pin = Integer.parseInt(((CallTerm)t).getArg(0).toString());
                pinDirection = ArduinoPinDirection.IN;
            }
            if (pin != null) {
                if (this.pinStatus.containsKey(pin) && !this.pinStatus.get(pin).equals((Object)pinDirection)) {
                    throw ArduinoGeneratorException.InconsistentPinType(pin);
                }
                this.pinStatus.put(pin, pinDirection);
            }
            return String.format("%s(%s)", ((CallTerm)t).getCallee().toString(), String.join((CharSequence)", ", args));
        }
        if (t instanceof SingleOperatorTerm) {
            return (Object)((Object)((SingleOperatorTerm)t).getOpr()) + this.termGenerate(((SingleOperatorTerm)t).getTerm(), t.getPrecedence());
        }
        if (t instanceof ElementTerm) {
            return String.format("%s[%s]", this.termGenerate(((ElementTerm)t).getContainer(), t.getPrecedence()), this.termGenerate(((ElementTerm)t).getKey(), 0));
        }
        if (t instanceof EnumValue) {
            return t.toString();
        }
        throw ArduinoGeneratorException.UnhandledTerm(t);
    }

    public String termAssertionGenerate(Term t) throws ValidationException, ArduinoGeneratorException {
        String result = "";
        if (t.getType() instanceof BoundedIntType) {
            BinaryOperatorTerm land = new BinaryOperatorTerm().setParent(t.getParent()).setOpr(EnumBinaryOperator.LAND).setLeft(new BinaryOperatorTerm()).setRight(new BinaryOperatorTerm());
            ((BinaryOperatorTerm)land.getLeft()).setLeft(t.copy());
            ((BinaryOperatorTerm)land.getLeft()).setRight(((BoundedIntType)t.getType()).getLowerBound());
            ((BinaryOperatorTerm)land.getLeft()).setOpr(EnumBinaryOperator.GEQ);
            ((BinaryOperatorTerm)land.getRight()).setLeft(t.copy());
            ((BinaryOperatorTerm)land.getRight()).setRight(((BoundedIntType)t.getType()).getUpperBound());
            ((BinaryOperatorTerm)land.getRight()).setOpr(EnumBinaryOperator.LEQ);
            result = this.termGenerate(land, 0);
        }
        if (result.length() > 0) {
            return String.format("assert (%s);", result);
        }
        return "";
    }

    @Override
    public String getName() {
        return "Arduino C code generator";
    }

    @Override
    public String getVersion() {
        return "0.0.1";
    }

    @Override
    public String getDescription() {
        return "providing support for Arduino C code generation";
    }

    @Override
    public List<String> requiredLibraries() {
        ArrayList<String> libs = new ArrayList<String>();
        libs.add("arduino");
        return libs;
    }
}

