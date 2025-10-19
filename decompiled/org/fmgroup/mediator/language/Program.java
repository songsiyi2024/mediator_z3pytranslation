/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ParseTree;
import org.fmgroup.mediator.common.ToolInfo;
import org.fmgroup.mediator.core.antlr.VerboseListener;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.system.System;
import org.fmgroup.mediator.language.function.Function;
import org.fmgroup.mediator.language.generated.MediatorLangLexer;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.scope.TypeDeclaration;
import org.fmgroup.mediator.language.scope.TypeDeclarationCollection;

public class Program
implements RawElement,
Scope {
    private List<Program> dependencies = new ArrayList<Program>();
    private TypeDeclarationCollection typedefs = new TypeDeclarationCollection();
    private Map<String, Function> functions = new HashMap<String, Function>();
    private Map<String, Automaton> automata = new HashMap<String, Automaton>();
    private Map<String, Automaton> compiledAutomata = new HashMap<String, Automaton>();
    private Map<String, System> systems = new HashMap<String, System>();
    private List<String> externalPaths = null;

    public List<String> getExternalPaths() {
        return this.externalPaths;
    }

    public Program setExternalPaths(List<String> externalPaths) {
        this.externalPaths = new ArrayList<String>(externalPaths);
        return this;
    }

    public List<Program> getDependencies() {
        return this.dependencies;
    }

    public TypeDeclarationCollection getTypedefs() {
        return this.typedefs;
    }

    public Map<String, Function> getFunctions() {
        return this.functions;
    }

    public Program addFunction(String name, Function f) throws ValidationException {
        if (this.functions.containsKey(name)) {
            throw ValidationException.DumplicatedIdentifier(name, "function");
        }
        this.functions.put(name, f);
        return this;
    }

    public Map<String, Automaton> getAutomata() {
        return this.automata;
    }

    public Program addAutomaton(String name, Automaton a) throws ValidationException {
        if (this.automata.containsKey(name)) {
            throw ValidationException.DumplicatedIdentifier(name, "automaton");
        }
        this.automata.put(name, a);
        return this;
    }

    public Map<String, Automaton> getCompiledAutomata() {
        return this.compiledAutomata;
    }

    public Map<String, System> getSystems() {
        return this.systems;
    }

    public Program addSystem(String name, System s) throws ValidationException {
        if (this.systems.containsKey(name)) {
            throw ValidationException.DumplicatedIdentifier(name, "system");
        }
        this.systems.put(name, s);
        return this;
    }

    @Override
    public Program fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ProgContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ProgContext", context.toString());
        }
        MediatorLangParser.ProgContext prog = (MediatorLangParser.ProgContext)context;
        for (MediatorLangParser.DependencyContext dc : prog.dependency()) {
            if (dc.importedlib != null) {
                String string = dc.importedlib.scopes.stream().map(token -> token.getText() + "/").collect(Collectors.joining("")) + dc.importedlib.identifier.getText();
                continue;
            }
            String libpath = dc.fromlib.scopes.stream().map(token -> token.getText() + "/").collect(Collectors.joining("")) + dc.fromlib.identifier.getText() + ".med";
            List idTsoImport = dc.ID().stream().map(ParseTree::getText).collect(Collectors.toList());
            Program lib = null;
            try {
                lib = Program.parseFile(libpath);
            }
            catch (FileNotFoundException e) {
                throw ValidationException.UnknownIdentifier(libpath, "library");
            }
            for (TypeDeclaration typedef : lib.getTypedefs().getDeclarationList()) {
                boolean flag = false;
                for (String name : typedef.getIdentifiers()) {
                    if (!idTsoImport.contains(name)) continue;
                    flag = true;
                    break;
                }
                if (!flag && !dc.importAll) continue;
                this.getTypedefs().addDeclaration(typedef);
            }
            for (String funcname : lib.getFunctions().keySet()) {
                if (!idTsoImport.contains(funcname) && !dc.importAll) continue;
                this.addFunction(funcname, lib.getFunctions().get(funcname));
            }
            for (String name : lib.getAutomata().keySet()) {
                if (!idTsoImport.contains(name) && !dc.importAll) continue;
                this.addAutomaton(name, lib.getAutomata().get(name));
            }
            for (String name : lib.getSystems().keySet()) {
                if (!idTsoImport.contains(name) && !dc.importAll) continue;
                this.addSystem(name, lib.getSystems().get(name));
            }
        }
        for (MediatorLangParser.TypedefContext tc : prog.typedef()) {
            this.typedefs.addDeclaration(new TypeDeclaration().fromContext(tc, this));
        }
        for (MediatorLangParser.FunctionContext fc : prog.function()) {
            Function func = new Function().setParent(this).fromContext(fc, this);
            this.functions.put(func.getName(), func);
        }
        for (MediatorLangParser.AutomatonContext ac : prog.automaton()) {
            Automaton automaton = new Automaton().fromContext(ac, this);
            this.automata.put(automaton.getName(), automaton);
        }
        for (MediatorLangParser.SystemContext sc : prog.system()) {
            System sys = new System().fromContext(sc, this);
            this.systems.put(sys.getName(), sys);
        }
        return this;
    }

    @Override
    public RawElement getParent() {
        return null;
    }

    @Override
    public RawElement setParent(RawElement parent) {
        return null;
    }

    public String toString() {
        String prog = "";
        prog = prog + this.typedefs.toString();
        prog = prog + "\n";
        for (String name : this.functions.keySet()) {
            prog = prog + this.functions.get(name).toString() + "\n";
        }
        prog = prog + "\n";
        for (String name : this.automata.keySet()) {
            prog = prog + this.automata.get(name).toString() + "\n";
        }
        prog = prog + "\n";
        for (String name : this.systems.keySet()) {
            prog = prog + this.systems.get(name).toString() + "\n";
        }
        return prog;
    }

    @Override
    public List<DeclarationCollection> getDeclarations() {
        ArrayList<DeclarationCollection> result = new ArrayList<DeclarationCollection>();
        result.add(this.typedefs);
        return result;
    }

    public Function getFunction(List<String> libraryPath, String identifier) {
        if (libraryPath == null || libraryPath.size() == 0) {
            if (this.functions.containsKey(identifier)) {
                return this.functions.get(identifier);
            }
        } else {
            return null;
        }
        return null;
    }

    public Entity getEntity(List<String> libraryPath, String identifier) {
        if (libraryPath == null || libraryPath.size() == 0) {
            if (this.automata.containsKey(identifier)) {
                return this.automata.get(identifier);
            }
            if (this.systems.containsKey(identifier)) {
                return this.systems.get(identifier);
            }
        } else {
            return null;
        }
        return null;
    }

    public static Program parseFile(String filename) throws FileNotFoundException {
        return Program.parseFile(filename, new ArrayList<String>());
    }

    public static Program parseFile(String filename, List<String> externalPaths) throws FileNotFoundException {
        block7: {
            File file = null;
            ArrayList<String> paths = new ArrayList<String>();
            paths.addAll(externalPaths);
            paths.add(ToolInfo.getSystemLibraryPath());
            paths.add(java.lang.System.getProperty("user.dir").toString());
            for (String path : paths) {
                if (!Files.exists(Paths.get(path, filename), new LinkOption[0])) continue;
                file = Paths.get(path, filename).toFile();
            }
            if (file == null) {
                throw new FileNotFoundException(String.format("cannot locate %s in all paths", filename));
            }
            try {
                FileInputStream is = new FileInputStream(file);
                MediatorLangLexer lexer = new MediatorLangLexer(CharStreams.fromStream(is));
                CommonTokenStream ts = new CommonTokenStream(lexer);
                MediatorLangParser parser = new MediatorLangParser(ts);
                parser.removeErrorListeners();
                VerboseListener listener = new VerboseListener();
                parser.addErrorListener(listener);
                MediatorLangParser.ProgContext prog = parser.prog();
                if (!listener.Succeed()) {
                    for (ValidationException ex : listener.getExceptions()) {
                        java.lang.System.err.println(ex.toString());
                    }
                    return null;
                }
                return new Program().setExternalPaths(externalPaths).fromContext(prog, null);
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            catch (ValidationException e) {
                java.lang.System.err.println(e.toString());
                if (!ToolInfo.DEBUG) break block7;
                e.printStackTrace();
            }
        }
        return null;
    }
}

