/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.List;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortIdentifier;
import org.fmgroup.mediator.language.entity.system.Connection;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.type.paramType.TemplateType;

public class CustomConnection
extends Connection {
    private TemplateType type;

    public TemplateType getType() {
        return this.type;
    }

    public CustomConnection setType(TemplateType type) {
        this.type = type;
        type.setParent(this);
        return this;
    }

    @Override
    public CustomConnection fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.ConnectionDeclContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "ConnectionDeclContext", context.getClass().toString());
        }
        this.setParent(parent);
        this.setType(new TemplateType().fromContext(((MediatorLangParser.CustomConnectionContext)context).type(), this));
        for (MediatorLangParser.PortIdentifierContext portid : ((MediatorLangParser.CustomConnectionContext)context).portIdentifier()) {
            this.addPortIdentifier(new PortIdentifier().fromContext(portid, this));
        }
        return this;
    }

    public String toString() {
        return String.format("%s(%s)", this.type.toString(), this.portIdentifiers.stream().map(Object::toString).collect(Collectors.joining(", ")));
    }

    @Override
    public Templated getProvider() {
        return this.getType().getProvider();
    }

    @Override
    public List<RawElement> getParams() {
        return this.getType().getParams();
    }
}

