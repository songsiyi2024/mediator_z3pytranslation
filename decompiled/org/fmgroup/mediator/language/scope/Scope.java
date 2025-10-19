/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.scope;

import java.util.ArrayList;
import java.util.List;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortDeclaration;
import org.fmgroup.mediator.language.entity.system.ComponentDeclaration;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.TypeDeclaration;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.term.IdValue;
import org.fmgroup.mediator.language.type.termType.EnumType;
import org.fmgroup.mediator.language.type.termType.IdType;

public interface Scope
extends RawElement {
    public List<DeclarationCollection> getDeclarations();

    default public boolean existsDeclaration(String identifier) {
        return this.getDeclaration(null, identifier) != null;
    }

    default public Declaration getDeclaration(List<String> scopeIdentifiers, String identifier) {
        if (scopeIdentifiers == null || scopeIdentifiers.size() == 0) {
            for (DeclarationCollection declarationCollection : this.getDeclarations()) {
                if (declarationCollection.getDeclaration(identifier) == null) continue;
                return declarationCollection.getDeclaration(identifier);
            }
        }
        return null;
    }

    default public TypeDeclaration getType(IdType typeIdentifier) {
        Declaration decl = this.getDeclaration(typeIdentifier.getScopeIdentifiers(), typeIdentifier.getIdentifier());
        if (decl instanceof TypeDeclaration) {
            return (TypeDeclaration)decl;
        }
        return null;
    }

    default public TypeDeclaration getType(String identifier) {
        Declaration decl = this.getDeclaration(null, identifier);
        if (decl instanceof TypeDeclaration) {
            return (TypeDeclaration)decl;
        }
        return null;
    }

    default public VariableDeclaration getVariable(IdValue variableIdentifier) {
        Declaration decl = this.getDeclaration(variableIdentifier.getScopeIdentifiers(), variableIdentifier.getIdentifier());
        if (decl instanceof VariableDeclaration) {
            return (VariableDeclaration)decl;
        }
        return null;
    }

    default public VariableDeclaration getVariable(String identifier) {
        Declaration decl = this.getDeclaration(null, identifier);
        if (decl instanceof VariableDeclaration) {
            return (VariableDeclaration)decl;
        }
        return null;
    }

    default public PortDeclaration getPort(String identifier) throws ValidationException {
        Declaration decl = this.getDeclaration(null, identifier);
        if (decl instanceof PortDeclaration) {
            return (PortDeclaration)decl;
        }
        throw ValidationException.UnknownIdentifier(identifier, "port");
    }

    default public ComponentDeclaration getComponent(String identifier) {
        Declaration decl = this.getDeclaration(null, identifier);
        if (decl instanceof ComponentDeclaration) {
            return (ComponentDeclaration)decl;
        }
        return null;
    }

    default public List<TypeDeclaration> getEnumTypes() {
        ArrayList<TypeDeclaration> result = new ArrayList<TypeDeclaration>();
        for (DeclarationCollection coll : this.getDeclarations()) {
            for (Object decl : coll.getDeclarationList()) {
                if (!(decl instanceof TypeDeclaration) || !(((TypeDeclaration)decl).getType() instanceof EnumType)) continue;
                result.add((TypeDeclaration)decl);
            }
        }
        return result;
    }

    default public TypeDeclaration getEnumFromIdentifier(String identifier) {
        for (TypeDeclaration typedecl : this.getEnumTypes()) {
            if (!(typedecl.getType() instanceof EnumType) || !((EnumType)typedecl.getType()).getItems().contains(identifier)) continue;
            return typedecl;
        }
        return null;
    }
}

