/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.function;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.Meta;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Template;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.function.FuncInterface;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class Function
implements RawElement,
Scope,
Templated {
    private RawElement parent = null;
    private String name;
    private Template template = null;
    private FuncInterface funcInterface = null;
    private VariableDeclarationCollection variables;
    private List<Statement> statements = new ArrayList<Statement>();
    private Type returnType = null;
    private boolean isNative = false;
    private Meta meta = null;

    public Meta getMeta() {
        return this.meta;
    }

    public Function setMeta(Meta meta) {
        this.meta = meta;
        meta.setParent(this);
        return this;
    }

    public String getName() {
        return this.name;
    }

    public Function setName(String name) {
        this.name = name;
        return this;
    }

    public FuncInterface getFuncInterface() {
        return this.funcInterface;
    }

    public Function setFuncInterface(FuncInterface funcInterface) {
        this.funcInterface = funcInterface;
        funcInterface.setParent(this);
        return this;
    }

    public VariableDeclarationCollection getVariables() {
        return this.variables;
    }

    public Function setVariables(VariableDeclarationCollection variables) {
        this.variables = variables;
        variables.setParent(this);
        return this;
    }

    public List<Statement> getStatements() {
        return this.statements;
    }

    public Function setStatements(List<Statement> statements) {
        this.statements = new ArrayList<Statement>();
        statements.forEach(this::addStatement);
        return this;
    }

    public Function addStatement(Statement statement) {
        this.statements.add(statement);
        statement.setParent(this);
        return this;
    }

    public Type getReturnType() {
        return this.returnType;
    }

    public Function setReturnType(Type returnType) {
        this.returnType = returnType;
        if (returnType != null) {
            returnType.setParent(this);
        }
        return this;
    }

    public boolean isNative() {
        return this.isNative;
    }

    public Function setNative(boolean aNative) {
        this.isNative = aNative;
        return this;
    }

    @Override
    public Function fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.FunctionContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "FunctionContext", context.toString());
        }
        this.setParent(parent);
        this.setNative(((MediatorLangParser.FunctionContext)context).isNative);
        this.setName(((MediatorLangParser.FunctionContext)context).name.getText());
        this.setTemplate(new Template().fromContext(((MediatorLangParser.FunctionContext)context).template(), this));
        this.setFuncInterface(new FuncInterface().fromContext(((MediatorLangParser.FunctionContext)context).functionInterface(), this));
        this.setReturnType(Type.parse(((MediatorLangParser.FunctionContext)context).returnType, this));
        if (!this.isNative) {
            this.setVariables(new VariableDeclarationCollection().setParent(this));
            for (MediatorLangParser.LocalVariableDefContext lvd : ((MediatorLangParser.FunctionContext)context).localVariableDef()) {
                this.getVariables().addDeclaration(new VariableDeclaration().fromContext(lvd, this));
            }
            for (MediatorLangParser.StatementContext sc : ((MediatorLangParser.FunctionContext)context).statement()) {
                this.addStatement(Statement.parse(sc, this));
            }
            if (((MediatorLangParser.FunctionContext)context).meta() != null) {
                this.setMeta(new Meta().fromContext(((MediatorLangParser.FunctionContext)context).meta(), this));
            }
        }
        return this;
    }

    public String toString() {
        String template;
        String string = template = this.template == null ? "" : this.template.toString();
        if (template.length() > 0) {
            template = "<" + template + "> ";
        }
        String rel = String.format("function %s%s (%s)", template, this.name, this.funcInterface.toString());
        if (this.returnType != null) {
            rel = rel + " : " + this.returnType.toString();
        }
        if (!this.isNative) {
            rel = rel + " {\n";
            rel = rel + UtilCode.addIndent(this.variables.toString(), 1);
            rel = rel + UtilCode.addIndent("statements {\n", 1);
            for (Statement stmt : this.statements) {
                rel = rel + UtilCode.addIndent(stmt.toString() + "\n", 2);
            }
            rel = rel + UtilCode.addIndent("}\n", 1);
            rel = rel + "}";
            if (this.getMeta() != null) {
                rel = rel + " " + this.getMeta().toString();
            }
        } else {
            rel = rel + ";";
        }
        return rel;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public Function setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public Function copy(RawElement parent) throws ValidationException {
        Function nfunc = new Function();
        nfunc.setParent(parent);
        nfunc.setName(this.getName());
        nfunc.setTemplate(this.getTemplate().copy(nfunc));
        nfunc.setFuncInterface(this.getFuncInterface().copy(nfunc));
        nfunc.setReturnType(this.getReturnType().copy(nfunc));
        for (Statement stmt : this.getStatements()) {
            nfunc.addStatement((Statement)stmt.copy(nfunc));
        }
        return nfunc;
    }

    @Override
    public List<DeclarationCollection> getDeclarations() {
        ArrayList<DeclarationCollection> result = new ArrayList<DeclarationCollection>();
        if (this.template != null) {
            result.add(this.template);
        }
        if (this.funcInterface != null) {
            result.add(this.funcInterface);
        }
        if (this.variables != null) {
            result.add(this.variables);
        }
        return result;
    }

    @Override
    public Template getTemplate() {
        return this.template;
    }

    @Override
    public Templated refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }

    @Override
    public Function setTemplate(Template template) {
        this.template = template;
        return this;
    }
}

