/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.paramType.TemplateType;

public class CallTerm
implements Term {
    private RawElement parent;
    private TemplateType callee;
    private List<Term> args = new ArrayList<Term>();

    @Override
    public CallTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.CallTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "CallTermContext", context.toString());
        }
        this.setParent(parent);
        this.setCallee(new TemplateType().fromContext(((MediatorLangParser.CallTermContext)context).callee, this));
        for (MediatorLangParser.TermContext t : ((MediatorLangParser.CallTermContext)context).args.term()) {
            this.addArg(Term.parse(t, this));
        }
        return this;
    }

    public String toString() {
        return String.format("%s(%s)", this.callee.toString(), this.args.stream().map(Object::toString).collect(Collectors.joining(", ")));
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public RawElement setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public TemplateType getCallee() {
        return this.callee;
    }

    public CallTerm setCallee(TemplateType callee) {
        this.callee = callee;
        callee.setParent(this);
        return this;
    }

    public CallTerm addArg(Term arg) {
        this.args.add(arg);
        arg.setParent(this);
        return this;
    }

    public Term getArg(int i) {
        return this.args.get(i);
    }

    public List<Term> getArgs() {
        return this.args;
    }

    public CallTerm setArgs(List<Term> args) {
        this.args = new ArrayList<Term>();
        args.forEach(this::addArg);
        return this;
    }

    @Override
    public CallTerm copy(RawElement parent) throws ValidationException {
        CallTerm nct = new CallTerm();
        nct.setParent(parent);
        nct.setCallee(this.getCallee().copy(nct));
        for (Term arg : this.args) {
            nct.addArg(arg.copy(nct));
        }
        return nct;
    }

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return 11;
    }

    @Override
    public CallTerm refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setCallee((TemplateType)this.getCallee().refactor((Map)typeRewriteMap, (Map)termRewriteMap));
        ArrayList<Term> args = new ArrayList<Term>();
        for (Term arg : this.getArgs()) {
            args.add(arg.refactor(typeRewriteMap, termRewriteMap));
        }
        this.setArgs(args);
        return this;
    }
}

