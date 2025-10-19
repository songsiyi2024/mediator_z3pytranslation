/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.IOException;
import java.io.InputStream;
import java.io.LineNumberReader;
import java.io.Reader;
import java.net.URL;
import org.ini4j.Config;
import org.ini4j.spi.HandlerBase;
import org.ini4j.spi.UnicodeInputStreamReader;

class IniSource {
    public static final char INCLUDE_BEGIN = '<';
    public static final char INCLUDE_END = '>';
    public static final char INCLUDE_OPTIONAL = '?';
    private static final char ESCAPE_CHAR = '\\';
    private URL _base;
    private IniSource _chain;
    private final String _commentChars;
    private final Config _config;
    private final HandlerBase _handler;
    private final LineNumberReader _reader;

    IniSource(InputStream input, HandlerBase handler, String comments, Config config) {
        this(new UnicodeInputStreamReader(input, config.getFileEncoding()), handler, comments, config);
    }

    IniSource(Reader input, HandlerBase handler, String comments, Config config) {
        this._reader = new LineNumberReader(input);
        this._handler = handler;
        this._commentChars = comments;
        this._config = config;
    }

    IniSource(URL input, HandlerBase handler, String comments, Config config) throws IOException {
        this(new UnicodeInputStreamReader(input.openStream(), config.getFileEncoding()), handler, comments, config);
        this._base = input;
    }

    int getLineNumber() {
        int ret = this._chain == null ? this._reader.getLineNumber() : this._chain.getLineNumber();
        return ret;
    }

    String readLine() throws IOException {
        String line;
        if (this._chain == null) {
            line = this.readLineLocal();
        } else {
            line = this._chain.readLine();
            if (line == null) {
                this._chain = null;
                line = this.readLine();
            }
        }
        return line;
    }

    private void close() throws IOException {
        this._reader.close();
    }

    private int countEndingEscapes(String line) {
        int escapeCount = 0;
        for (int i = line.length() - 1; i >= 0 && line.charAt(i) == '\\'; --i) {
            ++escapeCount;
        }
        return escapeCount;
    }

    private void handleComment(StringBuilder buff) {
        if (buff.length() != 0) {
            buff.deleteCharAt(buff.length() - 1);
            this._handler.handleComment(buff.toString());
            buff.delete(0, buff.length());
        }
    }

    /*
     * WARNING - Removed try catching itself - possible behaviour change.
     */
    private String handleInclude(String input) throws IOException {
        String line = input;
        if (this._config.isInclude() && line.length() > 2 && line.charAt(0) == '<' && line.charAt(line.length() - 1) == '>') {
            URL loc;
            boolean optional;
            boolean bl = optional = (line = line.substring(1, line.length() - 1).trim()).charAt(0) == '?';
            if (optional) {
                line = line.substring(1).trim();
            }
            URL uRL = loc = this._base == null ? new URL(line) : new URL(this._base, line);
            if (optional) {
                try {
                    this._chain = new IniSource(loc, this._handler, this._commentChars, this._config);
                }
                catch (IOException x) {
                }
                finally {
                    line = this.readLine();
                }
            } else {
                this._chain = new IniSource(loc, this._handler, this._commentChars, this._config);
                line = this.readLine();
            }
        }
        return line;
    }

    private String readLineLocal() throws IOException {
        String line = this.readLineSkipComments();
        if (line == null) {
            this.close();
        } else {
            line = this.handleInclude(line);
        }
        return line;
    }

    private String readLineSkipComments() throws IOException {
        StringBuilder comment = new StringBuilder();
        StringBuilder buff = new StringBuilder();
        String line = this._reader.readLine();
        while (line != null) {
            if ((line = line.trim()).length() == 0) {
                this.handleComment(comment);
            } else if (this._commentChars.indexOf(line.charAt(0)) >= 0 && buff.length() == 0) {
                comment.append(line.substring(1));
                comment.append(this._config.getLineSeparator());
            } else {
                this.handleComment(comment);
                if (!this._config.isEscapeNewline() || (this.countEndingEscapes(line) & 1) == 0) {
                    buff.append(line);
                    line = buff.toString();
                    break;
                }
                buff.append(line.subSequence(0, line.length() - 1));
            }
            line = this._reader.readLine();
        }
        if (line == null && comment.length() != 0) {
            this.handleComment(comment);
        }
        return line;
    }
}

