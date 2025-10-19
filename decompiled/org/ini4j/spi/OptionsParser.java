/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.net.URL;
import org.ini4j.Config;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.spi.AbstractParser;
import org.ini4j.spi.HandlerBase;
import org.ini4j.spi.IniSource;
import org.ini4j.spi.OptionsHandler;
import org.ini4j.spi.ServiceFinder;

public class OptionsParser
extends AbstractParser {
    private static final String COMMENTS = "!#";
    private static final String OPERATORS = ":=";

    public OptionsParser() {
        super(OPERATORS, COMMENTS);
    }

    public static OptionsParser newInstance() {
        return ServiceFinder.findService(OptionsParser.class);
    }

    public static OptionsParser newInstance(Config config) {
        OptionsParser instance = OptionsParser.newInstance();
        instance.setConfig(config);
        return instance;
    }

    public void parse(InputStream input, OptionsHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    public void parse(Reader input, OptionsHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    public void parse(URL input, OptionsHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    private void parse(IniSource source, OptionsHandler handler) throws IOException, InvalidFileFormatException {
        handler.startOptions();
        String line = source.readLine();
        while (line != null) {
            this.parseOptionLine(line, handler, source.getLineNumber());
            line = source.readLine();
        }
        handler.endOptions();
    }
}

