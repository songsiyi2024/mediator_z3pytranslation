/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language;

import java.util.ArrayList;
import java.util.List;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.scope.Scope;

public interface RawElement {
    public static Program getRoot(RawElement e) throws ValidationException {
        while (e != null) {
            if (e instanceof Program) {
                return (Program)e;
            }
            e = e.getParent();
        }
        return null;
    }

    default public RawElement fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }

    public RawElement getParent();

    public RawElement setParent(RawElement var1);

    default public RawElement copy(RawElement parent) throws ValidationException {
        throw ValidationException.UnderDevelopment();
    }

    default public RawElement copy() throws ValidationException {
        return this.copy(this.getParent());
    }

    default public List<Scope> getScopes() throws ValidationException {
        ArrayList<Scope> result = new ArrayList<Scope>();
        for (RawElement p = this; p != null; p = p.getParent()) {
            if (p instanceof Scope) {
                result.add((Scope)p);
            }
            if (p instanceof Program) break;
        }
        return result;
    }

    default public Scope getTopScope() throws ValidationException {
        List<Scope> scopes = this.getScopes();
        return scopes.get(scopes.size() - 1);
    }

    default public Scope getCurrentScope() throws ValidationException {
        return this.getScopes().get(0);
    }
}

