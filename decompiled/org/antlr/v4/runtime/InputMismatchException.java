/*
 * Decompiled with CFR 0.152.
 */
package org.antlr.v4.runtime;

import org.antlr.v4.runtime.Parser;
import org.antlr.v4.runtime.RecognitionException;

public class InputMismatchException
extends RecognitionException {
    public InputMismatchException(Parser recognizer) {
        super(recognizer, recognizer.getInputStream(), recognizer._ctx);
        this.setOffendingToken(recognizer.getCurrentToken());
    }
}

