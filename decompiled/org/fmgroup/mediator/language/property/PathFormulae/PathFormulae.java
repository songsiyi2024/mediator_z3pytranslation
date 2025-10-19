/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property.PathFormulae;

import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.BinaryOperatorFormulae;
import org.fmgroup.mediator.language.property.EnumBinaryOperatorTemporal;
import org.fmgroup.mediator.language.property.NotFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.AllPathFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.AtomicPathFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.ExistsPathFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.StateFormulae;

public interface PathFormulae
extends StateFormulae {
    public static PathFormulae parse(MediatorLangParser.PathFormulaeContext context, RawElement parent) throws ValidationException {
        if (context instanceof MediatorLangParser.NotPathFormulaeContext) {
            RawElement formula = new NotFormulae().setParent(parent);
            ((NotFormulae)formula).setFormulae(PathFormulae.parse(((MediatorLangParser.NotPathFormulaeContext)context).pathFormulae(), formula));
            return formula;
        }
        if (context instanceof MediatorLangParser.BinaryPathFormulaeContext) {
            RawElement formulae = new BinaryOperatorFormulae().setParent(parent);
            ((BinaryOperatorFormulae)formulae).setOpr(EnumBinaryOperatorTemporal.fromString(((MediatorLangParser.BinaryPathFormulaeContext)context).opr.getText()));
            ((BinaryOperatorFormulae)formulae).setLeft(PathFormulae.parse(((MediatorLangParser.BinaryPathFormulaeContext)context).left, formulae));
            ((BinaryOperatorFormulae)formulae).setRight(PathFormulae.parse(((MediatorLangParser.BinaryPathFormulaeContext)context).right, formulae));
            return formulae;
        }
        if (context instanceof MediatorLangParser.AllPathFormulaeContext) {
            return new AllPathFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.ExistsPathFormulaeContext) {
            return new ExistsPathFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.AtomicPathFormulaeContext) {
            return new AtomicPathFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.BracketPathFormulaeContext) {
            return PathFormulae.parse(((MediatorLangParser.BracketPathFormulaeContext)context).pathFormulae(), parent);
        }
        throw ValidationException.UnderDevelopment();
    }
}

