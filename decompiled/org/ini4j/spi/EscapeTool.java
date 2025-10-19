/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.spi.ServiceFinder;

public class EscapeTool {
    private static final String ESCAPE_LETTERS = "\\tnfbr:=";
    private static final String ESCAPEABLE_CHARS = "\\\t\n\f\b\r:=";
    private static final char ESCAPE_CHAR = '\\';
    static final char[] HEX = "0123456789abcdef".toCharArray();
    private static final EscapeTool INSTANCE = ServiceFinder.findService(EscapeTool.class);
    private static final char ASCII_MIN = ' ';
    private static final char ASCII_MAX = '~';
    static final int HEX_DIGIT_MASK = 15;
    static final int HEX_DIGIT_3_OFFSET = 4;
    static final int HEX_DIGIT_2_OFFSET = 8;
    static final int HEX_DIGIT_1_OFFSET = 12;
    static final int HEX_RADIX = 16;
    private static final int UNICODE_HEX_DIGITS = 4;
    static final char DOUBLE_QUOTE = '\"';

    public static EscapeTool getInstance() {
        return INSTANCE;
    }

    public String escape(String line) {
        int len = line.length();
        StringBuilder buffer = new StringBuilder(len * 2);
        for (int i = 0; i < len; ++i) {
            char c = line.charAt(i);
            int idx = ESCAPEABLE_CHARS.indexOf(c);
            if (idx >= 0) {
                buffer.append('\\');
                buffer.append(ESCAPE_LETTERS.charAt(idx));
                continue;
            }
            if (c < ' ' || c > '~') {
                this.escapeBinary(buffer, c);
                continue;
            }
            buffer.append(c);
        }
        return buffer.toString();
    }

    public String quote(String value) {
        String ret = value;
        if (value != null && value.length() != 0) {
            StringBuilder buff = new StringBuilder();
            buff.append('\"');
            for (int i = 0; i < value.length(); ++i) {
                char c = value.charAt(i);
                if (c == '\\' || c == '\"') {
                    buff.append('\\');
                }
                buff.append(c);
            }
            buff.append('\"');
            ret = buff.toString();
        }
        return ret;
    }

    public String unescape(String line) {
        int n = line.length();
        StringBuilder buffer = new StringBuilder(n);
        int i = 0;
        while (i < n) {
            char c;
            if ((c = line.charAt(i++)) == '\\') {
                int next;
                if ((next = this.unescapeBinary(buffer, c = line.charAt(i++), line, i)) == i) {
                    int idx = ESCAPE_LETTERS.indexOf(c);
                    if (idx >= 0) {
                        c = ESCAPEABLE_CHARS.charAt(idx);
                    }
                    buffer.append(c);
                    continue;
                }
                i = next;
                continue;
            }
            buffer.append(c);
        }
        return buffer.toString();
    }

    public String unquote(String value) {
        StringBuilder buff = new StringBuilder();
        boolean escape = false;
        for (int i = 1; i < value.length() - 1; ++i) {
            char c = value.charAt(i);
            if (c == '\\') {
                if (!escape) {
                    escape = true;
                    continue;
                }
                escape = false;
            }
            buff.append(c);
        }
        return buff.toString();
    }

    void escapeBinary(StringBuilder buff, char c) {
        buff.append("\\u");
        buff.append(HEX[c >>> 12 & 0xF]);
        buff.append(HEX[c >>> 8 & 0xF]);
        buff.append(HEX[c >>> 4 & 0xF]);
        buff.append(HEX[c & 0xF]);
    }

    int unescapeBinary(StringBuilder buff, char escapeType, String line, int index) {
        int ret = index;
        if (escapeType == 'u') {
            try {
                buff.append((char)Integer.parseInt(line.substring(index, index + 4), 16));
                ret = index + 4;
            }
            catch (Exception x) {
                throw new IllegalArgumentException("Malformed \\uxxxx encoding.", x);
            }
        }
        return ret;
    }
}

