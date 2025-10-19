/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.PrintWriter;
import java.io.Writer;
import org.ini4j.Config;
import org.ini4j.spi.AbstractFormatter;
import org.ini4j.spi.OptionsHandler;
import org.ini4j.spi.ServiceFinder;

public class OptionsFormatter
extends AbstractFormatter
implements OptionsHandler {
    public static OptionsFormatter newInstance(Writer out, Config config) {
        OptionsFormatter instance = OptionsFormatter.newInstance();
        instance.setOutput(out instanceof PrintWriter ? (PrintWriter)out : new PrintWriter(out));
        instance.setConfig(config);
        return instance;
    }

    public void endOptions() {
        this.getOutput().flush();
    }

    public void startOptions() {
    }

    private static OptionsFormatter newInstance() {
        return ServiceFinder.findService(OptionsFormatter.class);
    }
}

