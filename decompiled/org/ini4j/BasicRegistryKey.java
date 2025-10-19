/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import org.ini4j.BasicProfileSection;
import org.ini4j.BasicRegistry;
import org.ini4j.Registry;

class BasicRegistryKey
extends BasicProfileSection
implements Registry.Key {
    private static final long serialVersionUID = -1390060044244350928L;
    private static final String META_TYPE = "type";

    public BasicRegistryKey(BasicRegistry registry, String name) {
        super(registry, name);
    }

    public Registry.Key getChild(String key) {
        return (Registry.Key)super.getChild(key);
    }

    public Registry.Key getParent() {
        return (Registry.Key)super.getParent();
    }

    public Registry.Type getType(Object key) {
        return (Registry.Type)((Object)this.getMeta(META_TYPE, key));
    }

    public Registry.Type getType(Object key, Registry.Type defaultType) {
        Registry.Type type = this.getType(key);
        return type == null ? defaultType : type;
    }

    public Registry.Key addChild(String key) {
        return (Registry.Key)super.addChild(key);
    }

    public Registry.Key lookup(String ... path) {
        return (Registry.Key)super.lookup(path);
    }

    public Registry.Type putType(String key, Registry.Type type) {
        return (Registry.Type)((Object)this.putMeta(META_TYPE, key, (Object)type));
    }

    public Registry.Type removeType(Object key) {
        return (Registry.Type)((Object)this.removeMeta(META_TYPE, key));
    }
}

