/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.core.antlr;

import java.util.ArrayList;
import java.util.List;
import org.antlr.v4.runtime.BaseErrorListener;
import org.antlr.v4.runtime.RecognitionException;
import org.antlr.v4.runtime.Recognizer;
import org.fmgroup.mediator.language.ValidationException;

public class VerboseListener
extends BaseErrorListener {
    private List<ValidationException> exceptions = new ArrayList<ValidationException>();

    public List<ValidationException> getExceptions() {
        return this.exceptions;
    }

    @Override
    public void syntaxError(Recognizer<?, ?> recognizer, Object offendingSymbol, int line, int charPositionInLine, String msg, RecognitionException e) {
        this.exceptions.add(ValidationException.FromMessage(msg).setLine(line).setColumn(charPositionInLine));
    }

    public boolean Succeed() {
        return this.exceptions.size() == 0;
    }
}

