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
import org.ini4j.BasicOptionMap;
import org.ini4j.Config;
import org.ini4j.Configurable;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.Persistable;
import org.ini4j.spi.OptionsBuilder;
import org.ini4j.spi.OptionsFormatter;
import org.ini4j.spi.OptionsHandler;
import org.ini4j.spi.OptionsParser;

public class Options
extends BasicOptionMap
implements Persistable,
Configurable {
    private static final long serialVersionUID = -1119753444859181822L;
    private String _comment;
    private Config _config = Config.getGlobal().clone();
    private File _file;

    public Options() {
        this._config.setEmptyOption(true);
    }

    public Options(Reader input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Options(InputStream input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Options(URL input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Options(File input) throws IOException, InvalidFileFormatException {
        this();
        this._file = input;
        this.load();
    }

    public String getComment() {
        return this._comment;
    }

    public void setComment(String value) {
        this._comment = value;
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
        OptionsParser.newInstance(this.getConfig()).parse(input, this.newBuilder());
    }

    public void load(URL input) throws IOException, InvalidFileFormatException {
        OptionsParser.newInstance(this.getConfig()).parse(input, this.newBuilder());
    }

    public void load(File input) throws IOException, InvalidFileFormatException {
        this.load(input.toURI().toURL());
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
        this.store(OptionsFormatter.newInstance(output, this.getConfig()));
    }

    public void store(File output) throws IOException {
        FileOutputStream stream = new FileOutputStream(output);
        this.store(stream);
        ((OutputStream)stream).close();
    }

    protected OptionsHandler newBuilder() {
        return OptionsBuilder.newInstance(this);
    }

    protected void store(OptionsHandler formatter) throws IOException {
        formatter.startOptions();
        this.storeComment(formatter, this._comment);
        for (String name : this.keySet()) {
            this.storeComment(formatter, this.getComment(name));
            int n = this.getConfig().isMultiOption() ? this.length(name) : 1;
            for (int i = 0; i < n; ++i) {
                String value = (String)this.get((Object)name, i);
                formatter.handleOption(name, value);
            }
        }
        formatter.endOptions();
    }

    boolean isPropertyFirstUpper() {
        return this.getConfig().isPropertyFirstUpper();
    }

    private void storeComment(OptionsHandler formatter, String comment) {
        formatter.handleComment(comment);
    }
}

