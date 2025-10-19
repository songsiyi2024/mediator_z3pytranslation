/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class StructTerm
implements Term {
    private RawElement parent = null;
    private Map<String, Term> fields = new HashMap<String, Term>();

    public Map<String, Term> getFields() {
        return this.fields;
    }

    public StructTerm addField(String name, Term term) throws ValidationException {
        if (this.fields.containsKey(name)) {
            throw ValidationException.DumplicatedIdentifier(name, "field name");
        }
        this.fields.put(name, term);
        term.setParent(this);
        return this;
    }

    public StructTerm setFields(Map<String, Term> fields) {
        this.fields = fields;
        return this;
    }

    @Override
    public int getPrecedence() {
        return 13;
    }

    @Override
    public StructTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        this.setParent(parent);
        if (!(context instanceof MediatorLangParser.StructTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "StructTermContext", context.toString());
        }
        assert (((MediatorLangParser.StructTermContext)context).ID().size() == ((MediatorLangParser.StructTermContext)context).term().size());
        for (int i = 0; i < ((MediatorLangParser.StructTermContext)context).ID().size(); ++i) {
            this.addField(((MediatorLangParser.StructTermContext)context).ID(i).getText(), Term.parse(((MediatorLangParser.StructTermContext)context).term(i), this));
        }
        return this;
    }

    public String toString() {
        String result = String.format("{ %s }", this.fields.keySet().stream().map(key -> String.format("%s = %s", key, this.fields.get(key).toString())).collect(Collectors.joining(", ")));
        if (result.length() > 40) {
            result = String.format("{\n%s\n}", UtilCode.addIndent(this.fields.keySet().stream().map(key -> String.format("%s = %s", key, this.fields.get(key).toString())).collect(Collectors.joining(",\n")), 1));
        }
        return result;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        for (Term t : this.getFields().values()) {
            t.refactor(typeRewriteMap, termRewriteMap);
        }
        return this;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public StructTerm setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

