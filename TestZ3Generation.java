import java.util.ArrayList;
import java.util.List;
import org.fmgroup.mediator.common.ToolInfo;
import org.fmgroup.mediator.language.Program;
import org.fmgroup.mediator.language.entity.Entity;
import org.fmgroup.mediator.plugin.generator.FileSet;
import org.fmgroup.mediator.plugins.generators.z3.Z3Generator;

public class TestZ3Generation {
   public TestZ3Generation() {
   }

   public static void main(String[] var0) {
      try {
         System.out.println("System Library Path: " + ToolInfo.getSystemLibraryPath());
         System.out.println("User Dir: " + System.getProperty("user.dir"));
         String var1 = var0.length > 0 ? var0[0] : "models/smallcar/motor.med";
         String var2 = var0.length > 1 ? var0[1] : "testbench";
         int var3 = var0.length > 2 ? Integer.parseInt(var0[2]) : 20;
         System.out.println("Parsing model: " + var1);
         ArrayList var4 = new ArrayList();
         var4.add("library");
         Program var5 = Program.parseFile(var1, var4);
         if (var5 == null) {
            System.err.println("Error: Parsing failed (prog is null).");
            return;
         }

         Entity var6 = var5.getEntity((List)null, var2);
         if (var6 == null) {
            System.err.println("Error: Could not find system '" + var2 + "' in " + var1);
            return;
         }

         if (!(var6 instanceof org.fmgroup.mediator.language.entity.system.System)) {
            System.err.println("Error: Entity '" + var2 + "' is not a System, it is " + var6.getClass().getSimpleName());
            return;
         }

         System.out.println("Found system: " + var6.getName());
         Z3Generator var7 = new Z3Generator();
         var7.setBound(var3);
         if (!var7.available(var6)) {
            System.err.println("Error: Z3Generator says entity is not available.");
            return;
         }

         System.out.println("Generating Z3 script...");
         FileSet var8 = var7.generate(var6);
         System.out.println(var8.toString());
      } catch (Exception var9) {
         var9.printStackTrace();
      }

   }
}