/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.spi.HandlerBase;

public interface OptionsHandler
extends HandlerBase {
    public void endOptions();

    public void handleComment(String var1);

    public void handleOption(String var1, String var2);

    public void startOptions();
}

