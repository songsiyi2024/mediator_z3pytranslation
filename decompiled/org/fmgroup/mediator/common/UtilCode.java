/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.common;

public class UtilCode {
    public static String addIndent(String rawCode, int level) {
        int i;
        if (rawCode.equals("")) {
            return "";
        }
        String[] lines = rawCode.split("\n");
        String newCode = "";
        String indent = "";
        for (i = 0; i < level; ++i) {
            indent = indent + "\t";
        }
        for (i = 0; i < lines.length; ++i) {
            newCode = newCode + indent + lines[i];
            if (i >= lines.length - 1 && !rawCode.endsWith("\n")) continue;
            newCode = newCode + "\n";
        }
        return newCode;
    }
}

