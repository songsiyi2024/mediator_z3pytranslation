# Examples: ParseExample

This folder contains a small Java example showing how to parse a `.med` model using the project's API and print basic AST information.

Files:
- `ParseExample.java` - Java example that calls `Program.parseFile("models/example_z3.med")` and prints automata, variables and transitions.
- `models/example_z3.med` - a small automaton used by the example.

Prerequisites:
- Java JDK (javac and java) on PATH.
- You should run the example from the `release` directory so classpath resolution works with the shipped `org` classes.

Build & run (PowerShell):

```powershell
# From the release directory
# 1) Compile the example against the existing classes (class files in release/org/...)
javac -cp .;org ParseExample.java -d examples_bin

# 2) Run the example (include current dir and release org classes in classpath)
java -cp .;org;examples_bin ParseExample
```

Notes:
- If `Program.parseFile` prints syntax errors to stderr, the example will return with a null Program and print a message.
- If you see ClassNotFoundException for mediator classes, ensure you run from the `release` directory (the folder that contains `org/` compiled classes) and the classpath includes `.` and `org`.

If you'd like, I can also provide a small PowerShell script that automates compilation and runs the example, or create a simple Gradle/Maven wrapper for a more repeatable build. Let me know which you prefer.

Note about Gradle: a minimal Gradle build implementation lives under `release/tools/gradle/`.
At repository root there is a delegator `gradlew`/`gradlew.bat` which forwards to that implementation.
If you have Gradle installed you can run:

```powershell
# From the release directory
.\gradlew.bat runParseExample
```

Or use the provided scripts in `examples/`:

```powershell
# From the release directory
examples\build_and_run.ps1
```