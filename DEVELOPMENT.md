# Mediator-Z3: A Bounded Model Checking Framework for Mediator Models

## 1. Introduction & Background
This repository hosts the development of a formal verification backend for the **Mediator** modeling language. Mediator is a domain-specific language designed for modeling Cyber-Physical Systems (CPS), emphasizing the composition of heterogeneous components and their interactions.

The primary objective of this project is to enable **Bounded Model Checking (BMC)** for Mediator systems. By translating the operational semantics of Mediator into **Satisfiability Modulo Theories (SMT)** formulas, we leverage the **Z3 Theorem Prover** to verify safety properties and invariant preservation within a bounded execution depth $k$. This approach allows for the rigorous detection of counterexamples (bugs) that may arise from complex component interactions.

## 2. Project Structure
The repository is organized to support both the core compiler infrastructure and the verification extensions:

*   **`org/fmgroup/mediator`**: Contains the core Java source code for the Mediator compiler, including the parser, type checker, and Abstract Syntax Tree (AST) definitions.
*   **`org/fmgroup/mediator/plugins/generators/z3`**: The specific package implementing the Z3 translation backend (`Z3Generator`). This is the focal point of current development.
*   **`models/`**: A collection of Mediator models used for testing, benchmarking, and validation.
    *   `medical_pump.med`: A representative CPS case study used for integration testing.
    *   `test_z3/`: A suite of unit tests targeting specific language features (arrays, tuples, control flow) to ensure translation correctness.
*   **`dev_tools/`**: Utilities facilitating the development and debugging workflow.
    *   `MediatorToZ3.java`: A command-line driver for invoking the Z3 generator on Mediator models.
    *   `Z3Debugger.py`: A Python-based instrumentation tool for analyzing generated SMT scripts and diagnosing `unsat` cores or unexpected results.
*   **`library/`**: Standard libraries for Mediator (e.g., `math.med`, `arduino.med`) providing essential primitive definitions.

## 3. Z3Generator Implementation Status
The `Z3Generator` class implements the `Generator` interface and is responsible for the translation pipeline from Mediator AST to SMT-LIB 2.0 standard format.

### 3.1 Current Capabilities
*   **AST Translation**: Implements a visitor pattern to traverse the Mediator AST, translating variable declarations, assignments, and guard conditions into SMT constraints.
*   **Symbolic State Encoding**: Maps Mediator types to corresponding Z3 sorts (e.g., `Int`, `Bool`, `Array`, `Datatypes`).
*   **Bounded Unrolling**: Encodes the system's transition relation as a sequence of constraints over discrete time steps $t = 0 \dots k$.
*   **Control Flow Handling**: Supports conditional logic via `IteTerm` (If-Then-Else) translation, ensuring correct path condition evaluation.
*   **Counterexample Synthesis**: Upon detecting a property violation (i.e., the negation of the property is `sat`), the generator constructs a readable, step-by-step trace of the system state, facilitating error analysis.

### 3.2 Recent Improvements
*   **Stability**: Resolved critical `NullPointerException` issues in `IteTerm` handling, ensuring robust translation of complex nested conditional expressions.
*   **Correctness**: Enhanced the generation logic for array bounds checking and type consistency.
*   **Usability**: Integrated automated counterexample formatting directly into the SMT footer, providing immediate visual feedback on variable states across time steps.

## 4. Future Work
To achieve full industrial-strength verification capabilities, the following areas are identified for future research and development:

1.  **Advanced Type System Support**: Complete the translation logic for deeply nested complex types, including unions within tuples and custom `typedef` structures, to support more expressive models.
2.  **Constraint Optimization**: Implement formula simplification strategies (e.g., cone-of-influence reduction, common subexpression elimination) to minimize the size of generated SMT queries and improve solver performance.
3.  **Unbounded Verification**: Extend the framework to support $k$-induction or invariant generation techniques, enabling the proof of properties for unbounded time horizons.
4.  **Native Function Expansion**: Broaden the support for external native functions and libraries, ensuring that platform-specific behaviors (e.g., Arduino hardware abstraction) are correctly modeled in the SMT domain.

   
some notes: when developing, we didn't notice the java codes in the repository out of the release folder by accident.As a consequence, we developed those things based on decompiled codes.It may have caused and will cause some problems i think, which is really embarrassing. 
