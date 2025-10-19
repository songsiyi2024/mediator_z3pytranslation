/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property.StateFormulae;

import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.BinaryOperatorFormulae;
import org.fmgroup.mediator.language.property.EnumBinaryOperatorTemporal;
import org.fmgroup.mediator.language.property.Formulae;
import org.fmgroup.mediator.language.property.NotFormulae;
import org.fmgroup.mediator.language.property.PathFormulae.PathFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.FinallyStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.GloballyStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.NextStateFormulae;
import org.fmgroup.mediator.language.property.StateFormulae.UntilStateFormulae;

public interface StateFormulae
extends Formulae {
    public static StateFormulae parse(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (context instanceof MediatorLangParser.PathStateFormulaeContext) {
            return PathFormulae.parse(((MediatorLangParser.PathStateFormulaeContext)context).pathFormulae(), parent);
        }
        if (context instanceof MediatorLangParser.NotStateFormulaeContext) {
            RawElement formulae = new NotFormulae().setParent(parent);
            ((NotFormulae)formulae).setFormulae(StateFormulae.parse(((MediatorLangParser.NotStateFormulaeContext)context).stateFormulae(), formulae));
            return formulae;
        }
        if (context instanceof MediatorLangParser.BinaryStateFormulaeContext) {
            RawElement formulae = new BinaryOperatorFormulae().setParent(parent);
            ((BinaryOperatorFormulae)formulae).setOpr(EnumBinaryOperatorTemporal.fromString(((MediatorLangParser.BinaryStateFormulaeContext)context).opr.getText()));
            ((BinaryOperatorFormulae)formulae).setLeft(StateFormulae.parse(((MediatorLangParser.BinaryStateFormulaeContext)context).left, formulae));
            ((BinaryOperatorFormulae)formulae).setRight(StateFormulae.parse(((MediatorLangParser.BinaryStateFormulaeContext)context).right, formulae));
            return formulae;
        }
        if (context instanceof MediatorLangParser.NextStateFormulaeContext) {
            return new NextStateFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.FinallyStateFormulaeContext) {
            return new FinallyStateFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.GloballyStateFormulaeContext) {
            return new GloballyStateFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.UntilStateFormulaeContext) {
            return new UntilStateFormulae().fromContext(context, parent);
        }
        if (context instanceof MediatorLangParser.BracketStateFormulaeContext) {
            return StateFormulae.parse(((MediatorLangParser.BracketStateFormulaeContext)context).stateFormulae(), parent);
        }
        throw ValidationException.UnderDevelopment();
    }
}

