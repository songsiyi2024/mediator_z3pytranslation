/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PushbackInputStream;
import java.io.Reader;
import java.nio.charset.Charset;

class UnicodeInputStreamReader
extends Reader {
    private static final int BOM_SIZE = 4;
    private final Charset _defaultEncoding;
    private InputStreamReader _reader;
    private final PushbackInputStream _stream;

    UnicodeInputStreamReader(InputStream in, Charset defaultEnc) {
        this._stream = new PushbackInputStream(in, 4);
        this._defaultEncoding = defaultEnc;
    }

    public void close() throws IOException {
        this.init();
        this._reader.close();
    }

    public int read(char[] cbuf, int off, int len) throws IOException {
        this.init();
        return this._reader.read(cbuf, off, len);
    }

    protected void init() throws IOException {
        int unread;
        Charset encoding;
        if (this._reader != null) {
            return;
        }
        byte[] data = new byte[4];
        int n = this._stream.read(data, 0, data.length);
        Bom bom = Bom.find(data);
        if (bom == null) {
            encoding = this._defaultEncoding;
            unread = n;
        } else {
            encoding = bom._charset;
            unread = data.length - bom._bytes.length;
        }
        if (unread > 0) {
            this._stream.unread(data, n - unread, unread);
        }
        this._reader = new InputStreamReader((InputStream)this._stream, encoding);
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    private static enum Bom {
        UTF32BE("UTF-32BE", new byte[]{0, 0, -2, -1}),
        UTF32LE("UTF-32LE", new byte[]{-1, -2, 0, 0}),
        UTF16BE("UTF-16BE", new byte[]{-2, -1}),
        UTF16LE("UTF-16LE", new byte[]{-1, -2}),
        UTF8("UTF-8", new byte[]{-17, -69, -65});

        private final byte[] _bytes;
        private Charset _charset;

        private Bom(String charsetName, byte[] bytes) {
            try {
                this._charset = Charset.forName(charsetName);
            }
            catch (Exception x) {
                this._charset = null;
            }
            this._bytes = bytes;
        }

        private static Bom find(byte[] data) {
            Bom ret = null;
            for (Bom bom : Bom.values()) {
                if (!bom.supported() || !bom.match(data)) continue;
                ret = bom;
                break;
            }
            return ret;
        }

        private boolean match(byte[] data) {
            boolean ok = true;
            for (int i = 0; i < this._bytes.length; ++i) {
                if (data[i] == this._bytes[i]) continue;
                ok = false;
                break;
            }
            return ok;
        }

        private boolean supported() {
            return this._charset != null;
        }
    }
}

