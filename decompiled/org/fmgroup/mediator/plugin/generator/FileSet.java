/*
 * Decompiled with CFR 0.152.
 */
package org.fmgroup.mediator.plugin.generator;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;

public class FileSet {
    private Map<String, String> contents = new HashMap<String, String>();

    public void add(String path, String content) throws FileAlreadyExistsException {
        if (this.contents.containsKey(path)) {
            throw new FileAlreadyExistsException(path);
        }
        this.contents.put(path, content);
    }

    public void add(String path, File existingFile) throws IOException {
        String content = "";
        InputStreamReader reader = new InputStreamReader(new FileInputStream(content));
        char[] buffer = new char[(int)existingFile.length()];
        reader.read(buffer);
        this.add(path, buffer.toString());
    }

    public String toString() {
        String rendered = "";
        for (String path : this.contents.keySet()) {
            rendered = rendered + String.format("[ %s ]\n\n", path);
            rendered = rendered + this.contents.get(path) + "\n";
        }
        return rendered;
    }

    public void writeToFileSystem(File rootdir) throws FileNotFoundException {
        if (!rootdir.exists()) {
            throw new FileNotFoundException(rootdir.getPath());
        }
        for (String path : this.contents.keySet()) {
            File file = Paths.get(rootdir.getPath(), path).toFile();
            try {
                FileWriter writer = new FileWriter(file);
                writer.write(this.contents.get(path));
                writer.close();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}

