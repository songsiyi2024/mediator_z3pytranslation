/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.BinaryOperatorTerm;
import org.fmgroup.mediator.language.term.BoolValue;
import org.fmgroup.mediator.language.term.CallTerm;
import org.fmgroup.mediator.language.term.ElementTerm;
import org.fmgroup.mediator.language.term.FieldTerm;
import org.fmgroup.mediator.language.term.IdValue;
import org.fmgroup.mediator.language.term.IntValue;
import org.fmgroup.mediator.language.term.IteTerm;
import org.fmgroup.mediator.language.term.ListTerm;
import org.fmgroup.mediator.language.term.NullValue;
import org.fmgroup.mediator.language.term.PortVariableValue;
import org.fmgroup.mediator.language.term.SingleOperatorTerm;
import org.fmgroup.mediator.language.term.StructTerm;
import org.fmgroup.mediator.language.term.TupleTerm;
import org.fmgroup.mediator.language.type.Type;

public interface Term
extends RawElement {
    public static Term parse(MediatorLangParser.TermContext term, RawElement parent) throws ValidationException {
        if (term instanceof MediatorLangParser.ValueTermContext) {
            return Term.parseValue(((MediatorLangParser.ValueTermContext)term).value(), parent);
        }
        if (term instanceof MediatorLangParser.BracketTermContext) {
            return Term.parse(((MediatorLangParser.BracketTermContext)term).term(), parent);
        }
        if (term instanceof MediatorLangParser.BinaryOprTermContext) {
            return new BinaryOperatorTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.FieldTermContext) {
            return new FieldTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.ElementTermContext) {
            return new ElementTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.CallTermContext) {
            return new CallTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.SingleOprTermContext) {
            return new SingleOperatorTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.ListTermContext) {
            return new ListTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.TupleTermContext) {
            return new TupleTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.StructTermContext) {
            return new StructTerm().fromContext(term, parent);
        }
        if (term instanceof MediatorLangParser.IteTermContext) {
            return new IteTerm().fromContext(term, parent);
        }
        throw ValidationException.UnregisteredTerm(term.getClass().toString()).At(term);
    }

    public static Term parseValue(MediatorLangParser.ValueContext value, RawElement parent) throws ValidationException {
        if (value instanceof MediatorLangParser.NullValueContext) {
            return new NullValue().fromContext(value, parent);
        }
        if (value instanceof MediatorLangParser.IntValueContext) {
            return new IntValue().fromContext(value, parent);
        }
        if (value instanceof MediatorLangParser.IdValueContext) {
            return new IdValue().fromContext(value, parent);
        }
        if (value instanceof MediatorLangParser.BoolValueContext) {
            return new BoolValue().fromContext(value, parent);
        }
        if (value instanceof MediatorLangParser.PortVarValueContext) {
            return new PortVariableValue().fromContext(value, parent);
        }
        throw ValidationException.UnregisteredTerm(value.getClass().toString());
    }

    public int getPrecedence();

    default public Type getType() throws ValidationException {
        if (!1.$assertionsDisabled) {
            throw new AssertionError();
        }
        return null;
    }

    default public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return this;
    }

    @Override
    default public Term copy(RawElement parent) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }

    @Override
    default public Term copy() throws ValidationException {
        return this.copy(this.getParent());
    }

    default public boolean isValue() {
        return false;
    }

    static {
        if (1.$assertionsDisabled) {
            // empty if block
        }
    }
}

