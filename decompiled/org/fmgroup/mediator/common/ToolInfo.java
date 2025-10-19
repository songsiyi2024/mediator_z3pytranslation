/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.common;

import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.file.Paths;

public class ToolInfo {
    public static String version = "alpha";
    public static String authors = "Li Yi";
    public static boolean DEBUG = true;

    public static boolean isWindows() {
        String os = System.getProperty("os.name");
        return os.toLowerCase().contains("windows");
    }

    public static String getSystemRootPath() {
        String path = ToolInfo.class.getResource("/").getPath().toString();
        if (ToolInfo.isWindows()) {
            if (path.startsWith("/")) {
                path = path.substring(1);
            }
            path = path.replace('/', '\\');
        }
        return path;
    }

    public static String getSystemLibraryPath() {
        try {
            String root = URLDecoder.decode(ToolInfo.getSystemRootPath(), "utf-8");
            return Paths.get(root, "library").toString();
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return null;
        }
    }
}

