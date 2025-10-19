/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;
import org.ini4j.BasicMultiMap;
import org.ini4j.CommentedMap;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public class CommonMultiMap<K, V>
extends BasicMultiMap<K, V>
implements CommentedMap<K, V> {
    private static final long serialVersionUID = 3012579878005541746L;
    private static final String SEPARATOR = ";#;";
    private static final String FIRST_CATEGORY = "";
    private static final String LAST_CATEGORY = "zzzzzzzzzzzzzzzzzzzzzz";
    private static final String META_COMMENT = "comment";
    private SortedMap<String, Object> _meta;

    @Override
    public String getComment(Object key) {
        return (String)this.getMeta(META_COMMENT, key);
    }

    @Override
    public void clear() {
        super.clear();
        if (this._meta != null) {
            this._meta.clear();
        }
    }

    @Override
    public void putAll(Map<? extends K, ? extends V> map) {
        SortedMap<String, Object> meta;
        super.putAll(map);
        if (map instanceof CommonMultiMap && (meta = ((CommonMultiMap)map)._meta) != null) {
            this.meta().putAll(meta);
        }
    }

    @Override
    public String putComment(K key, String comment) {
        return (String)this.putMeta(META_COMMENT, key, comment);
    }

    @Override
    public V remove(Object key) {
        Object ret = super.remove(key);
        this.removeMeta(key);
        return ret;
    }

    @Override
    public V remove(Object key, int index) {
        Object ret = super.remove(key, index);
        if (this.length(key) == 0) {
            this.removeMeta(key);
        }
        return ret;
    }

    @Override
    public String removeComment(Object key) {
        return (String)this.removeMeta(META_COMMENT, key);
    }

    Object getMeta(String category, Object key) {
        return this._meta == null ? null : this._meta.get(this.makeKey(category, key));
    }

    Object putMeta(String category, K key, Object value) {
        return this.meta().put(this.makeKey(category, key), value);
    }

    void removeMeta(Object key) {
        if (this._meta != null) {
            this._meta.subMap(this.makeKey(FIRST_CATEGORY, key), this.makeKey(LAST_CATEGORY, key)).clear();
        }
    }

    Object removeMeta(String category, Object key) {
        return this._meta == null ? null : this._meta.remove(this.makeKey(category, key));
    }

    private String makeKey(String category, Object key) {
        StringBuilder buff = new StringBuilder();
        buff.append(String.valueOf(key));
        buff.append(SEPARATOR);
        buff.append(category);
        return buff.toString();
    }

    private Map<String, Object> meta() {
        if (this._meta == null) {
            this._meta = new TreeMap<String, Object>();
        }
        return this._meta;
    }
}

