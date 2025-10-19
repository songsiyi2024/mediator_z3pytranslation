/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.List;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.scope.Scope;

public interface Declaration
extends RawElement {
    default public int size() {
        return this.getIdentifiers().size();
    }

    default public String getIdentifier(int index) {
        return this.getIdentifiers().get(index);
    }

    default public Declaration addIdentifier(String identifier) throws ValidationException {
        Scope currScope = this.getCurrentScope();
        if (currScope.existsDeclaration(identifier) || this.containsIdentifier(identifier)) {
            throw ValidationException.DumplicatedIdentifier(identifier, "symbol");
        }
        this.getIdentifiers().add(identifier);
        return this;
    }

    public List<String> getIdentifiers();

    default public boolean containsIdentifier(String identifier) {
        for (int i = 0; i < this.size(); ++i) {
            if (!this.getIdentifier(i).equals(identifier)) continue;
            return true;
        }
        return false;
    }
}

