/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.Collection;
import java.util.List;
import java.util.stream.Collectors;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.scope.Declaration;

public interface DeclarationCollection<T extends Declaration>
extends RawElement {
    public List<T> getDeclarationList();

    public DeclarationCollection<T> setDeclarationList(List<T> var1);

    public DeclarationCollection<T> addDeclaration(T var1);

    default public T getDeclaration(int index) {
        List<T> declarations = this.getDeclarationList();
        int offset = index;
        for (Declaration declaration : declarations) {
            if (declaration.size() > index) {
                return (T)declaration;
            }
            index -= declaration.size();
        }
        return null;
    }

    default public Declaration getDeclaration(String identifier) {
        List result = this.getDeclarationList().stream().filter(declaration -> declaration.containsIdentifier(identifier)).collect(Collectors.toList());
        if (!1.$assertionsDisabled && result.size() > 1) {
            throw new AssertionError();
        }
        if (result.size() == 1) {
            return (Declaration)result.get(0);
        }
        return null;
    }

    default public String getDeclarationIdentifier(int index) {
        List<T> declarations = this.getDeclarationList();
        int offset = index;
        for (Declaration declaration : declarations) {
            if (declaration.size() > index) {
                return declaration.getIdentifier(index);
            }
            index -= declaration.size();
        }
        return null;
    }

    default public int getDeclarationIndex(String identifier) {
        List identifiers = this.getDeclarationList().stream().map(Declaration::getIdentifiers).flatMap(Collection::stream).collect(Collectors.toList());
        for (int i = 0; i < identifiers.size(); ++i) {
            if (!((String)identifiers.get(i)).equals(identifier)) continue;
            return i;
        }
        return -1;
    }

    static {
        if (1.$assertionsDisabled) {
            // empty if block
        }
    }
}

