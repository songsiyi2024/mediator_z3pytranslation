/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.type.paramType;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.antlr.v4.runtime.Token;
import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Template;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.CallTerm;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class TemplateType
implements Type {
    private RawElement parent;
    private List<String> libraryPath;
    private String identifier;
    private Templated provider = null;
    private List<RawElement> params = new ArrayList<RawElement>();

    public List<String> getLibraryPath() {
        return this.libraryPath;
    }

    public TemplateType setLibraryPath(List<String> libraryPath) {
        this.libraryPath = libraryPath;
        return this;
    }

    public String getIdentifier() {
        return this.identifier;
    }

    public TemplateType setIdentifier(String identifier) throws ValidationException {
        this.identifier = identifier;
        Program prog = RawElement.getRoot(this);
        Template template = null;
        if (this.libraryPath.size() > 0) {
            throw ValidationException.UnderDevelopment();
        }
        if (this.parent instanceof CallTerm) {
            this.provider = prog.getFunction(this.libraryPath, identifier);
            if (this.provider == null) {
                throw ValidationException.UnknownIdentifier(identifier, "function");
            }
        } else {
            this.provider = prog.getEntity(this.libraryPath, identifier);
            if (this.provider == null) {
                throw ValidationException.UnknownIdentifier(identifier, "entity");
            }
        }
        template = this.provider.getTemplate();
        if (this.provider == null) {
            throw ValidationException.UnknownIdentifier(this.toString(), "Interface");
        }
        if (this.params.size() != (template == null ? 0 : template.getDeclarationList().size())) {
            throw ValidationException.FromMessage("Number of params mismatched.");
        }
        return this;
    }

    public List<RawElement> getParams() {
        return this.params;
    }

    public TemplateType addParam(RawElement param) {
        this.params.add(param);
        param.setParent(this);
        return this;
    }

    public TemplateType setParams(List<RawElement> params) {
        this.params = new ArrayList<RawElement>();
        params.forEach(this::addParam);
        return this;
    }

    public Templated getProvider() {
        return this.provider;
    }

    @Override
    public TemplateType fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        this.setParent(parent);
        if (context instanceof MediatorLangParser.TemplateTypeContext) {
            for (MediatorLangParser.TypeorvalueContext tov : ((MediatorLangParser.TemplateTypeContext)context).typeorvalue()) {
                if (tov.type() == null) {
                    this.params.add(Term.parseValue(tov.value(), this));
                    continue;
                }
                this.params.add(Type.parse(tov.type(), this));
            }
            this.setLibraryPath(((MediatorLangParser.TemplateTypeContext)context).scopedID().scopes.stream().map(Token::getText).collect(Collectors.toList()));
            this.setIdentifier(((MediatorLangParser.TemplateTypeContext)context).scopedID().identifier.getText());
        } else if (context instanceof MediatorLangParser.IdTypeContext) {
            this.setLibraryPath(((MediatorLangParser.IdTypeContext)context).scopedID().scopes.stream().map(Token::getText).collect(Collectors.toList()));
            this.setIdentifier(((MediatorLangParser.IdTypeContext)context).scopedID().identifier.getText());
        } else {
            throw ValidationException.IncompatibleContextType(this.getClass(), "TemplateTypeContext / IdTypeContext", context.getClass().toString());
        }
        return this;
    }

    public String toString() {
        String rel = String.join((CharSequence)".", this.libraryPath);
        if (rel.length() > 0) {
            rel = rel + ".";
        }
        rel = rel + this.identifier;
        if (this.params.size() > 0) {
            rel = rel + "<";
            for (RawElement raw : this.params) {
                if (this.params.indexOf(raw) > 0) {
                    rel = rel + ", ";
                }
                rel = rel + raw.toString();
            }
            rel = rel + ">";
        }
        return rel;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public TemplateType setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public TemplateType copy(RawElement parent) throws ValidationException {
        TemplateType nit = new TemplateType();
        nit.setParent(parent);
        for (RawElement elem : this.params) {
            nit.addParam(elem.copy(nit));
        }
        nit.setLibraryPath(this.getLibraryPath());
        nit.setIdentifier(this.getIdentifier());
        return nit;
    }

    @Override
    public TemplateType refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        return this;
    }

    public Templated getProviderWithNoTemplate() throws ValidationException {
        return this.getProvider().resolveTemplate(this.getParams());
    }
}

