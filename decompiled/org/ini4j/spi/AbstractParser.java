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
import org.ini4j.spi.EscapeTool;
import org.ini4j.spi.HandlerBase;
import org.ini4j.spi.IniSource;

abstract class AbstractParser {
    private final String _comments;
    private Config _config = Config.getGlobal();
    private final String _operators;

    protected AbstractParser(String operators, String comments) {
        this._operators = operators;
        this._comments = comments;
    }

    protected Config getConfig() {
        return this._config;
    }

    protected void setConfig(Config value) {
        this._config = value;
    }

    protected void parseError(String line, int lineNumber) throws InvalidFileFormatException {
        throw new InvalidFileFormatException("parse error (at line: " + lineNumber + "): " + line);
    }

    IniSource newIniSource(InputStream input, HandlerBase handler) {
        return new IniSource(input, handler, this._comments, this.getConfig());
    }

    IniSource newIniSource(Reader input, HandlerBase handler) {
        return new IniSource(input, handler, this._comments, this.getConfig());
    }

    IniSource newIniSource(URL input, HandlerBase handler) throws IOException {
        return new IniSource(input, handler, this._comments, this.getConfig());
    }

    void parseOptionLine(String line, HandlerBase handler, int lineNumber) throws InvalidFileFormatException {
        int idx = this.indexOfOperator(line);
        String name = null;
        String value = null;
        if (idx < 0) {
            if (this.getConfig().isEmptyOption()) {
                name = line;
            } else {
                this.parseError(line, lineNumber);
            }
        } else {
            name = this.unescapeKey(line.substring(0, idx)).trim();
            value = this.unescapeValue(line.substring(idx + 1)).trim();
        }
        if (name.length() == 0) {
            this.parseError(line, lineNumber);
        }
        if (this.getConfig().isLowerCaseOption()) {
            name = name.toLowerCase(Locale.getDefault());
        }
        handler.handleOption(name, value);
    }

    String unescapeKey(String line) {
        return this.getConfig().isEscape() ? EscapeTool.getInstance().unescape(line) : line;
    }

    String unescapeValue(String line) {
        return this.getConfig().isEscape() && !this.getConfig().isEscapeKeyOnly() ? EscapeTool.getInstance().unescape(line) : line;
    }

    private int indexOfOperator(String line) {
        int idx = -1;
        block0: for (char c : this._operators.toCharArray()) {
            int index = line.indexOf(c);
            while (index >= 0) {
                if (!(index < 0 || index != 0 && line.charAt(index - 1) == '\\' || idx != -1 && index >= idx)) {
                    idx = index;
                    continue block0;
                }
                index = index == line.length() - 1 ? -1 : line.indexOf(c, index + 1);
            }
        }
        return idx;
    }
}

