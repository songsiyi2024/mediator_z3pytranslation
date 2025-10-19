/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.Config;
import org.ini4j.Options;
import org.ini4j.spi.OptionsHandler;
import org.ini4j.spi.ServiceFinder;

public class OptionsBuilder
implements OptionsHandler {
    private boolean _header;
    private String _lastComment;
    private Options _options;

    public static OptionsBuilder newInstance(Options opts) {
        OptionsBuilder instance = OptionsBuilder.newInstance();
        instance.setOptions(opts);
        return instance;
    }

    public void setOptions(Options value) {
        this._options = value;
    }

    public void endOptions() {
        if (this._lastComment != null && this._header) {
            this.setHeaderComment();
        }
    }

    public void handleComment(String comment) {
        if (this._lastComment != null && this._header) {
            this.setHeaderComment();
            this._header = false;
        }
        this._lastComment = comment;
    }

    public void handleOption(String name, String value) {
        if (this.getConfig().isMultiOption()) {
            this._options.add(name, value);
        } else {
            this._options.put(name, value);
        }
        if (this._lastComment != null) {
            if (this._header) {
                this.setHeaderComment();
            } else {
                this.putComment(name);
            }
            this._lastComment = null;
        }
        this._header = false;
    }

    public void startOptions() {
        if (this.getConfig().isHeaderComment()) {
            this._header = true;
        }
    }

    protected static OptionsBuilder newInstance() {
        return ServiceFinder.findService(OptionsBuilder.class);
    }

    private Config getConfig() {
        return this._options.getConfig();
    }

    private void setHeaderComment() {
        if (this.getConfig().isComment()) {
            this._options.setComment(this._lastComment);
        }
    }

    private void putComment(String key) {
        if (this.getConfig().isComment()) {
            this._options.putComment(key, this._lastComment);
        }
    }
}

