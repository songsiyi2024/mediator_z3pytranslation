/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.scheduler;

public class TopoGraphVertice<T> {
    public T element = null;

    public TopoGraphVertice(T element) {
        this.element = element;
    }

    public TopoGraphVertice() {
    }

    public String toString() {
        if (this.element == null) {
            return String.format("VirtualNode (%d)", this.hashCode());
        }
        return this.element.toString();
    }
}

