/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.Map;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.EnumBinaryOperator;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class BinaryOperatorTerm
implements Term {
    private RawElement parent = null;
    private Term left;
    private Term right;
    private EnumBinaryOperator opr;

    @Override
    public Type getType() {
        return null;
    }

    @Override
    public int getPrecedence() {
        return this.opr.oprLevel;
    }

    @Override
    public BinaryOperatorTerm refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        this.setLeft(this.getLeft().refactor(typeRewriteMap, termRewriteMap));
        this.setRight(this.getRight().refactor(typeRewriteMap, termRewriteMap));
        return this;
    }

    @Override
    public BinaryOperatorTerm fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.BinaryOprTermContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "BinaryOprTermContext", context.toString());
        }
        this.setParent(parent);
        this.setLeft(Term.parse(((MediatorLangParser.BinaryOprTermContext)context).left, this));
        this.setRight(Term.parse(((MediatorLangParser.BinaryOprTermContext)context).right, this));
        this.setOpr(EnumBinaryOperator.fromString(((MediatorLangParser.BinaryOprTermContext)context).opr.getText()));
        return this;
    }

    public String toString() {
        return String.format(this.right.getPrecedence() < this.getPrecedence() ? "%s %s (%s)" : "%s %s %s", this.left.toString(), this.opr.toString(), this.right.toString());
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public BinaryOperatorTerm setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public BinaryOperatorTerm copy(RawElement parent) throws ValidationException {
        BinaryOperatorTerm nbot = new BinaryOperatorTerm();
        nbot.setParent(parent);
        nbot.setLeft(this.left.copy(nbot));
        nbot.setRight(this.right.copy(nbot));
        nbot.setOpr(this.opr);
        return nbot;
    }

    public EnumBinaryOperator getOpr() {
        return this.opr;
    }

    public BinaryOperatorTerm setOpr(EnumBinaryOperator opr) {
        this.opr = opr;
        return this;
    }

    public Term getLeft() {
        return this.left;
    }

    public BinaryOperatorTerm setLeft(Term left) throws ValidationException {
        this.left = left;
        left.setParent(this);
        return this;
    }

    public Term getRight() {
        return this.right;
    }

    public BinaryOperatorTerm setRight(Term right) throws ValidationException {
        this.right = right;
        right.setParent(this);
        return this;
    }
}

