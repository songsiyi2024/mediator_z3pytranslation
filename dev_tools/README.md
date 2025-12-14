# Development Tools

This directory contains temporary tools and scripts used for the development and testing of the Mediator-to-Z3 translation feature.

## Contents

*   **`MediatorToZ3.java`**: A standalone driver program used to parse Mediator models and invoke the `Z3Generator`. It serves as a test harness during development.
    *   Usage: `java -cp "dev_tools;.;org;net/sourceforge/argparse4j" MediatorToZ3 <model_path> <bound>`
    *   Example: `java -cp "dev_tools;.;org;net/sourceforge/argparse4j" MediatorToZ3 models/medical_pump.med 20`
*   **`Z3Debugger.py`**: A Python script to instrument generated Z3 verification scripts with incremental checks. It helps pinpoint exactly which step or constraint causes an `unsat` result during debugging.
    *   Usage: `python dev_tools/Z3Debugger.py <input_z3_script.py> [--mode step|all]`

## Note

These tools are intended for internal development use. Once the Z3 generation feature is fully stable and integrated, the functionality demonstrated here will be merged into the core `mediator` generation pipeline (e.g., `Generator.generate()`).
