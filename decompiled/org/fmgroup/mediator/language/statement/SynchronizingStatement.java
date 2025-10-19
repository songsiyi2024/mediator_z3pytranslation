/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.statement;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortIdentifier;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.statement.Statement;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;

public class SynchronizingStatement
implements Statement {
    private RawElement parent = null;
    private List<PortIdentifier> synchronizedPorts = new ArrayList<PortIdentifier>();

    public List<PortIdentifier> getSynchronizedPorts() {
        return this.synchronizedPorts;
    }

    public SynchronizingStatement setSynchronizedPorts(List<PortIdentifier> synchronizedPorts) {
        this.synchronizedPorts = new ArrayList<PortIdentifier>();
        synchronizedPorts.forEach(this::addSyncronizedPort);
        return this;
    }

    public PortIdentifier getSynchronizedPort(int i) {
        return this.synchronizedPorts.get(i);
    }

    public SynchronizingStatement addSyncronizedPort(PortIdentifier synchronizedPort) {
        this.synchronizedPorts.add(synchronizedPort);
        synchronizedPort.setParent(this);
        return this;
    }

    @Override
    public SynchronizingStatement fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        if (!(context instanceof MediatorLangParser.SynchronizingStatementContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "SynchronizingStatementContext", context.toString());
        }
        this.setParent(parent);
        for (MediatorLangParser.PortIdentifierContext portid : ((MediatorLangParser.SynchronizingStatementContext)context).portIdentifier()) {
            this.addSyncronizedPort(new PortIdentifier().fromContext(portid, this));
        }
        return this;
    }

    public List<SynchronizingStatement> split() throws ValidationException {
        ArrayList<SynchronizingStatement> newStmts = new ArrayList<SynchronizingStatement>();
        for (PortIdentifier port : this.synchronizedPorts) {
            newStmts.add(new SynchronizingStatement().setParent(this.parent).addSyncronizedPort(port));
        }
        return newStmts;
    }

    public boolean equals(Object obj) {
        return this.toString().equals(obj.toString()) && obj instanceof Statement;
    }

    public String toString() {
        assert (this.synchronizedPorts.size() > 0);
        return "sync " + this.synchronizedPorts.stream().map(PortIdentifier::toString).collect(Collectors.joining(", ")) + ";";
    }

    @Override
    public RawElement getParent() {
        return this.parent;
    }

    @Override
    public SynchronizingStatement setParent(RawElement parent) {
        this.parent = parent;
        return this;
    }

    @Override
    public SynchronizingStatement copy(RawElement parent) throws ValidationException {
        SynchronizingStatement nss = new SynchronizingStatement();
        nss.setParent(parent);
        for (PortIdentifier port : this.synchronizedPorts) {
            nss.addSyncronizedPort(port.copy(nss));
        }
        return nss;
    }

    @Override
    public SynchronizingStatement refactor(Map<String, Type> typeRewriteMap, Map<String, Term> termRewriteMap) throws ValidationException {
        ArrayList<PortIdentifier> newPorts = new ArrayList<PortIdentifier>();
        for (PortIdentifier port : this.getSynchronizedPorts()) {
            if (termRewriteMap.containsKey(port + ".value")) {
                String newPortName = termRewriteMap.get(port + ".value").toString().replace("_value", "");
                newPorts.add(new PortIdentifier().setParent(this.parent).setPortName(newPortName, true));
                continue;
            }
            newPorts.add(port);
        }
        this.setSynchronizedPorts(newPorts);
        return this;
    }
}

