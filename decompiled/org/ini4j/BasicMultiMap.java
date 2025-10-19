/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.HashSet;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import org.ini4j.MultiMap;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public class BasicMultiMap<K, V>
implements MultiMap<K, V>,
Serializable {
    private static final long serialVersionUID = 4716749660560043989L;
    private final Map<K, List<V>> _impl;

    public BasicMultiMap() {
        this(new LinkedHashMap());
    }

    public BasicMultiMap(Map<K, List<V>> impl) {
        this._impl = impl;
    }

    @Override
    public List<V> getAll(Object key) {
        return this._impl.get(key);
    }

    @Override
    public boolean isEmpty() {
        return this._impl.isEmpty();
    }

    @Override
    public void add(K key, V value) {
        this.getList(key, true).add(value);
    }

    @Override
    public void add(K key, V value, int index) {
        this.getList(key, true).add(index, value);
    }

    @Override
    public void clear() {
        this._impl.clear();
    }

    @Override
    public boolean containsKey(Object key) {
        return this._impl.containsKey(key);
    }

    @Override
    public boolean containsValue(Object value) {
        boolean ret = false;
        for (List<V> all : this._impl.values()) {
            if (!all.contains(value)) continue;
            ret = true;
            break;
        }
        return ret;
    }

    @Override
    public Set<Map.Entry<K, V>> entrySet() {
        HashSet<Map.Entry<K, V>> ret = new HashSet<Map.Entry<K, V>>();
        for (K key : this.keySet()) {
            ret.add(new ShadowEntry(key));
        }
        return ret;
    }

    @Override
    public V get(Object key) {
        List<V> values = this.getList(key, false);
        return values == null ? null : (V)values.get(values.size() - 1);
    }

    @Override
    public V get(Object key, int index) {
        List<V> values = this.getList(key, false);
        return values == null ? null : (V)values.get(index);
    }

    @Override
    public Set<K> keySet() {
        return this._impl.keySet();
    }

    @Override
    public int length(Object key) {
        List<V> values = this.getList(key, false);
        return values == null ? 0 : values.size();
    }

    @Override
    public V put(K key, V value) {
        V ret = null;
        List<V> values = this.getList(key, true);
        if (values.isEmpty()) {
            values.add(value);
        } else {
            ret = values.set(values.size() - 1, value);
        }
        return ret;
    }

    @Override
    public V put(K key, V value, int index) {
        return this.getList(key, false).set(index, value);
    }

    @Override
    public void putAll(Map<? extends K, ? extends V> map) {
        if (map instanceof MultiMap) {
            MultiMap mm = (MultiMap)map;
            for (Object key : mm.keySet()) {
                this.putAll(key, mm.getAll(key));
            }
        } else {
            for (K key : map.keySet()) {
                this.put(key, map.get(key));
            }
        }
    }

    @Override
    public List<V> putAll(K key, List<V> values) {
        List<V> ret = this._impl.get(key);
        this._impl.put(key, new ArrayList<V>(values));
        return ret;
    }

    @Override
    public V remove(Object key) {
        List<V> prev = this._impl.remove(key);
        return prev == null ? null : (V)prev.get(0);
    }

    @Override
    public V remove(Object key, int index) {
        V ret = null;
        List<V> values = this.getList(key, false);
        if (values != null) {
            ret = values.remove(index);
            if (values.isEmpty()) {
                this._impl.remove(key);
            }
        }
        return ret;
    }

    @Override
    public int size() {
        return this._impl.size();
    }

    public String toString() {
        return this._impl.toString();
    }

    @Override
    public Collection<V> values() {
        ArrayList<V> all = new ArrayList<V>(this._impl.size());
        for (List<V> values : this._impl.values()) {
            all.addAll(values);
        }
        return all;
    }

    private List<V> getList(Object key, boolean create) {
        List<V> values = this._impl.get(key);
        if (values == null && create) {
            values = new ArrayList<V>();
            this._impl.put(key, values);
        }
        return values;
    }

    /*
     * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
     */
    class ShadowEntry
    implements Map.Entry<K, V> {
        private final K _key;

        ShadowEntry(K key) {
            this._key = key;
        }

        @Override
        public K getKey() {
            return this._key;
        }

        @Override
        public V getValue() {
            return BasicMultiMap.this.get(this._key);
        }

        @Override
        public V setValue(V value) {
            return BasicMultiMap.this.put(this._key, value);
        }
    }
}

