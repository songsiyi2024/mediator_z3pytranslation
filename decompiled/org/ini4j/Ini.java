/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;
import java.net.URL;
import org.ini4j.BasicProfile;
import org.ini4j.Config;
import org.ini4j.Configurable;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.Persistable;
import org.ini4j.Profile;
import org.ini4j.spi.IniBuilder;
import org.ini4j.spi.IniFormatter;
import org.ini4j.spi.IniHandler;
import org.ini4j.spi.IniParser;

public class Ini
extends BasicProfile
implements Persistable,
Configurable {
    private static final long serialVersionUID = -6029486578113700585L;
    private Config _config = Config.getGlobal();
    private File _file;

    public Ini() {
    }

    public Ini(Reader input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Ini(InputStream input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Ini(URL input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Ini(File input) throws IOException, InvalidFileFormatException {
        this();
        this._file = input;
        this.load();
    }

    public Config getConfig() {
        return this._config;
    }

    public void setConfig(Config value) {
        this._config = value;
    }

    public File getFile() {
        return this._file;
    }

    public void setFile(File value) {
        this._file = value;
    }

    public void load() throws IOException, InvalidFileFormatException {
        if (this._file == null) {
            throw new FileNotFoundException();
        }
        this.load(this._file);
    }

    public void load(InputStream input) throws IOException, InvalidFileFormatException {
        this.load(new InputStreamReader(input, this.getConfig().getFileEncoding()));
    }

    public void load(Reader input) throws IOException, InvalidFileFormatException {
        IniParser.newInstance(this.getConfig()).parse(input, this.newBuilder());
    }

    public void load(File input) throws IOException, InvalidFileFormatException {
        this.load(input.toURI().toURL());
    }

    public void load(URL input) throws IOException, InvalidFileFormatException {
        IniParser.newInstance(this.getConfig()).parse(input, this.newBuilder());
    }

    public void store() throws IOException {
        if (this._file == null) {
            throw new FileNotFoundException();
        }
        this.store(this._file);
    }

    public void store(OutputStream output) throws IOException {
        this.store(new OutputStreamWriter(output, this.getConfig().getFileEncoding()));
    }

    public void store(Writer output) throws IOException {
        this.store(IniFormatter.newInstance(output, this.getConfig()));
    }

    public void store(File output) throws IOException {
        FileOutputStream stream = new FileOutputStream(output);
        this.store(stream);
        ((OutputStream)stream).close();
    }

    protected IniHandler newBuilder() {
        return IniBuilder.newInstance(this);
    }

    protected void store(IniHandler formatter, Profile.Section section) {
        if (this.getConfig().isEmptySection() || section.size() != 0) {
            super.store(formatter, section);
        }
    }

    protected void store(IniHandler formatter, Profile.Section section, String option, int index) {
        if (this.getConfig().isMultiOption() || index == section.length(option) - 1) {
            super.store(formatter, section, option, index);
        }
    }

    boolean isTreeMode() {
        return this.getConfig().isTree();
    }

    char getPathSeparator() {
        return this.getConfig().getPathSeparator();
    }

    boolean isPropertyFirstUpper() {
        return this.getConfig().isPropertyFirstUpper();
    }
}

