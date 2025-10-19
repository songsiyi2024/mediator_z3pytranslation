/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.common;

import java.io.File;
import java.io.UnsupportedEncodingException;
import java.net.URLDecoder;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import org.fmgroup.mediator.common.ToolInfo;
import org.fmgroup.mediator.plugin.Plugin;
import org.fmgroup.mediator.plugin.command.Command;
import org.fmgroup.mediator.plugin.generator.Generator;

public class UtilClass {
    private static Map<Class, Map<String, List<Class>>> cache = new HashMap<Class, Map<String, List<Class>>>();

    private static String getClassRoot() {
        try {
            return URLDecoder.decode(ToolInfo.getSystemRootPath(), "utf-8");
        }
        catch (UnsupportedEncodingException e) {
            e.printStackTrace();
            return null;
        }
    }

    public static List<Class> getImplementation(Class _interface) {
        return UtilClass.getImplementation(_interface, "");
    }

    public static List<Class> getImplementation(Class _interface, String pkgname) {
        if (cache.containsKey(_interface) && cache.get(_interface).containsKey(pkgname)) {
            return cache.get(_interface).get(pkgname);
        }
        Path searchPath = Paths.get(UtilClass.getClassRoot(), pkgname.replace(".", "/"));
        File pkg = searchPath.toFile();
        assert (pkg.isDirectory());
        List<Class> classes = UtilClass.getImplementation(_interface, pkg);
        if (!cache.containsKey(_interface)) {
            cache.put(_interface, new HashMap());
        }
        cache.get(_interface).put(pkgname, classes);
        return classes;
    }

    public static List<Class> getImplementation(Class _interface, File root) {
        ArrayList<Class> classes = new ArrayList<Class>();
        for (File f : root.listFiles()) {
            if (f.isFile() && f.getName().endsWith(".class")) {
                String clsname = f.getPath().substring(0, f.getPath().length() - 6);
                if (clsname.startsWith(UtilClass.getClassRoot())) {
                    clsname = clsname.substring(UtilClass.getClassRoot().length());
                }
                clsname = ToolInfo.isWindows() ? clsname.replace("\\", ".") : clsname.replace("/", ".");
                try {
                    if (!UtilClass.isExtendedFrom(Class.forName(clsname), _interface)) continue;
                    classes.add(Class.forName(clsname));
                }
                catch (ClassNotFoundException e) {
                    e.printStackTrace();
                }
                catch (NoClassDefFoundError noClassDefFoundError) {}
                continue;
            }
            if (!f.isDirectory()) continue;
            classes.addAll(UtilClass.getImplementation(_interface, f));
        }
        return classes;
    }

    public static List<Class<Plugin>> getPlugins() {
        ArrayList<Class<Plugin>> plugins = new ArrayList<Class<Plugin>>();
        for (Class c : UtilClass.getImplementation(Plugin.class, "org.fmgroup.mediator.plugins")) {
            plugins.add(c);
        }
        return plugins;
    }

    public static List<Class<Command>> getCommands() {
        ArrayList<Class<Command>> commands = new ArrayList<Class<Command>>();
        for (Class c : UtilClass.getImplementation(Command.class, "org.fmgroup.mediator.plugins")) {
            commands.add(c);
        }
        return commands;
    }

    public static List<Class<Generator>> getGenerators() {
        ArrayList<Class<Generator>> generators = new ArrayList<Class<Generator>>();
        for (Class c : UtilClass.getImplementation(Generator.class, "org.fmgroup.mediator.plugins")) {
            generators.add(c);
        }
        return generators;
    }

    public static boolean isExtendedFrom(Class sub, Class parent) {
        try {
            sub.asSubclass(parent);
            return true;
        }
        catch (ClassCastException classCastException) {
            return false;
        }
    }
}

