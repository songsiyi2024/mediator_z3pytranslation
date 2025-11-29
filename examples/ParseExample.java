import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import org.fmgroup.mediator.plugins.generators.z3.Z3Generator;
import org.fmgroup.mediator.plugin.generator.FileSet;
import java.io.File;
import java.util.Map;
import java.util.List;

public class ParseExample {
    public static void main(String[] args) throws Exception {
        String model = args.length > 0 ? args[0] : "models/testbench.med";
        System.out.println("Parsing: " + model);
        Program p = Program.parseFile(model);
        if (p == null) {
            System.err.println("Parsing failed (null Program). Check for syntax errors printed to stderr.");
            return;
        }
        
        // Generate Z3
        Z3Generator gen = new Z3Generator();
        org.fmgroup.mediator.language.RawElement target = null;
        
        if (p.getSystems().size() > 0) {
            target = p.getSystems().values().iterator().next();
        } else if (p.getAutomata().size() > 0) {
            target = p.getAutomata().values().iterator().next();
        }
        
        if (target != null) {
            System.out.println("Generating Z3 for " + ((org.fmgroup.mediator.language.entity.Entity)target).getName());
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
            System.out.println("Generated files in: " + outputDir.getAbsolutePath() + " and " + flattenedDir.getAbsolutePath());
        }
    }
}
