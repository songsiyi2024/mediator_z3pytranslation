/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.core.antlr;

import java.io.ByteArrayInputStream;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.LinkOption;
import java.nio.file.Paths;
import java.util.ArrayList;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.CharStreams;
import org.antlr.v4.runtime.CommonTokenStream;
import org.fmgroup.mediator.common.ToolInfo;
import org.fmgroup.mediator.language.generated.MediatorLangLexer;
import org.fmgroup.mediator.language.generated.MediatorLangParser;

public class Parser {
    public static MediatorLangParser getParserFromString(String content) throws IOException {
        ByteArrayInputStream is = new ByteArrayInputStream(content.getBytes());
        return Parser.getParserFromCharStream(CharStreams.fromStream(is));
    }

    public static MediatorLangParser getParserFromFile(String filename) throws IOException {
        ArrayList<String> paths = new ArrayList<String>();
        paths.add(ToolInfo.getSystemLibraryPath());
        paths.add(System.getProperty("user.dir").toString());
        for (String path : paths) {
            if (!Files.exists(Paths.get(path, filename), new LinkOption[0])) continue;
            FileInputStream is = new FileInputStream(Paths.get(path, filename).toFile());
            return Parser.getParserFromCharStream(CharStreams.fromStream(is));
        }
        throw new FileNotFoundException(String.format("cannot locate %s in all paths", filename));
    }

    public static MediatorLangParser getParserFromCharStream(CharStream cs) {
        MediatorLangLexer lexer = new MediatorLangLexer(cs);
        CommonTokenStream ts = new CommonTokenStream(lexer);
        MediatorLangParser parser = new MediatorLangParser(ts);
        return parser;
    }
}

