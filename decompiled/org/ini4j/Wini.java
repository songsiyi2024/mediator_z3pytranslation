/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.Reader;
import java.net.URL;
import org.ini4j.Config;
import org.ini4j.Ini;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.spi.WinEscapeTool;

public class Wini
extends Ini {
    private static final long serialVersionUID = -2781377824232440728L;
    public static final char PATH_SEPARATOR = '\\';

    public Wini() {
        Config cfg = Config.getGlobal().clone();
        cfg.setEscape(false);
        cfg.setEscapeNewline(false);
        cfg.setGlobalSection(true);
        cfg.setEmptyOption(true);
        cfg.setMultiOption(false);
        cfg.setPathSeparator('\\');
        this.setConfig(cfg);
    }

    public Wini(File input) throws IOException, InvalidFileFormatException {
        this();
        this.setFile(input);
        this.load();
    }

    public Wini(URL input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Wini(InputStream input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Wini(Reader input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public String escape(String value) {
        return WinEscapeTool.getInstance().escape(value);
    }

    public String unescape(String value) {
        return WinEscapeTool.getInstance().unescape(value);
    }
}

