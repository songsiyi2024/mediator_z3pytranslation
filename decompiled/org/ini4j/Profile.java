/*
 * Decompiled with CFR 0.152.
 */
package org.ini4j;

import org.ini4j.CommentedMap;
import org.ini4j.MultiMap;
import org.ini4j.OptionMap;

/*
 * This class specifies class file version 49.0 but uses Java 6 signatures.  Assumed Java 6.
 */
public interface Profile
extends MultiMap<String, Section>,
CommentedMap<String, Section> {
    public static final char PATH_SEPARATOR = '/';

    public String getComment();

    public void setComment(String var1);

    public Section add(String var1);

    public void add(String var1, String var2, Object var3);

    public <T> T as(Class<T> var1);

    public <T> T as(Class<T> var1, String var2);

    public String fetch(Object var1, Object var2);

    public <T> T fetch(Object var1, Object var2, Class<T> var3);

    public String get(Object var1, Object var2);

    public <T> T get(Object var1, Object var2, Class<T> var3);

    public String put(String var1, String var2, Object var3);

    public Section remove(Section var1);

    public String remove(Object var1, Object var2);

    public static interface Section
    extends OptionMap {
        public Section getChild(String var1);

        public String getName();

        public Section getParent();

        public String getSimpleName();

        public Section addChild(String var1);

        public String[] childrenNames();

        public Section lookup(String ... var1);

        public void removeChild(String var1);
    }
}

