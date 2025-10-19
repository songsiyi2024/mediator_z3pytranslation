/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity;

import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.entity.EntityInterface;
import org.fmgroup.mediator.language.scope.Scope;

public interface Entity
extends RawElement,
Scope,
Templated {
    public EntityInterface getInterface();

    public String getName();
}

