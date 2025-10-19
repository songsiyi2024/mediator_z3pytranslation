/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.property.Formulae;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class NotFormulae<T extends Formulae>
implements PathFormulae {
    private RawElement parent;
    private T formulae;

    public T getFormulae() {
        return this.formulae;
    }

    public NotFormulae<T> setFormulae(T formulae) {
        this.formulae = formulae;
        formulae.setParent(this);
        return this;
    }

    public String toString() {
        return "!" + this.formulae.toString();
    }

    @Override
    public int getPrecedence() {
        return 0;
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
    public NotFormulae<T> setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }
}

