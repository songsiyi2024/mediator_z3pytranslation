/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugin.generator;

import org.fmgroup.mediator.language.RawElement;
import org.fmgroup.mediator.plugin.Plugin;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugins.generators.arduino.ArduinoGeneratorException;

public interface Generator
extends Plugin {
    public FileSet generate(RawElement var1) throws ArduinoGeneratorException;

    default public boolean available(RawElement elem) throws ArduinoGeneratorException {
        return true;
    }

    public String getSupportedPlatform();
}

