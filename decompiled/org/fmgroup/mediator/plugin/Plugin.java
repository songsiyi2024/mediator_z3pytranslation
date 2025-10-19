/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugin;

import java.util.ArrayList;
import java.util.List;

public interface Plugin {
    public String getName();

    public String getVersion();

    public String getDescription();

    default public boolean isBuiltIn() {
        return false;
    }

    default public List<String> requiredLibraries() {
        return new ArrayList<String>();
    }
}

