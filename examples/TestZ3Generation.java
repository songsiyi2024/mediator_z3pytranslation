import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.language.entity.system.System;
import org.fmgroup.mediator.plugins.generators.z3.Z3Generator;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.common.ToolInfo;
import java.io.File;
import java.util.Map;
import java.util.List;
import java.util.ArrayList;

public class TestZ3Generation {
    public static void main(String[] args) {
        try {
            java.lang.System.out.println("System Library Path: " + ToolInfo.getSystemLibraryPath());
            java.lang.System.out.println("User Dir: " + java.lang.System.getProperty("user.dir"));

            // 1. Parse the model file
            // Note: Adjust path if running from a different directory
            String modelPath = "models/smallcar/motor.med";
            java.lang.System.out.println("Parsing model: " + modelPath);
            
            List<String> paths = new ArrayList<>();
            paths.add("library");
            Program prog = Program.parseFile(modelPath, paths);
            
            if (prog == null) {
                java.lang.System.err.println("Error: Parsing failed (prog is null).");
                return;
            }

            // WORKAROUND: Clear properties from all automata to avoid ValidationException.UnderDevelopment
            // which is thrown by PropertyCollection.copy() during system instantiation.
            // We use reflection because setProperties(null) throws NPE.
            for (org.fmgroup.mediator.language.entity.automaton.Automaton autom : prog.getAutomata().values()) {
                try {
                    java.lang.reflect.Field f = org.fmgroup.mediator.language.entity.automaton.Automaton.class.getDeclaredField("properties");
                    f.setAccessible(true);
                    f.set(autom, null);
                } catch (Exception e) {
                    java.lang.System.err.println("Warning: Failed to clear properties for automaton " + autom.getName());
                    e.printStackTrace();
                }
            }

            // 2. Find the system entity 'testbench'
            Entity entity = prog.getEntity(null, "testbench");
            
            if (entity == null) {
                java.lang.System.err.println("Error: Could not find system 'testbench' in " + modelPath);
                return;
            }
            
            if (!(entity instanceof System)) {
                java.lang.System.err.println("Error: Entity 'testbench' is not a System, it is " + entity.getClass().getSimpleName());
                return;
            }
            
            java.lang.System.out.println("Found system: " + entity.getName());
            
            // 3. Generate Z3 code
            Z3Generator generator = new Z3Generator();
            generator.setBound(20); // Set unfolding steps to 20
            if (!generator.available(entity)) {
                 java.lang.System.err.println("Error: Z3Generator says entity is not available.");
                 return;
            }
            
            java.lang.System.out.println("Generating Z3 script...");
            FileSet fileSet = generator.generate(entity);
            
            // 4. Output results
            java.lang.System.out.println(fileSet.toString());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
