/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Template;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.scope.TypeDeclaration;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public interface Templated
extends RawElement,
Scope {
    public Template getTemplate();

    public Templated setTemplate(Template var1);

    default public Templated resolveTemplate(List<RawElement> params) throws ValidationException {
        if (this.getTemplate().size() != params.size()) {
            throw ValidationException.UnderDevelopment();
        }
        Templated resolved = (Templated)this.copy(this.getParent());
        HashMap<String, Type> typeRewriteMap = new HashMap<String, Type>();
        HashMap<String, Term> termRewriteMap = new HashMap<String, Term>();
        for (int i = 0; i < params.size(); ++i) {
            if (params.get(i) instanceof Type && this.getTemplate().getDeclaration(i) instanceof TypeDeclaration) {
                typeRewriteMap.put(this.getTemplate().getDeclarationIdentifier(i), (Type)params.get(i));
                continue;
            }
            termRewriteMap.put(this.getTemplate().getDeclarationIdentifier(i), (Term)params.get(i));
        }
        resolved.refactor(typeRewriteMap, termRewriteMap);
        resolved.setTemplate(new Template());
        return resolved;
    }

    public Templated refactor(Map<String, Type> var1, Map<String, Term> var2) throws ValidationException;
}

