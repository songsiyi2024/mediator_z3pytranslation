/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.language.entity.system;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import org.antlr.v4.runtime.ParserRuleContext;
import org.fmgroup.mediator.core.antlr.Parser;
import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.language.Templated;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.entity.PortIdentifier;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.entity.system.Connection;
import org.fmgroup.mediator.language.entity.system.Options;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.language.term.IntValue;
import org.fmgroup.mediator.language.term.Term;
import org.fmgroup.mediator.language.type.Type;
import org.fmgroup.mediator.language.type.paramType.AbstractType;

public class BasicConnection
extends Connection {
    private Options options = null;
    private List<PortIdentifier> inPorts = new ArrayList<PortIdentifier>();
    private List<PortIdentifier> outPorts = new ArrayList<PortIdentifier>();
    private Automaton provider = null;
    private Term capacity = null;
    private Type type = new AbstractType();

    @Override
    public BasicConnection fromContext(ParserRuleContext context, RawElement parent) throws ValidationException {
        PortIdentifier portId;
        if (!(context instanceof MediatorLangParser.BasicConnectionContext)) {
            throw ValidationException.IncompatibleContextType(this.getClass(), "BasicConnectionContext", context.toString());
        }
        this.setParent(parent);
        for (MediatorLangParser.PortIdentifierContext portContext : ((MediatorLangParser.BasicConnectionContext)context).inPorts.portIdentifier()) {
            portId = new PortIdentifier().fromContext(portContext, this);
            this.inPorts.add(portId);
            this.portIdentifiers.add(portId);
        }
        for (MediatorLangParser.PortIdentifierContext portContext : ((MediatorLangParser.BasicConnectionContext)context).outPorts.portIdentifier()) {
            portId = new PortIdentifier().fromContext(portContext, this);
            this.outPorts.add(portId);
            this.portIdentifiers.add(portId);
        }
        this.options = new Options().fromContext(((MediatorLangParser.BasicConnectionContext)context).connectionOptions(), this);
        this.buildProvider();
        return this;
    }

    private void buildProvider() throws ValidationException {
        String ports = "";
        String variables = "";
        String transitions = "";
        String extTransitions = "";
        Stream<Integer> inputPortIndexStream = Stream.iterate(0, item -> item + 1).limit(this.inPorts.size());
        Stream<Integer> outputPortIndexStream = Stream.iterate(0, item -> item + 1).limit(this.outPorts.size());
        ports = ports + String.join((CharSequence)",", inputPortIndexStream.map(i -> String.format("_AG_PI%d", i)).collect(Collectors.toList()));
        ports = ports + ": in T, ";
        ports = ports + String.join((CharSequence)",", outputPortIndexStream.map(i -> String.format("_AG_PO%d", i)).collect(Collectors.toList()));
        ports = ports + ": out T";
        if (this.options.contains("async")) {
            variables = String.format("buf  : (T | NULL) [bufsize] init null;front: int 0 .. bufsize - 1 init 0;rear : int 0 .. bufsize - 1 init 0;", new Object[0]);
        }
        if (this.options.contains("async")) {
            int j;
            this.capacity = this.options.get("capacity");
            for (int i2 = 0; i2 < this.inPorts.size(); ++i2) {
                transitions = transitions + String.format("(_AG_PI%d.reqRead != (buf[rear] == null)) -> _AG_PI%d.reqRead = buf[rear] == null;", i2, i2);
                extTransitions = extTransitions + String.format("true -> {sync _AG_PI%d;buf[rear] = _AG_PI%d.value;rear = (rear + 1) %% bufsize;} ", i2, i2);
            }
            for (j = 0; j < this.outPorts.size(); ++j) {
                transitions = transitions + String.format("(_AG_PO%d.reqWrite != (buf[front] != null)) -> _AG_PI%d.reqWrite = buf[front] != null;", j, j);
            }
            if (this.options.contains("unicast")) {
                for (j = 0; j < this.outPorts.size(); ++j) {
                    extTransitions = extTransitions + String.format("true -> {_AG_PO%d.value = buf[front];front = (front + 1) %% bufsize;sync _AG_PO%d;} ", j, j);
                }
            } else {
                String tmpExtTrans = "";
                for (int j2 = 0; j2 < this.outPorts.size(); ++j2) {
                    tmpExtTrans = tmpExtTrans + String.format("_AG_PO%d.value = buf[front];sync _AG_PO%d;", j2, j2);
                }
                tmpExtTrans = tmpExtTrans + "front = (front + 1) % bufsize;";
                extTransitions = extTransitions + String.format("true -> {%s}", tmpExtTrans);
            }
        } else {
            int j;
            int i3;
            this.capacity = new IntValue().setParent(this).setValue(0);
            for (i3 = 0; i3 < this.inPorts.size(); ++i3) {
                for (j = 0; j < this.outPorts.size(); ++j) {
                    transitions = transitions + String.format("(_AG_PO%d.reqWrite != _AG_PI%d.reqWrite) -> _AG_PO%d.reqWrite = _AG_PI%d.reqWrite;", j, i3, j, i3);
                }
            }
            if (this.options.contains("unicast")) {
                for (i3 = 0; i3 < this.inPorts.size(); ++i3) {
                    for (j = 0; j < this.outPorts.size(); ++j) {
                        transitions = transitions + String.format("(_AG_PI%d.reqRead != _AG_PO%d.reqRead) -> _AG_PI%d.reqRead = _AG_PO%d.reqRead;", i3, j, i3, j);
                        extTransitions = extTransitions + String.format("true -> {sync _AG_PI%d;_AG_PO%d.value = _AG_PI%d.value;sync _AG_PO%d;}", i3, j, i3, j);
                    }
                }
            } else {
                for (i3 = 0; i3 < this.inPorts.size(); ++i3) {
                    String sourceCond = String.format("_AG_PI%d.reqRead", i3);
                    String targetCond = "true";
                    String tmpExtTran = String.format("sync _AG_PI%d;", i3);
                    for (int j3 = 0; j3 < this.outPorts.size(); ++j3) {
                        targetCond = String.format("(%s && _AG_PO%d.reqRead)", targetCond, j3);
                        tmpExtTran = tmpExtTran + String.format("_AG_PO%d.value = _AG_PI%d.value; sync _AG_PO%d;", j3, i3, j3);
                    }
                    transitions = transitions + String.format("%s != %s -> %s = %s;", sourceCond, targetCond, sourceCond, targetCond);
                    extTransitions = extTransitions + String.format("true -> {%s}", tmpExtTran);
                }
            }
        }
        String providerText = String.format("automaton <T:type, bufsize:int> CONN(%s) {\n%s%s\n}\n", ports, String.format("variables {%s}", variables), String.format("transitions {%s group {%s}}", transitions, extTransitions));
        try {
            MediatorLangParser.AutomatonContext context = Parser.getParserFromString(providerText).automaton();
            this.provider = new Automaton().fromContext(context, this.getTopScope());
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Override
    public Templated getProvider() {
        return this.provider;
    }

    @Override
    public List<RawElement> getParams() {
        ArrayList<RawElement> params = new ArrayList<RawElement>();
        params.add(this.type);
        params.add(this.capacity);
        return params;
    }

    public String toString() {
        String inp = String.join((CharSequence)",", this.inPorts.stream().map(PortIdentifier::toString).collect(Collectors.toList()));
        if (this.inPorts.size() > 1) {
            inp = "(" + inp + ")";
        }
        String outp = String.join((CharSequence)",", this.outPorts.stream().map(PortIdentifier::toString).collect(Collectors.toList()));
        if (this.outPorts.size() > 1) {
            outp = "(" + outp + ")";
        }
        if (this.options.isEmpty()) {
            return inp + " -> " + outp;
        }
        return String.format("%s --(%s)-> %s", inp, this.options.toString(), outp);
    }
}

