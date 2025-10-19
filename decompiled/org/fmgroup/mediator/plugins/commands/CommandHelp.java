/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.commands;

import net.sourceforge.argparse4j.inf.Namespace;
import org.fmgroup.mediator.plugin.command.Command;

public class CommandHelp
implements Command {
    @Override
    public String getName() {
        return "CommandHelp";
    }

    @Override
    public String getVersion() {
        return "0.0.1";
    }

    @Override
    public String getDescription() {
        return "generate help docs based on existing plugins";
    }

    @Override
    public String getCommandName() {
        return "help";
    }

    @Override
    public void run(Namespace args) {
    }

    @Override
    public boolean isBuiltIn() {
        return true;
    }
}

