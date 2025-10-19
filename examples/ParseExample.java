import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.entity.automaton.Automaton;
import org.fmgroup.mediator.language.scope.VariableDeclarationCollection;
import java.util.Map;
import java.util.List;

public class ParseExample {
    public static void main(String[] args) throws Exception {
        String model = "models/example_z3.med";
        System.out.println("Parsing: " + model);
        Program p = Program.parseFile(model);
        if (p == null) {
            System.err.println("Parsing failed (null Program). Check for syntax errors printed to stderr.");
            return;
        }
        System.out.println("Program toString():\n" + p.toString());
        Map<String, Automaton> automata = p.getAutomata();
        System.out.println("Found automata: " + automata.keySet());
        for (String name : automata.keySet()) {
            Automaton a = automata.get(name);
            System.out.println("Automaton: " + a.getName());
            VariableDeclarationCollection vars = a.getLocalVars();
            System.out.println("Variables:\n" + vars.toString());
            System.out.println("Transitions:\n" + a.getTransitions().toString());
        }
    }
}
