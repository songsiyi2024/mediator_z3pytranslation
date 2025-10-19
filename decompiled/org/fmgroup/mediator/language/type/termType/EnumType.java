/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.termType;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.tree.ParseTree;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.EnumValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class EnumType
implements Type {
    private RawElement parent;
    private List<String> items = new ArrayList<String>();

    public List<String> getItems() {
        return this.items;
    }

    public EnumType setItems(List<String> items) throws ValidationException {
        this.items = new ArrayList<String>();
        for (String item : items) {
            this.addItem(item);
        }
        return this;
    }

    public EnumType addItem(String item) throws ValidationException {
        if (this.getItems().contains(item)) {
            throw ValidationException.DumplicatedIdentifier(item, "enum item");
        }
        this.items.add(item);
        return this;
    }

    @Override
    public Term getInitValue() throws ValidationException {
        return new EnumValue().setParent(this).setReference(this).setIdentifier(this.getItems().get(0));
    }

    @Override
    public EnumType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.EnumTypeContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "EnumTypeContext", context.toString());
        }
        this.setItems(((MediatorLangParser.EnumTypeContext)context).ID().stream().map(ParseTree::getText).collect(Collectors.toList()));
        return this;
    }

    public String toString() {
        return "enum { " + String.join((CharSequence)", ", this.items) + " }";
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public EnumType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public EnumType copy(RawElement parent) throws ValidationException {
        EnumType net = new EnumType();
        net.setParent(parent);
        net.setItems(this.getItems());
        return net;
    }

    @Override
    public Type refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return this;
    }
}

