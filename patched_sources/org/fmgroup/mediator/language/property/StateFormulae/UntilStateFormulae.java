package org.fmgroup.mediator.language.property.StateFormulae;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class UntilStateFormulae
implements StateFormulae {
    private RawElement parent;
    private StateFormulae keep;
    private StateFormulae until;

    public StateFormulae getKeep() {
        return this.keep;
    }

    public UntilStateFormulae setKeep(StateFormulae keep) {
        this.keep = keep;
        keep.setParent(this);
        return this;
    }

    public StateFormulae getUntil() {
        return this.until;
    }

    public UntilStateFormulae setUntil(StateFormulae until) {
        this.until = until;
        until.setParent(this);
        return this;
    }

    @Override
    public UntilStateFormulae fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.UntilStateFormulaeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "UntilStateFormulaeContext", context.toString());
        }
        this.setParent(parent);
        this.setKeep(StateFormulae.parse(((MediatorLangParser.UntilStateFormulaeContext)context).keep, (RawElement)this));
        this.setUntil(StateFormulae.parse(((MediatorLangParser.UntilStateFormulaeContext)context).until, (RawElement)this));
        return this;
    }

    @Override
    public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return null;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public UntilStateFormulae setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public String toString() {
        return String.format("[%s U %s]", this.keep.toString(), this.until.toString());
    }

    @Override
    public Term copy(RawElement parent) throws ValidationException {
        UntilStateFormulae copy = new UntilStateFormulae();
        copy.setParent(parent);
        if (this.keep != null) {
            copy.setKeep((StateFormulae) this.keep.copy(copy));
        }
        if (this.until != null) {
            copy.setUntil((StateFormulae) this.until.copy(copy));
        }
        return copy;
    }
}
