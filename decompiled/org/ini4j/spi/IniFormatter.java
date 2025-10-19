/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.PrintWriter;
import java.io.Writer;
import org.ini4j.Config;
import org.ini4j.spi.AbstractFormatter;
import org.ini4j.spi.IniHandler;
import org.ini4j.spi.ServiceFinder;

public class IniFormatter
extends AbstractFormatter
implements IniHandler {
    public static IniFormatter newInstance(Writer out, Config config) {
        IniFormatter instance = IniFormatter.newInstance();
        instance.setOutput(out instanceof PrintWriter ? (PrintWriter)out : new PrintWriter(out));
        instance.setConfig(config);
        return instance;
    }

    public void endIni() {
        this.getOutput().flush();
    }

    public void endSection() {
        this.getOutput().print(this.getConfig().getLineSeparator());
    }

    public void startIni() {
    }

    public void startSection(String sectionName) {
        this.setHeader(false);
        if (!this.getConfig().isGlobalSection() || !sectionName.equals(this.getConfig().getGlobalSectionName())) {
            this.getOutput().print('[');
            this.getOutput().print(this.escapeKey(sectionName));
            this.getOutput().print(']');
            this.getOutput().print(this.getConfig().getLineSeparator());
        }
    }

    private static IniFormatter newInstance() {
        return ServiceFinder.findService(IniFormatter.class);
    }
}

