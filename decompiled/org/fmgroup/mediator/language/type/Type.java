/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type;

import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.paramType.AbstractType;
import org.fmgroup.mediator.language.type.paramType.TemplateType;
import org.fmgroup.mediator.language.type.termType.BoolType;
import org.fmgroup.mediator.language.type.termType.BoundedIntType;
import org.fmgroup.mediator.language.type.termType.DoubleType;
import org.fmgroup.mediator.language.type.termType.EnumType;
import org.fmgroup.mediator.language.type.termType.IdType;
import org.fmgroup.mediator.language.type.termType.InitType;
import org.fmgroup.mediator.language.type.termType.IntType;
import org.fmgroup.mediator.language.type.termType.ListType;
import org.fmgroup.mediator.language.type.termType.NullType;
import org.fmgroup.mediator.language.type.termType.StructType;
import org.fmgroup.mediator.language.type.termType.TupleType;
import org.fmgroup.mediator.language.type.termType.UnionType;

public interface Type
extends RawElement {
    @Deprecated
    public static boolean isFinite(Type type) {
        System.err.println("Unknown Type " + type.toString() + " @" + Type.class.toGenericString());
        return false;
    }

    public static Type parse(MediatorLangParser.TypeContext tc, RawElement parent) throws ValidationException {
        if (tc == null) {
            return null;
        }
        if (tc instanceof MediatorLangParser.DoubleTypeContext) {
            return new DoubleType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.BoolTypeContext) {
            return new BoolType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.BoundedIntTypeContext) {
            return new BoundedIntType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.IntTypeContext) {
            return new IntType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.IdTypeContext) {
            return new IdType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.NullTypeContext) {
            return new NullType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.TupleTypeContext) {
            return new TupleType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.InitTypeContext) {
            return new InitType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.ListTypeContext) {
            return new ListType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.BracketTypeContext) {
            return Type.parse(((MediatorLangParser.BracketTypeContext)tc).type(), parent);
        }
        if (tc instanceof MediatorLangParser.UnionTypeContext) {
            return new UnionType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.TemplateTypeContext) {
            return new TemplateType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.AbstractTypeContext) {
            return new AbstractType().setParent(parent);
        }
        if (tc instanceof MediatorLangParser.StructTypeContext) {
            return new StructType().fromContext(tc, parent);
        }
        if (tc instanceof MediatorLangParser.EnumTypeContext) {
            return new EnumType().fromContext(tc, parent);
        }
        throw ValidationException.UnregisteredType(tc.getClass().toString());
    }

    @Override
    default public Type copy(RawElement parent) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }

    @Override
    default public Type copy() throws ValidationException {
        return this.copy(this.getParent());
    }

    default public Term getInitValue() throws ValidationException {
        throw ValidationException.TypeNotInitialized(this);
    }

    default public Type extractRawType() throws ValidationException {
        return this.copy();
    }

    public Type refactor(Map<String, Type> var1, Map<String, Term> var2) throws ValidationException;

    default public boolean isSubtypeOf(Type parentType) {
        return false;
    }

    default public boolean isEqualTo(Type anotherType) {
        return this.isSubtypeOf(anotherType) && anotherType.isSubtypeOf(this);
    }
}

