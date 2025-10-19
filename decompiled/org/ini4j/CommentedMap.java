/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import java.util.Map;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public interface CommentedMap<K, V>
extends Map<K, V> {
    public String getComment(Object var1);

    public String putComment(K var1, String var2);

    public String removeComment(Object var1);
}

