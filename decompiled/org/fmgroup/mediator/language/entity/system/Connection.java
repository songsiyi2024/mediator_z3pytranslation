/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.util.ArrayList;
import java.util.List;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortIdentifier;

public abstract class Connection
implements RawElement {
    public RawElement parent;
    public List<PortIdentifier> portIdentifiers = new ArrayList<PortIdentifier>();

    public abstract Templated getProvider();

    public Templated getProviderWithNoTemplate() throws ValidationException {
        return this.getProvider().resolveTemplate(this.getParams());
    }

    public abstract List<RawElement> getParams();

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public RawElement setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    public List<PortIdentifier> getPortIdentifiers() {
        return this.portIdentifiers;
    }

    public Connection setPortIdentifiers(List<PortIdentifier> portIdentifiers) {
        this.portIdentifiers.forEach(this::addPortIdentifier);
        return this;
    }

    public Connection addPortIdentifier(PortIdentifier portIdentifier) {
        this.portIdentifiers.add(portIdentifier);
        portIdentifier.setParent(this);
        return this;
    }
}

