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
            String modelPath = args.length > 0 ? args[0] : "models/smallcar/motor.med";
            String systemName = args.length > 1 ? args[1] : "testbench";
            int bound = args.length > 2 ? Integer.parseInt(args[2]) : 20;

            java.lang.System.out.println("Parsing model: " + modelPath);
            
            List<String> paths = new ArrayList<>();
            paths.add("library");
            Program prog = Program.parseFile(modelPath, paths);
            
            if (prog == null) {
                java.lang.System.err.println("Error: Parsing failed (prog is null).");
                return;
            }

            // 2. Find the system entity
            Entity entity = prog.getEntity(null, systemName);
            
            if (entity == null) {
                java.lang.System.err.println("Error: Could not find system '" + systemName + "' in " + modelPath);
                return;
            }
            
            if (!(entity instanceof System)) {
                java.lang.System.err.println("Error: Entity '" + systemName + "' is not a System, it is " + entity.getClass().getSimpleName());
                return;
            }
            
            java.lang.System.out.println("Found system: " + entity.getName());
            
            // 3. Generate Z3 code
            Z3Generator generator = new Z3Generator();
            generator.setBound(bound); // Set unfolding steps
            if (!generator.available(entity)) {
                 java.lang.System.err.println("Error: Z3Generator says entity is not available.");
                 return;
            }
            
            java.lang.System.out.println("Generating Z3 script...");
            FileSet fileSet = generator.generate(entity);
            
            // 4. Output results
            // java.lang.System.out.println(fileSet.toString());
            
            File outputDir = new File("python_test");
            if (!outputDir.exists()) {
                outputDir.mkdirs();
            }
            fileSet.writeToFileSystem(outputDir);
            java.lang.System.out.println("Generated files written to: " + outputDir.getAbsolutePath());
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
