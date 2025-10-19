/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.Map;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public interface Value
extends Term {
    @Override
    default public Term refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        if (termRewriteMap.containsKey(this.toString())) {
            return termRewriteMap.get(this.toString()).copy(this.getParent());
        }
        return this;
    }
}

