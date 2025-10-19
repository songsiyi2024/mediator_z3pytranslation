/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.property.EnumBinaryOperatorTemporal;
import org.fmgroup.mediator.language.property.Formulae;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class BinaryOperatorFormulae<T extends Formulae>
implements PathFormulae {
    private RawElement parent;
    private T left;
    private T right;
    private EnumBinaryOperatorTemporal opr;

    public T getLeft() {
        return this.left;
    }

    public BinaryOperatorFormulae setLeft(T left) {
        this.left = left;
        left.setParent(this);
        return this;
    }

    public T getRight() {
        return this.right;
    }

    public BinaryOperatorFormulae setRight(T right) {
        this.right = right;
        right.setParent(this);
        return this;
    }

    public EnumBinaryOperatorTemporal getOpr() {
        return this.opr;
    }

    public BinaryOperatorFormulae setOpr(EnumBinaryOperatorTemporal opr) {
        this.opr = opr;
        return this;
    }

    @Override
    public int getPrecedence() {
        return this.opr.oprLevel;
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
    public BinaryOperatorFormulae<T> setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public String toString() {
        return String.format(this.right.getPrecedence() < this.getPrecedence() ? "%s %s (%s)" : "%s %s %s", this.left.toString(), this.opr.toString(), this.right.toString());
    }
}

