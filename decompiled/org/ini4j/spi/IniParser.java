/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.net.URL;
import java.util.Locale;
import org.ini4j.Config;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.spi.AbstractParser;
import org.ini4j.spi.HandlerBase;
import org.ini4j.spi.IniHandler;
import org.ini4j.spi.IniSource;
import org.ini4j.spi.ServiceFinder;

public class IniParser
extends AbstractParser {
    private static final String COMMENTS = ";#";
    private static final String OPERATORS = ":=";
    static final char SECTION_BEGIN = '[';
    static final char SECTION_END = ']';

    public IniParser() {
        super(OPERATORS, COMMENTS);
    }

    public static IniParser newInstance() {
        return ServiceFinder.findService(IniParser.class);
    }

    public static IniParser newInstance(Config config) {
        IniParser instance = IniParser.newInstance();
        instance.setConfig(config);
        return instance;
    }

    public void parse(InputStream input, IniHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    public void parse(Reader input, IniHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    public void parse(URL input, IniHandler handler) throws IOException, InvalidFileFormatException {
        this.parse(this.newIniSource(input, (HandlerBase)handler), handler);
    }

    private void parse(IniSource source, IniHandler handler) throws IOException, InvalidFileFormatException {
        handler.startIni();
        String sectionName = null;
        String line = source.readLine();
        while (line != null) {
            if (line.charAt(0) == '[') {
                if (sectionName != null) {
                    handler.endSection();
                }
                sectionName = this.parseSectionLine(line, source, handler);
            } else {
                if (sectionName == null) {
                    if (this.getConfig().isGlobalSection()) {
                        sectionName = this.getConfig().getGlobalSectionName();
                        handler.startSection(sectionName);
                    } else {
                        this.parseError(line, source.getLineNumber());
                    }
                }
                this.parseOptionLine(line, handler, source.getLineNumber());
            }
            line = source.readLine();
        }
        if (sectionName != null) {
            handler.endSection();
        }
        handler.endIni();
    }

    private String parseSectionLine(String line, IniSource source, IniHandler handler) throws InvalidFileFormatException {
        String sectionName;
        if (line.charAt(line.length() - 1) != ']') {
            this.parseError(line, source.getLineNumber());
        }
        if ((sectionName = this.unescapeKey(line.substring(1, line.length() - 1).trim())).length() == 0 && !this.getConfig().isUnnamedSection()) {
            this.parseError(line, source.getLineNumber());
        }
        if (this.getConfig().isLowerCaseSection()) {
            sectionName = sectionName.toLowerCase(Locale.getDefault());
        }
        handler.startSection(sectionName);
        return sectionName;
    }
}

