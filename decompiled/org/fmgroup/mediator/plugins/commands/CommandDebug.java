/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugins.commands;

import java.io.IOException;
import net.sourceforge.argparse4j.inf.Namespace;
import org.fmgroup.mediator.core.antlr.Parser;
import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.ValidationException;
import org.fmgroup.mediator.language.generated.MediatorLangParser;
import org.fmgroup.mediator.plugin.command.Command;
import org.fmgroup.mediator.plugins.scheduler.Scheduler;

public class CommandDebug
implements Command {
    @Override
    public String getCommandName() {
        return "debug";
    }

    @Override
    public void run(Namespace args) throws IOException {
        MediatorLangParser parser = Parser.getParserFromFile("resources/models/test/newconn.med");
        try {
            Program prog = new Program().fromContext(parser.prog(), null);
            System.out.println(prog.toString());
            org.fmgroup.mediator.language.entity.system.System t = prog.getSystems().get("t");
            System.out.println(Scheduler.Schedule(t).toString());
        }
        catch (ValidationException e) {
            e.printStackTrace();
        }
    }

    @Override
    public String getName() {
        return "debug";
    }

    @Override
    public String getVersion() {
        return "0.1";
    }

    @Override
    public String getDescription() {
        return "debug";
    }

    @Override
    public boolean isBuiltIn() {
        return true;
    }
}

