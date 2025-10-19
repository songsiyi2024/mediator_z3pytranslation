/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.PrintWriter;
import org.ini4j.Config;
import org.ini4j.spi.EscapeTool;
import org.ini4j.spi.HandlerBase;

abstract class AbstractFormatter
implements HandlerBase {
    private static final char OPERATOR = '=';
    private static final char COMMENT = '#';
    private static final char SPACE = ' ';
    private Config _config = Config.getGlobal();
    private boolean _header = true;
    private PrintWriter _output;

    AbstractFormatter() {
    }

    public void handleComment(String comment) {
        if (this.getConfig().isComment() && (!this._header || this.getConfig().isHeaderComment()) && comment != null && comment.length() != 0) {
            for (String line : comment.split(this.getConfig().getLineSeparator())) {
                this.getOutput().print('#');
                this.getOutput().print(line);
                this.getOutput().print(this.getConfig().getLineSeparator());
            }
            if (this._header) {
                this.getOutput().print(this.getConfig().getLineSeparator());
            }
        }
        this._header = false;
    }

    public void handleOption(String optionName, String optionValue) {
        if (this.getConfig().isStrictOperator()) {
            if (this.getConfig().isEmptyOption() || optionValue != null) {
                this.getOutput().print(this.escapeKey(optionName));
                this.getOutput().print('=');
            }
            if (optionValue != null) {
                this.getOutput().print(this.escapeValue(optionValue));
            }
            if (this.getConfig().isEmptyOption() || optionValue != null) {
                this.getOutput().print(this.getConfig().getLineSeparator());
            }
        } else {
            String value;
            String string = value = optionValue == null && this.getConfig().isEmptyOption() ? "" : optionValue;
            if (value != null) {
                this.getOutput().print(this.escapeKey(optionName));
                this.getOutput().print(' ');
                this.getOutput().print('=');
                this.getOutput().print(' ');
                this.getOutput().print(this.escapeValue(value));
                this.getOutput().print(this.getConfig().getLineSeparator());
            }
        }
        this.setHeader(false);
    }

    protected Config getConfig() {
        return this._config;
    }

    protected void setConfig(Config value) {
        this._config = value;
    }

    protected PrintWriter getOutput() {
        return this._output;
    }

    protected void setOutput(PrintWriter value) {
        this._output = value;
    }

    void setHeader(boolean value) {
        this._header = value;
    }

    String escapeKey(String input) {
        return this.getConfig().isEscape() ? EscapeTool.getInstance().escape(input) : input;
    }

    String escapeValue(String input) {
        return this.getConfig().isEscape() && !this.getConfig().isEscapeKeyOnly() ? EscapeTool.getInstance().escape(input) : input;
    }
}

