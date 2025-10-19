/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.scheduler;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.fmgroup.mediator.plugins.scheduler.TopoGraphVertice;

public class TopoGraph<Tvertice> {
    public Set<TopoGraphVertice> vertices = new HashSet<TopoGraphVertice>();
    public Map<TopoGraphVertice, List<TopoGraphVertice>> edges = new HashMap<TopoGraphVertice, List<TopoGraphVertice>>();

    public TopoGraphVertice createNode(Tvertice value) {
        TopoGraphVertice<Tvertice> newTopoGraphVertice = new TopoGraphVertice<Tvertice>(value);
        this.vertices.add(newTopoGraphVertice);
        return newTopoGraphVertice;
    }

    public TopoGraphVertice createVirtualNode() {
        TopoGraphVertice v = new TopoGraphVertice();
        this.vertices.add(v);
        return v;
    }

    public TopoGraphVertice getNode(Tvertice value) {
        for (TopoGraphVertice v : this.vertices) {
            if (v.element == null || !v.element.equals(value)) continue;
            return v;
        }
        return null;
    }

    public TopoGraphVertice getOrCreateNode(Tvertice value) {
        if (this.getNode(value) == null) {
            return this.createNode(value);
        }
        return this.getNode(value);
    }

    public void connect(TopoGraphVertice from, TopoGraphVertice to) {
        if (!this.edges.containsKey(from)) {
            this.edges.put(from, new ArrayList());
        }
        this.edges.get(from).add(to);
    }

    public int countInEdges(TopoGraphVertice v) {
        int count = 0;
        for (TopoGraphVertice from : this.edges.keySet()) {
            if (!this.edges.get(from).contains(v)) continue;
            ++count;
        }
        return count;
    }

    public int countOutEdges(TopoGraphVertice v) {
        if (!this.edges.containsKey(v)) {
            return 0;
        }
        return this.edges.get(v).size();
    }

    public List<Tvertice> TopologySort() {
        HashMap<TopoGraphVertice, Integer> inCount = new HashMap<TopoGraphVertice, Integer>();
        for (TopoGraphVertice v : this.vertices) {
            inCount.put(v, this.countInEdges(v));
        }
        ArrayList result = new ArrayList();
        while (this.vertices.size() > 0) {
            boolean allocated = false;
            for (TopoGraphVertice vt : inCount.keySet()) {
                if ((Integer)inCount.get(vt) != 0) continue;
                this.vertices.remove(vt);
                inCount.remove(vt);
                if (this.edges.containsKey(vt)) {
                    for (TopoGraphVertice next : this.edges.get(vt)) {
                        inCount.put(next, (Integer)inCount.get(next) - 1);
                    }
                    this.edges.remove(vt);
                }
                if (vt.element != null) {
                    result.add(vt.element);
                }
                allocated = true;
                break;
            }
            if (allocated) continue;
            return null;
        }
        return result;
    }
}

