/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.automaton;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.common.UtilCode;
import org.fmgroup.mediator.language.Meta;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Template;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.EntityInterface;
import org.fmgroup.mediator.language.entity.PortDeclaration;
import org.fmgroup.mediator.language.entity.automaton.Transition;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.property.PropertyCollection;
import org.fmgroup.mediator.language.scope.DeclarationCollection;
import org.fmgroup.mediator.language.scope.Scope;
import org.fmgroup.mediator.language.scope.VariableDeclaration;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class Automaton
implements Entity,
Scope,
Templated {
    private RawElement parent = null;
    private Template template = null;
    private EntityInterface entityInterface = null;
    private VariableDeclarationCollection localVars = new VariableDeclarationCollection().setParent(this);
    private List<Transition> transitions = new ArrayList<Transition>();
    private PropertyCollection properties = null;
    private String name;
    private Meta meta = null;

    public PropertyCollection getProperties() {
        return this.properties;
    }

    public Automaton setProperties(PropertyCollection properties) {
        this.properties = properties;
        properties.setParent(this);
        return this;
    }

    public Meta getMeta() {
        return this.meta;
    }

    public Automaton setMeta(Meta meta) {
        this.meta = meta;
        meta.setParent(this);
        return this;
    }

    public EntityInterface getEntityInterface() {
        return this.entityInterface;
    }

    public Automaton setEntityInterface(EntityInterface entityInterface) {
        this.entityInterface = entityInterface;
        entityInterface.setParent(this);
        return this;
    }

    public VariableDeclarationCollection getLocalVars() {
        return this.localVars;
    }

    public Automaton setLocalVars(VariableDeclarationCollection localVars) {
        this.localVars = localVars;
        localVars.setParent(this);
        return this;
    }

    public List<Transition> getTransitions() {
        return this.transitions;
    }

    public Automaton addTransition(Transition transition) {
        this.transitions.add(transition);
        transition.setParent(this);
        return this;
    }

    public Automaton setTransitions(List<Transition> transitions) {
        this.transitions = new ArrayList<Transition>();
        transitions.forEach(this::addTransition);
        return this;
    }

    public Transition getTransition(int i) {
        return this.transitions.get(i);
    }

    @Override
    public String getName() {
        return this.name;
    }

    public Automaton setName(String name) {
        this.name = name;
        return this;
    }

    @Override
    public Automaton fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.AutomatonContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "AutomatonContext", context.toString());
        }
        MediatorLangParser.AutomatonContext automaton = (MediatorLangParser.AutomatonContext)context;
        this.setParent(parent);
        this.setName(((MediatorLangParser.AutomatonContext)context).name.getText());
        if (((MediatorLangParser.AutomatonContext)context).template() != null) {
            this.setTemplate(new Template().fromContext(((MediatorLangParser.AutomatonContext)context).template(), this));
        }
        this.setEntityInterface(new EntityInterface().fromContext(((MediatorLangParser.AutomatonContext)context).entityInterface(), this));
        for (MediatorLangParser.VariableSegmentContext vsc : automaton.variableSegment()) {
            for (MediatorLangParser.LocalVariableDefContext lvc : vsc.localVariableDef()) {
                this.localVars.addDeclaration(new VariableDeclaration().fromContext(lvc, this));
            }
        }
        for (MediatorLangParser.TransitionSegmentContext tsc : automaton.transitionSegment()) {
            for (MediatorLangParser.TransitionContext tc : tsc.transition()) {
                this.transitions.add(Transition.parse(tc, this));
            }
        }
        if (((MediatorLangParser.AutomatonContext)context).meta() != null) {
            this.setMeta(new Meta().fromContext(((MediatorLangParser.AutomatonContext)context).meta(), this));
        }
        if (((MediatorLangParser.AutomatonContext)context).propertySegment().size() > 0) {
            this.setProperties(new PropertyCollection());
            for (MediatorLangParser.PropertySegmentContext pseg : ((MediatorLangParser.AutomatonContext)context).propertySegment()) {
                this.getProperties().fromContext(pseg, this);
            }
        }
        return this;
    }

    @Override
    public Automaton copy(RawElement parent) throws ValidationException {
        Automaton a = new Automaton();
        a.setParent(parent);
        a.setName(this.getName());
        if (this.getTemplate() != null) {
            a.setTemplate(this.getTemplate().copy(a));
        }
        a.setEntityInterface(this.getEntityInterface().copy(a));
        a.setLocalVars(this.getLocalVars().copy(a));
        ArrayList<Transition> transitions = new ArrayList<Transition>();
        for (Transition t : this.getTransitions()) {
            transitions.add((Transition)t.copy(a));
        }
        a.setTransitions(transitions);
        if (this.getProperties() != null) {
            a.setProperties(this.getProperties().copy(a));
        }
        return a;
    }

    public String toString() {
        String template;
        String string = template = this.template == null ? "" : this.template.toString();
        if (template.length() > 0) {
            template = "<" + template + "> ";
        }
        String rel = String.format("automaton %s%s (%s) {\n", template, this.name, this.entityInterface.toString());
        rel = rel + UtilCode.addIndent(this.localVars.toString(), 1);
        if (this.transitions.size() > 0) {
            rel = rel + UtilCode.addIndent(String.format("transitions {\n%s}\n", UtilCode.addIndent(this.getTransitions().stream().map(transition -> transition.toString() + "\n").collect(Collectors.joining("")), 1)), 1);
        }
        if (this.properties != null) {
            rel = rel + UtilCode.addIndent(this.properties.toString(), 1);
        }
        rel = rel + "}";
        if (this.getMeta() != null) {
            rel = rel + " " + this.getMeta().toString();
        }
        return rel;
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public Automaton setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public EntityInterface getInterface() {
        return this.entityInterface;
    }

    @Override
    public Template getTemplate() {
        if (this.template == null) {
            return new Template().setParent(this);
        }
        return this.template;
    }

    @Override
    public Automaton refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        for (PortDeclaration portdecl : this.getEntityInterface().getDeclarationList()) {
            portdecl.setType(portdecl.getType().refactor(typeRewriteMap, termRewriteMap));
        }
        for (VariableDeclaration vardecl : this.getLocalVars().getDeclarationList()) {
            vardecl.setType(vardecl.getType().refactor(typeRewriteMap, termRewriteMap));
        }
        for (Transition t : this.getTransitions()) {
            t.refactor(typeRewriteMap, termRewriteMap, this);
        }
        return this;
    }

    @Override
    public Automaton setTemplate(Template template) {
        this.template = template;
        if (template != null) {
            template.setParent(this);
        }
        return this;
    }

    @Override
    public List<DeclarationCollection> getDeclarations() {
        ArrayList<DeclarationCollection> result = new ArrayList<DeclarationCollection>();
        if (this.template != null) {
            result.add(this.template);
        }
        if (this.entityInterface != null) {
            result.add(this.entityInterface);
        }
        if (this.localVars != null) {
            result.add(this.localVars);
        }
        return result;
    }
}

