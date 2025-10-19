/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.term;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.Token;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.scope.Declaration;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.term.Value;
import org.fmgroup.mediator.language.type.Type;

public class IdValue
implements Value {
    private RawElement parent = null;
    private List<String> scopeIdentifiers = new ArrayList<String>();
    private String identifier = null;
    private Declaration reference = null;

    @Override
    public Type getType() throws ValidationException {
        if (this.reference instanceof VariableDeclaration) {
            return ((VariableDeclaration)this.reference).getType().extractRawType();
        }
        throw ValidationException.UnderDevelopment();
    }

    @Override
    public int getPrecedence() {
        return 14;
    }

    @Override
    public IdValue fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (context instanceof MediatorLangParser.IdValueContext) {
            context = ((MediatorLangParser.IdValueContext)context).scopedID();
        }
        if (!(context instanceof MediatorLangParser.ScopedIDContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "(Scope)IdValueContext", context.getClass().toString());
        }
        this.setParent(parent);
        this.setScopeIdentifiers(((MediatorLangParser.ScopedIDContext)context).scopes.stream().map(Token::getText).collect(Collectors.toList()));
        this.setIdentifier(((MediatorLangParser.ScopedIDContext)context).identifier.getText());
        return this;
    }

    public List<String> getScopeIdentifiers() {
        return this.scopeIdentifiers;
    }

    public IdValue setScopeIdentifiers(List<String> scopeIdentifiers) {
        this.scopeIdentifiers = scopeIdentifiers;
        return this;
    }

    public String getIdentifier() {
        return this.identifier;
    }

    public IdValue setIdentifier(String identifier) throws ValidationException {
        this.identifier = identifier;
        if (this.scopeIdentifiers.size() == 0) {
            List<Scope> scopes = this.getScopes();
            for (Scope scope : scopes) {
                if (scope.getVariable(this) != null) {
                    this.reference = scope.getVariable(this);
                    break;
                }
                if (scope.getEnumFromIdentifier(this.identifier) == null) continue;
                this.reference = scope.getEnumFromIdentifier(this.identifier);
                break;
            }
        }
        if (this.reference == null) {
            throw ValidationException.UnknownIdentifier(this.toString(), "variable");
        }
        return this;
    }

    public String toString() {
        return String.join((CharSequence)".", this.scopeIdentifiers) + (this.scopeIdentifiers.size() > 0 ? "." : "") + this.identifier;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public IdValue setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public IdValue copy(RawElement parent) throws ValidationException {
        IdValue niv = new IdValue();
        niv.setParent(parent);
        niv.setScopeIdentifiers(new ArrayList<String>(this.scopeIdentifiers));
        niv.setIdentifier(this.identifier);
        return niv;
    }
}

