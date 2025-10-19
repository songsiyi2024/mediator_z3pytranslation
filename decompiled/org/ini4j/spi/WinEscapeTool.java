/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.spi.EscapeTool;

public class WinEscapeTool
extends EscapeTool {
    private static final int ANSI_HEX_DIGITS = 2;
    private static final int ANSI_OCTAL_DIGITS = 3;
    private static final int OCTAL_RADIX = 8;
    private static final WinEscapeTool INSTANCE = new WinEscapeTool();

    public static WinEscapeTool getInstance() {
        return INSTANCE;
    }

    void escapeBinary(StringBuilder buff, char c) {
        buff.append("\\x");
        buff.append(HEX[c >>> 4 & 0xF]);
        buff.append(HEX[c & 0xF]);
    }

    int unescapeBinary(StringBuilder buff, char escapeType, String line, int index) {
        int ret = index;
        if (escapeType == 'x') {
            try {
                buff.append((char)Integer.parseInt(line.substring(index, index + 2), 16));
                ret = index + 2;
            }
            catch (Exception x) {
                throw new IllegalArgumentException("Malformed \\xHH encoding.", x);
            }
        }
        if (escapeType == 'o') {
            try {
                buff.append((char)Integer.parseInt(line.substring(index, index + 3), 8));
                ret = index + 3;
            }
            catch (Exception x) {
                throw new IllegalArgumentException("Malformed \\oOO encoding.", x);
            }
        }
        return ret;
    }
}

