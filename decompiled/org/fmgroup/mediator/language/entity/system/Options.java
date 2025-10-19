/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;

public class Options
implements RawElement {
    private RawElement parent;
    private Map<String, Term> items = new HashMap<String, Term>();

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public Options setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public boolean isEmpty() {
        return this.items.isEmpty();
    }

    public boolean contains(String key) {
        return this.items.containsKey(key);
    }

    public Term get(String key) {
        return this.items.get(key);
    }

    @Override
    public Options fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ConnectionOptionsContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ProgContext", context.toString());
        }
        this.setParent(parent);
        for (MediatorLangParser.ConnectionOptionContext opt : ((MediatorLangParser.ConnectionOptionsContext)context).connectionOption()) {
            if (opt.term() == null) {
                this.items.put(opt.connectionOptionItem().getText(), null);
                continue;
            }
            this.items.put(opt.connectionOptionItem().getText(), Term.parse(opt.term(), this));
        }
        return this;
    }

    public String toString() {
        return String.join((CharSequence)",", this.items.entrySet().stream().map(stringTermEntry -> (String)stringTermEntry.getKey() + (stringTermEntry.getValue() == null ? "" : " = " + ((Term)stringTermEntry.getValue()).toString())).collect(Collectors.toList()));
    }
}

