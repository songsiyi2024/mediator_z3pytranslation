/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugin.command;

import java.io.IOException;
import net.sourceforge.argparse4j.ArgumentParsers;
import net.sourceforge.argparse4j.inf.ArgumentParser;
import net.sourceforge.argparse4j.inf.Namespace;
import org.fmgroup.mediator.plugin.Plugin;

public interface Command
extends Plugin {
    public String getCommandName();

    default public ArgumentParser getParamsParser() {
        ArgumentParser parser = ArgumentParsers.newFor("command").build().description("you need to override getParamsParser in Command to customize this line.");
        return parser;
    }

    public void run(Namespace var1) throws IOException;
}

