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
import java.io.InterruptedIOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.Reader;
import java.io.Writer;
import java.net.URL;
import org.ini4j.BasicRegistry;
import org.ini4j.Config;
import org.ini4j.Configurable;
import org.ini4j.InvalidFileFormatException;
import org.ini4j.Persistable;
import org.ini4j.Registry;
import org.ini4j.spi.IniFormatter;
import org.ini4j.spi.IniHandler;
import org.ini4j.spi.IniParser;
import org.ini4j.spi.RegBuilder;

public class Reg
extends BasicRegistry
implements Registry,
Persistable,
Configurable {
    private static final long serialVersionUID = -1485602876922985912L;
    protected static final String DEFAULT_SUFFIX = ".reg";
    protected static final String TMP_PREFIX = "reg-";
    private static final int STDERR_BUFF_SIZE = 8192;
    private static final String PROP_OS_NAME = "os.name";
    private static final boolean WINDOWS = Config.getSystemProperty("os.name", "Unknown").startsWith("Windows");
    private static final char CR = '\r';
    private static final char LF = '\n';
    private Config _config;
    private File _file;

    public Reg() {
        Config cfg = Config.getGlobal().clone();
        cfg.setEscape(false);
        cfg.setGlobalSection(false);
        cfg.setEmptyOption(true);
        cfg.setMultiOption(true);
        cfg.setStrictOperator(true);
        cfg.setEmptySection(true);
        cfg.setPathSeparator('\\');
        cfg.setFileEncoding(FILE_ENCODING);
        cfg.setLineSeparator("\r\n");
        this._config = cfg;
    }

    public Reg(String registryKey) throws IOException {
        this();
        this.read(registryKey);
    }

    public Reg(File input) throws IOException, InvalidFileFormatException {
        this();
        this._file = input;
        this.load();
    }

    public Reg(URL input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Reg(InputStream input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public Reg(Reader input) throws IOException, InvalidFileFormatException {
        this();
        this.load(input);
    }

    public static boolean isWindows() {
        return WINDOWS;
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

    public void load(URL input) throws IOException, InvalidFileFormatException {
        this.load(new InputStreamReader(input.openStream(), this.getConfig().getFileEncoding()));
    }

    public void load(Reader input) throws IOException, InvalidFileFormatException {
        int newline = 2;
        StringBuilder buff = new StringBuilder();
        int c = input.read();
        while (c != -1) {
            if (c == 10) {
                if (--newline == 0) {
                    break;
                }
            } else if (c != 13 && newline != 1) {
                buff.append((char)c);
            }
            c = input.read();
        }
        if (buff.length() == 0) {
            throw new InvalidFileFormatException("Missing version header");
        }
        if (!buff.toString().equals(this.getVersion())) {
            throw new InvalidFileFormatException("Unsupported version: " + buff.toString());
        }
        IniParser.newInstance(this.getConfig()).parse(input, this.newBuilder());
    }

    public void load(File input) throws IOException, InvalidFileFormatException {
        this.load(input.toURI().toURL());
    }

    /*
     * WARNING - Removed try catching itself - possible behaviour change.
     */
    public void read(String registryKey) throws IOException {
        File tmp = this.createTempFile();
        try {
            this.regExport(registryKey, tmp);
            this.load(tmp);
        }
        finally {
            tmp.delete();
        }
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
        output.write(this.getVersion());
        output.write(this.getConfig().getLineSeparator());
        output.write(this.getConfig().getLineSeparator());
        this.store(IniFormatter.newInstance(output, this.getConfig()));
    }

    public void store(File output) throws IOException {
        FileOutputStream stream = new FileOutputStream(output);
        this.store(stream);
        ((OutputStream)stream).close();
    }

    /*
     * WARNING - Removed try catching itself - possible behaviour change.
     */
    public void write() throws IOException {
        File tmp = this.createTempFile();
        try {
            this.store(tmp);
            this.regImport(tmp);
        }
        finally {
            tmp.delete();
        }
    }

    protected IniHandler newBuilder() {
        return RegBuilder.newInstance(this);
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

    void exec(String[] args) throws IOException {
        Process proc = Runtime.getRuntime().exec(args);
        try {
            int status = proc.waitFor();
            if (status != 0) {
                InputStreamReader in = new InputStreamReader(proc.getErrorStream());
                char[] buff = new char[8192];
                int n = in.read(buff);
                ((Reader)in).close();
                throw new IOException(new String(buff, 0, n).trim());
            }
        }
        catch (InterruptedException x) {
            throw (IOException)new InterruptedIOException().initCause(x);
        }
    }

    private File createTempFile() throws IOException {
        File ret = File.createTempFile(TMP_PREFIX, DEFAULT_SUFFIX);
        ret.deleteOnExit();
        return ret;
    }

    private void regExport(String registryKey, File file) throws IOException {
        this.requireWindows();
        this.exec(new String[]{"cmd", "/c", "reg", "export", registryKey, file.getAbsolutePath()});
    }

    private void regImport(File file) throws IOException {
        this.requireWindows();
        this.exec(new String[]{"cmd", "/c", "reg", "import", file.getAbsolutePath()});
    }

    private void requireWindows() {
        if (!WINDOWS) {
            throw new UnsupportedOperationException("Unsupported operating system or runtime environment");
        }
    }
}

