/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.property;

import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.term.Term;

public interface Formulae
extends RawElement,
Term {
    @Override
    default public int getPrecedence() {
        return 0;
    }
}

