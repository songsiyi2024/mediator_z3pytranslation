import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import org.fmgroup.mediator.plugins.generators.z3.Z3Generator;
import org.fmgroup.mediator.plugin.generator.FileSet;
import java.io.File;
import java.util.Map;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.StandardCopyOption;

public class MediatorToZ3 {
    public static void main(String[] args) throws Exception {
        String model = args.length > 0 ? args[0] : "models/testbench.med";
        int bound = args.length > 1 ? Integer.parseInt(args[1]) : 20;
        String customOutputName = args.length > 2 ? args[2] : null;

        System.out.println("Parsing: " + model);
        
        List<String> libPaths = new java.util.ArrayList<>();
        libPaths.add(new File("library").getAbsolutePath());
        
        Program p = Program.parseFile(model, libPaths);
        if (p == null) {
            System.err.println("Parsing failed (null Program). Check for syntax errors printed to stderr.");
            return;
        }
        
        // Generate Z3
        Z3Generator gen = new Z3Generator();
        gen.setBound(bound);

        org.fmgroup.mediator.language.RawElement target = null;
        
        if (p.getSystems().size() > 0) {
            target = p.getSystems().values().iterator().next();
        } else if (p.getAutomata().size() > 0) {
            target = p.getAutomata().values().iterator().next();
        }
        
        if (target != null) {
            String name = ((org.fmgroup.mediator.language.entity.Entity)target).getName();
            System.out.println("Generating Z3 for " + name + " with bound " + bound);
            FileSet fs = gen.generate(target);
            
            File outputDir = new File("python_test");
            if (!outputDir.exists()) {
                outputDir.mkdirs();
            }
            
            // Ensure flattened_automaton directory exists (it's a sibling of python_test)
            File flattenedDir = new File("flattened_automaton");
            if (!flattenedDir.exists()) {
                flattenedDir.mkdirs();
            }
            
            fs.writeToFileSystem(outputDir);

            // Rename the generated file if a custom name is provided
            File generatedFile = new File(outputDir, name + "_z3_check.py");
            
            if (customOutputName != null) {
                File targetFile = new File(outputDir, customOutputName);
                if (generatedFile.exists()) {
                    Files.move(generatedFile.toPath(), targetFile.toPath(), StandardCopyOption.REPLACE_EXISTING);
                    System.out.println("Renamed " + generatedFile.getName() + " to " + targetFile.getName());
                } else {
                    System.err.println("Expected generated file " + generatedFile.getAbsolutePath() + " not found.");
                }
            } else {
                System.out.println("Generated file: " + generatedFile.getName());
            }

            System.out.println("Generated files in: " + outputDir.getAbsolutePath() + " and " + flattenedDir.getAbsolutePath());
        }
    }
}
