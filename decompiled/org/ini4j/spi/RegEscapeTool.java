/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j.spi;

import java.io.UnsupportedEncodingException;
import java.nio.charset.Charset;
import java.util.Arrays;
import org.ini4j.Registry;
import org.ini4j.spi.EscapeTool;
import org.ini4j.spi.ServiceFinder;
import org.ini4j.spi.TypeValuesPair;

public class RegEscapeTool
extends EscapeTool {
    private static final RegEscapeTool INSTANCE = ServiceFinder.findService(RegEscapeTool.class);
    private static final Charset HEX_CHARSET = Charset.forName("UTF-16LE");
    private static final int LOWER_DIGIT = 15;
    private static final int UPPER_DIGIT = 240;
    private static final int DIGIT_SIZE = 4;

    public static final RegEscapeTool getInstance() {
        return INSTANCE;
    }

    public TypeValuesPair decode(String raw) {
        Registry.Type type = this.type(raw);
        String value = type == Registry.Type.REG_SZ ? this.unquote(raw) : raw.substring(type.toString().length() + 1);
        switch (type) {
            case REG_EXPAND_SZ: 
            case REG_MULTI_SZ: {
                value = this.bytes2string(this.binary(value));
                break;
            }
            case REG_DWORD: {
                value = String.valueOf(Long.parseLong(value, 16));
                break;
            }
            case REG_SZ: {
                break;
            }
        }
        String[] values = type == Registry.Type.REG_MULTI_SZ ? this.splitMulti(value) : new String[]{value};
        return new TypeValuesPair(type, values);
    }

    public String encode(TypeValuesPair data) {
        String ret = null;
        if (data.getType() == Registry.Type.REG_SZ) {
            ret = this.quote(data.getValues()[0]);
        } else if (data.getValues()[0] != null) {
            ret = this.encode(data.getType(), data.getValues());
        }
        return ret;
    }

    byte[] binary(String value) {
        byte[] bytes = new byte[value.length()];
        int idx = 0;
        int shift = 4;
        for (int i = 0; i < value.length(); ++i) {
            char c = value.charAt(i);
            if (Character.isWhitespace(c)) continue;
            if (c == ',') {
                ++idx;
                shift = 4;
                continue;
            }
            int digit = Character.digit(c, 16);
            if (digit < 0) continue;
            int n = idx;
            bytes[n] = (byte)(bytes[n] | digit << shift);
            shift = 0;
        }
        return Arrays.copyOfRange(bytes, 0, idx + 1);
    }

    String encode(Registry.Type type, String[] values) {
        StringBuilder buff = new StringBuilder();
        buff.append(type.toString());
        buff.append(':');
        switch (type) {
            case REG_EXPAND_SZ: {
                buff.append(this.hexadecimal(values[0]));
                break;
            }
            case REG_DWORD: {
                buff.append(String.format("%08x", Long.parseLong(values[0])));
                break;
            }
            case REG_MULTI_SZ: {
                int n = values.length;
                for (int i = 0; i < n; ++i) {
                    buff.append(this.hexadecimal(values[i]));
                    buff.append(',');
                }
                buff.append("00,00");
                break;
            }
            default: {
                buff.append(values[0]);
            }
        }
        return buff.toString();
    }

    String hexadecimal(String value) {
        StringBuilder buff = new StringBuilder();
        if (value != null && value.length() != 0) {
            byte[] bytes = this.string2bytes(value);
            for (int i = 0; i < bytes.length; ++i) {
                buff.append(Character.forDigit((bytes[i] & 0xF0) >> 4, 16));
                buff.append(Character.forDigit(bytes[i] & 0xF, 16));
                buff.append(',');
            }
            buff.append("00,00");
        }
        return buff.toString();
    }

    Registry.Type type(String raw) {
        int idx;
        Registry.Type type = raw.charAt(0) == '\"' ? Registry.Type.REG_SZ : ((idx = raw.indexOf(58)) < 0 ? Registry.Type.REG_SZ : Registry.Type.fromString(raw.substring(0, idx)));
        return type;
    }

    private String bytes2string(byte[] bytes) {
        String str;
        try {
            str = new String(bytes, 0, bytes.length - 2, HEX_CHARSET);
        }
        catch (NoSuchMethodError x) {
            try {
                str = new String(bytes, 0, bytes.length, HEX_CHARSET.name());
            }
            catch (UnsupportedEncodingException ex) {
                throw new IllegalStateException(ex);
            }
        }
        return str;
    }

    private String[] splitMulti(String value) {
        int len = value.length();
        int n = 0;
        int start = 0;
        int end = value.indexOf(0, start);
        while (end >= 0) {
            ++n;
            start = end + 1;
            if (start >= len) break;
            end = value.indexOf(0, start);
        }
        String[] values = new String[n];
        start = 0;
        for (int i = 0; i < n; ++i) {
            end = value.indexOf(0, start);
            values[i] = value.substring(start, end);
            start = end + 1;
        }
        return values;
    }

    private byte[] string2bytes(String value) {
        byte[] bytes;
        try {
            bytes = value.getBytes(HEX_CHARSET);
        }
        catch (NoSuchMethodError x) {
            try {
                bytes = value.getBytes(HEX_CHARSET.name());
            }
            catch (UnsupportedEncodingException ex) {
                throw new IllegalStateException(ex);
            }
        }
        return bytes;
    }
}

