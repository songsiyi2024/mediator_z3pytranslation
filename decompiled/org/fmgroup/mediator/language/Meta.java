/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language;

import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.StructTerm;
import org.fmgroup.mediator.language.term.Term;

public class Meta
implements RawElement {
    private RawElement parent = null;
    private StructTerm infos = null;

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public Meta fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        this.setParent(parent);
        if (!(context instanceof MediatorLangParser.MetaContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "MetaContext", context.toString());
        }
        this.infos = new StructTerm().setParent(this);
        for (int i = 0; i < ((MediatorLangParser.MetaContext)context).ID().size(); ++i) {
            this.infos.addField(((MediatorLangParser.MetaContext)context).ID(i).getText(), Term.parse(((MediatorLangParser.MetaContext)context).term(i), this));
        }
        return this;
    }

    public String toString() {
        return String.format("meta %s", this.infos.toString());
    }

    @Override
    public Meta setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

