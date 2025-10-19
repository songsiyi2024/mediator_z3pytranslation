/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import org.ini4j.CommentedMap;
import org.ini4j.Config;
import org.ini4j.Profile;
import org.ini4j.spi.IniHandler;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
abstract class AbstractProfileBuilder
implements IniHandler {
    private Profile.Section _currentSection;
    private boolean _header;
    private String _lastComment;

    AbstractProfileBuilder() {
    }

    @Override
    public void endIni() {
        if (this._lastComment != null && this._header) {
            this.setHeaderComment();
        }
    }

    @Override
    public void endSection() {
        this._currentSection = null;
    }

    @Override
    public void handleComment(String comment) {
        if (this._lastComment != null && this._header) {
            this._header = false;
            this.setHeaderComment();
        }
        this._lastComment = comment;
    }

    @Override
    public void handleOption(String name, String value) {
        this._header = false;
        if (this.getConfig().isMultiOption()) {
            this._currentSection.add(name, value);
        } else {
            this._currentSection.put(name, value);
        }
        if (this._lastComment != null) {
            this.putComment(this._currentSection, name);
            this._lastComment = null;
        }
    }

    @Override
    public void startIni() {
        if (this.getConfig().isHeaderComment()) {
            this._header = true;
        }
    }

    @Override
    public void startSection(String sectionName) {
        if (this.getConfig().isMultiSection()) {
            this._currentSection = this.getProfile().add(sectionName);
        } else {
            Profile.Section s = (Profile.Section)this.getProfile().get(sectionName);
            Profile.Section section = this._currentSection = s == null ? this.getProfile().add(sectionName) : s;
        }
        if (this._lastComment != null) {
            if (this._header) {
                this.setHeaderComment();
            } else {
                this.putComment(this.getProfile(), sectionName);
            }
            this._lastComment = null;
        }
        this._header = false;
    }

    abstract Config getConfig();

    abstract Profile getProfile();

    Profile.Section getCurrentSection() {
        return this._currentSection;
    }

    private void setHeaderComment() {
        if (this.getConfig().isComment()) {
            this.getProfile().setComment(this._lastComment);
        }
    }

    private void putComment(CommentedMap<String, ?> map, String key) {
        if (this.getConfig().isComment()) {
            map.putComment(key, this._lastComment);
        }
    }
}

