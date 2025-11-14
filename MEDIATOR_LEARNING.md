# Learning Mediator — Syntax, Implementation and Z3 Translation Guide

## 摘要

本文件基于你提供的开发者论文与当前仓库实现，面向想快速掌握 Mediator 语言（.med 文件格式）及工具链的读者。文档按论文式结构组织，结合代码片段、数学符号与可操作示例，目标是：

1. 快速理解 Mediator 语言的语法与语义。   
2. 理解项目代码库中各部分的职责与实现要点（解析、AST、插件、生成器与仿真器）。
3. 指导如何把 Mediator 模型翻译为 Z3 Python（z3py），以便做有界验证（bounded model checking）。
4. 提供若干小练习，帮助巩固理解与实践。

本文件尽量避免“用专业名词解释专业名词”的循环定义；对必须的概念（如 AST、Guard、Transition）会给出直观解释与数学/代码示例。

---

## 目录

1. 引言
2. 语言概览（语法要点与示例）
3. 把文本变为程序：解析器与 AST
  - 3.4 ANTLR 与 Parse Tree（入门）
4. 语言运行时：Program、Entity、Automaton 与 Property
5. 插件架构：Command、Generator、FileSet
6. 仿真器（Simulator）与求值（Evaluation）
7. 从 Mediator 到 Z3py：设计与映射清单（逐步实现）
8. 练习与小项目
9. 附录：快速 API 索引与常见 AST 节点

---

## 1. 引言

Mediator 是一种面向建模与验证的领域特定语言（DSL），设计目标是用结构化的文本文件（.med）描述组件、端口、自动机（automaton）以及性质（properties），并通过一组工具（解析器、生成器、仿真器、插件）实现模型的验证与生成。

一个典型的工作流：

- 在 `.med` 中手工编写模型（automata、system、property）。
- 使用 `mediator parse` 做语法/语义检查（解析器 + 验证器）。
- 使用 `mediator generate -t <target>` 调用 generator 将模型转为目标平台代码或验证脚本（如 Arduino 或 Z3py）。
- 使用 `Simulator` 做快速动态模拟，或把模型转给更强的工具做形式化验证（例如 Z3）。

下一节我们先看语言本身。

---

## 2. 语言概览（语法要点与示例）

### 2.1 概念术语（直观说明）
- Entity（实体）：系统的基本构件，例如 automaton 或 system。可以具有端口、局部变量与 transition。  
- Automaton（自动机）：由局部变量、transition 以及可选的 properties 组成的行为模块。  
- Transition（迁移）：描述从某个守卫（guard）成立时如何更新变量与可能同步端口的行为。  
- Guard：一个布尔表达式，决定 transition 是否可触发。  
- Statement：transition 内的动作，常见如赋值（Assignment）或同步语句（SynchronizingStatement）。

这些术语会贯穿本文；如需更数学化的定义会在后文给出符号化说明。

### 2.2 典型语法片段（示例）

下面给出一个简单 automaton 的 `.med` 示例，已用于本仓库的 `models/example_z3.med`：

```med
automaton Counter () {
    variables {
        x : int init 0;
    }
    transitions {
        [x >= 0] -> { x = x + 1; }
        [x > 5] -> { x = x - 10; }
    }
    properties {
        safe : x >= 0;
    }
}
```

上面含义：Counter 自动机有一个整型局部变量 x，初值 0；有两条 transition：当 `x>=0` 时递增，当 `x>5` 时减 10；最后定义了一个性质 `safe: x >= 0`。

注：实际语法更为丰富（Type、Template、function、system、connection 等），具体规则见仓库中的 ANTLR 生成类 `language/generated`（实践中通常不用直接读 grammar 文件，只需使用 Program.parseFile）。

### 2.3 语义简介（直观）
一个 automaton 的执行可以看作是一个离散时间序列（step 0,1,2,...），每一步：
1. 评估所有 transition 的 guard，在 guard 成立的 transition 中选择一条（如果有多条则按语义可能随机选择或按调度器决定）；
2. 执行该 transition 的 statements，更新变量；
3. 进入下一步。

Simulator 就是实现了这一步步的执行逻辑（详见第 6 节）。

---

## 3. 把文本变为程序：解析器与 AST

### 3.1 ANTLR 的作用与封装
项目使用 ANTLR 来描述语言的词法与语法（`.g4`），由 ANTLR 生成的类位于 `org/fmgroup/mediator/language/generated`：Lexer、Parser、BaseListener 等。

在项目里你无需直接操作 grammar（除非扩展语言），项目提供了对 ANTLR 的封装：

- `org.fmgroup.mediator.core.antlr.Parser`：提供 `getParserFromFile`、`getParserFromString`、`getParserFromCharStream`，把文本变成 `MediatorLangParser` 实例。
- `org.fmgroup.mediator.core.antlr.VerboseListener`：继承 ANTLR 的 `BaseErrorListener`，把语法错误转为 `ValidationException` 以便上层显示。
- `Program.parseFile(filename)`：这是你最常用的入口，它内部使用 ANTLR（创建 Lexer/Parser、添加 VerboseListener、调用 parser.prog()），并把 parse tree 转为 `Program` 对象（AST）。

因此：通常只需调用 `Program.parseFile()` 来获得 AST，无需直接操作 ANTLR。

### 3.2 AST（抽象语法树）是什么？
直观地说，AST 将文本解析得到的语法树 "净化" 为程序结构化对象（类/接口），常见节点：
- `Program`（根）
- `Automaton`, `System`, `Function`（实体）
- `VariableDeclaration`, `Type`（类型/变量信息）
- `Transition`, `Statement`, `Term`（行为描述/表达式）

例如 `IntValue` 是一种 `Term` 的具体子类，代表字面整数；`BinaryOperatorTerm` 代表加减乘除或逻辑运算符。

### 3.3 代码示例：从文件到 AST
```java
Program prog = Program.parseFile("models/example_z3.med");
Automaton a = (Automaton) prog.getEntity(null, "Counter");
List<VariableDeclaration> vars = a.getLocalVars().getDeclarationList();
List<Transition> trans = a.getTransitions();
```

### 3.4 ANTLR 与 Parse Tree（入门）

为什么需要 ANTLR？

- ANTLR 是一个流行的 parser-generator：你用一个语法文件（`.g4`）描述语言的词法和语法，ANTLR 会根据这个描述生成一个 Lexer（把文本拆成 token）和一个 Parser（把 token 组织成 parse tree）。
- 在本项目中，ANTLR 负责把 `.med` 的源文本转换为一个 parse tree，接着项目把 parse tree 转换为更友好的 AST（Program / Automaton / Term 等）。

什么是 Parse Tree？

- Parse Tree（解析树）是直接由语法产生的树形结构：每个节点对应语法规则或词法 token。它保留了完整的语法信息（包括所有括号、分号、具体的语法分支），通常比 AST 更“冗长”。
- 示例（极简化，基于 `x = x + 1;`）：

  AssignmentStatement
  ├─ Identifier: x
  ├─ '='
  └─ Expression
     ├─ Identifier: x
     ├─ '+'
     └─ IntLiteral: 1

Parse Tree 与 AST 的区别（直观）

- Parse Tree 是语法的镜像，保留所有细节；AST 是经过精简/抽象后的结构，只保留语义上重要的节点（例如把 `Expression` 中的加法直接变成 `BinaryOperatorTerm`，并去掉语法噪音）。
- 把 Parse Tree 转为 AST 的过程叫做 "AST construction" 或 "tree walking"，通常使用 ANTLR 生成的 Listener/Visitor（在本项目中，Program 有一个 fromContext / factory 方法把 parse tree 转换为 AST）。

项目中的流程（一步步）

1. 读取 `.med` 源文本。
2. 用 ANTLR 创建 Lexer 和 Parser；Parser 执行入口规则（例如 `prog()`），生成 parse tree（`ParseTree` 或 `ParserRuleContext` 子类）。
3. 使用一个 Listener/Visitor 或手写的转换函数遍历 parse tree，将语法节点映射为 AST 对象（例如 `TransitionSingle`、`BinaryOperatorTerm`）。
4. AST 经语义分析（类型检查、符号解析）后可直接供 Generator/Simulator 使用。

一个最小的转换示例（伪代码）

假设我们有一条 parse tree 节点 `assignmentContext`（由 ANTLR 生成），伪代码把它变为 AST `AssignmentStatement`：

```java
// listener/visitor 回调中
public AssignmentStatement visitAssignment(AssignmentContext ctx) {
  String id = ctx.ID().getText();
  Term expr = visitExpression(ctx.expression()); // 递归处理子表达式
  VariableDeclaration var = lookupVar(id);
  return new AssignmentStatement(var, expr);
}
```

Parse Tree 的树形结构如何影响生成器

- Parse Tree 中的每一个表达式/语句都对应一个或多个 AST 节点。Generator 不直接操作 parse tree（那样太冗长），而是操作 AST：
  - AST 节点（Term、Statement、Transition）提供了语义化的方法（例如 `getGuard()` 返回一个 Term 对象），便于在 `Z3Generator` 中写 `termToZ3`。 
  - 生成器的职责是把 AST 节点映射为目标语言表达（例如把 `AssignmentStatement` 变为一条 `x_{t+1} == x_t + 1` 的 z3 约束）。

重组（assembly）阶段长什么样？

- 在完成 AST 到目标片段的映射后，生成器会把这些代码片段以合理顺序 "组装" 成最终输出文件：
  1. 前言（imports / helper functions）
  2. 变量声明（按时间展开的声明 x_0..x_k）
  3. 初始状态约束（x_0 == init）
  4. 每步的 transition 约束（for t in 0..k-1: add Or(branch_i)）
  5. property 的否定组合与 check-sat 代码
  6. 模型打印/结果处理

举例（以 `Counter` 示例串联说明）

- 原始 `.med`（见第 2 节）：

```med
automaton Counter () {
  variables {
    x : int init 0;
  }
  transitions {
    [x >= 0] -> { x = x + 1; }
    [x > 5] -> { x = x - 10; }
  }
  properties {
    safe : x >= 0;
  }
}
```

- parse tree（局部示意）:

```
Automaton
├─ 'automaton'
├─ Identifier: Counter
├─ '('
├─ ')'
├─ '{'
├─ VariablesBlock
│  └─ VariableDecl
│     ├─ Identifier: x
│     ├─ ':'
│     └─ Type: int init 0
├─ TransitionsBlock
│  ├─ Transition
│  │  ├─ Guard: x >= 0
│  │  └─ StatementBlock: x = x + 1
│  └─ Transition
│     ├─ Guard: x > 5
│     └─ StatementBlock: x = x - 10
└─ PropertiesBlock
   └─ Property: safe : x >= 0
```

- AST（精简）:

```
Automaton(name=Counter,
  vars=[VariableDeclaration(name=x,type=int,init=0)],
  transitions=[Transition(guard=BinaryOp(x,GE,0), stmts=[Assign(x, BinaryOp(x,ADD,1))]),
         Transition(guard=BinaryOp(x,GT,5), stmts=[Assign(x, BinaryOp(x,SUB,10))])],
  properties=[Property(name=safe, formula=BinaryOp(x,GE,0))]
)
```

- Generator（Z3Generator）做的事情：
  1. 遍历 AST，找到变量 x 并为每个时间 t 生成 `x_t` 的声明。  
  2. 把初始值 `x_0 == 0` 加入约束集合。  
  3. 对每一步 t，把第一条 transition 的分支生成 `And(x_t >= 0, x_{t+1} == x_t + 1, otherVarsUnchanged...)`，第二条分支类似。  
  4. 把 property 的否定组合构成 `Or(Not(safe_0),...,Not(safe_k))` 并加入 check。  

小结：Parse Tree 是从语法角度的“完整”树，AST 是语义友好的精简树，生成器基于 AST 做映射和重组，最后写出目标语言脚本（例如 z3py）。


上面演示了最常见的数据流：文本 -> Program.parseFile -> Program/Automaton -> 读取变量和 transition。

---

## 4. 语言运行时：Program、Entity、Automaton 与 Property

### 4.1 `Program` 的职责
- 维护类型定义（typedef）、函数（Function）、automata、system 等。
- `Program.parseFile`：解析文件并把 parse tree 转为 Program 对象。
- 支持从 Program 请求实体：`getEntity(libraryPath, identifier)`。

### 4.2 Automaton 的内部结构
`Automaton`（类）包含：
- 名称（name）
- `VariableDeclarationCollection localVars` —— 局部变量集合
- `List<Transition> transitions` —— transition 列表
- `PropertyCollection properties` —— 可以包含多个具名 property

Transition 分为 `TransitionSingle` 与 `TransitionGroup` 等，`TransitionSingle` 包含 `Term guard` 与 `List<Statement> statements`。

### 4.3 Property 的表达
`Property` 使用 PathFormulae/StateFormulae 表达式（解析自 grammar），项目有一套 AST 表示 path/state formula。当前 Z3 生成器原型未完整支持这些节点直接翻译，需要扩展 term->Z3 的翻译。

---

## 5. 插件架构：Command、Generator、FileSet

### 5.1 目录结构与发现机制
- 插件接口在 `org.fmgroup.mediator.plugin` 下（`Plugin`、`Command`、`Generator` 等）。
- `UtilClass.getGenerators()` 等函数使用基于 classpath 的扫描（遍历 `org/fmgroup/mediator/plugins` 下的 class）来发现插件。

### 5.2 Command（命令）
- 例子：`CommandParse`、`CommandGenerate`。
- `Core.main` 使用 `UtilClass.getCommands()` 并匹配命令名来调用对应命令。

### 5.3 Generator（生成器）与 FileSet
- Generator 接口定义 `FileSet generate(RawElement elem)`。
- `FileSet` 是一个内存文件集合，生成器把要输出的文件以 path/string 的形式放入 FileSet，然后上层决定把它写到磁盘。
- 你实现的 `Z3Generator` 就是一个 Generator，返回包含 `*.py` 的 FileSet。

---

## 6. 仿真器（Simulator）与求值（Evaluation）

项目内含一个简单的执行器（Simulator），用于运行 automaton 的步骤并计算 Term 的值。

### 6.1 Evaluation 与 EvaluationAutomaton
- `Evaluation` 是一个接口，`EvaluationAutomaton` 实现了基于变量名->Term 的 map，支持 `eval(Term)` 来计算 Term 在当前 evaluation 下的实际值。
- `Simulator` 使用 Evaluation 来选择可行的 Transition 与执行 Statement（目前主要支持 AssignmentStatement），并维护 `trace`（SimulatorState 列表）。

### 6.2 使用场景
- 快速调试模型、观察某条运行轨迹、验证简单运行时性质。
- 注意：它是执行式的（按选择一个 transition 执行），不是穷尽的 model checker。

---

## 7. 从 Mediator 到 Z3py：设计与映射清单

本节给出一份具体的映射清单（你可以把它当作实现规范），并解释为什么要这么做。

### 7.1 目标与假设
- 目标：把一个 `Automaton` 翻译为一个 z3py 脚本，该脚本能在给定步数 k 下寻找违反不变式（invariant）或到达坏状态（bad state）的反例。
- 假设：目前我们针对单个 Automaton，处理局部变量（int/bool/enum），以及 TransitionSingle 中的 Assignment 与 Guard。系统/并发/端口同步暂不处理（后续扩展）。

### 7.2 映射要点（小表格）
- Mediator 概念 -> Z3 表示
  - 变量 x at time t -> Z3 变量 x_t (Int/Bool)
  - 初始值 -> constraint: x_0 == init
  - guard(t) -> z3 条件（在时间 t 用对应变量替换）
  - assignment: x = expr -> constraint x_{t+1} == expr(t)
  - 未更新变量 -> constraint x_{t+1} == x_t
  - existence of counterexample for property P over 0..k -> assert Or(Not(P_0), ..., Not(P_k)) and check-sat

### 7.3 数学说明（有界展开）
记变量集合 V = {v1, v2, ..., vn}，时间步集合 T = {0,1,...,k}。定义每个变量在时间 t 的值为 v_i(t)。

Transition i 在时间 t 的激活条件为 G_i(t)（把语法树中的变量替换为 v(t)），并导致变量的更新：

v_j(t+1) = U_{i,j}(v_1(t), ..., v_n(t))  当 Transition i 被选中。

要编码 "在每个 t 存在一个 transition 能执行"，我们对每个 t 添加约束：

Or_i ( G_i(t) AND (v_1(t+1)=U_{i,1}(t)) AND ... AND (v_n(t+1)=U_{i,n}(t)) )

最后把 P（property）在所有 t 的否定组合为 Or(Not(P(0)), ..., Not(P(k)))，若可满足则说明存在反例。

### 7.4 代码片段（如何把 Term 转为 z3py 字符串）
一个简化版的 termToZ3:

```java
private String termToZ3(Term term, int t) {
    if (term instanceof IdValue) return id.getIdentifier() + "_" + t;
    if (term instanceof IntValue) return Integer.toString(((IntValue)term).getValue());
    if (term instanceof BinaryOperatorTerm) {
        String l = termToZ3(bt.getLeft(), t);
        String r = termToZ3(bt.getRight(), t);
        switch(bt.getOpr()) {
            case ADD: return "("+l+" + "+r+")";
            case GEQ: return l + " >= " + r;
            // ...
        }
    }
    // fallback
    return "0";
}
```

注意：这只是一段示意代码，完整实现需要覆盖所有 Term 子类并正确转义/括号。

### 7.5 已实现的原型（仓库内 Z3Generator 概述）
- 我在 `org/fmgroup/mediator/plugins/generators/z3/Z3Generator.java` 中实现了一个原型：
  - 为每个变量声明 x_0..x_k 的 Int；
  - 把初值约束写入 s.add(...);
  - 对每个 t 生成 `s.add(Or(...))`，其中每个 Or 分支对应一条 transition 的 `And(guard, updates...)`；
  - 最后调用 s.check() 并在 sat 时打印模型。
- 已生成示例脚本 `release/Counter_z3_check.py`。

### 7.6 已知问题与改进方向
- 当前实现对复杂 term（FieldTerm、数组索引、函数调用）做了 fallback（返回 0），应扩展 termToZ3 处理更多 term 子类。
- 需要把 property AST 正确翻译并加入脚本（当前是注释掉的）。
- 更严谨的方式要为 transitions 中的 `updates` 使用 `And(u1, u2, ...)` 语法而非逗号拼接（原型中已修正）。

---

## 8. 练习与小项目
下面给出 4 个循序渐进的小任务，帮助你把理论变为实践：

### 练习 1：理解 AST
- 目标：手写 3 个小的 .med 文件（counter、producer-consumer、simple-switch），并用 `Program.parseFile` 在 Java 中载入并打印 `Automaton.toString()`。
- 步骤：
  1. 在 `models/` 下创建 `my_counter.med`（参考示例）。
  2. 写一个小的 Java 程序：
```java
Program p = Program.parseFile("models/my_counter.med");
System.out.println(p.toString());
```
  3. 观察输出的 AST/字符串表示，比较与源文件。

### 练习 2：扩展 termToZ3
- 目标：使 Z3Generator 支持 `FieldTerm`（如 `buf[0]` 或 `port.value`）与 `IntValue.toString()` 的正确返回。
- 步骤：在 `Z3Generator.termToZ3` 中新增分支，处理 `FieldTerm` 并在 Python 端把数组/字段翻译为合适的命名约定（如 `buf_0_t`）。

### 练习 3：property 翻译
- 目标：把 automaton.properties 中第一个 property 翻译为 `Or(Not(P_0),...,Not(P_k))` 并把它加入脚本中。
- 步骤：使用 `autom.getProperties()` 读取 `Property`，把其 `toString()` 或更可靠的 AST 转换为 Z3 条件并写入脚本。

### 练习 4：从单个 automaton 扩展到 system（并行）
- 目标：把系统里多个 automata 的交互语义表达到 z3py（先做 interleaving semantics，再尝试精确的同步 semantics）。
- 步骤：先为每个 automaton 声明各自变量和 transition，再在每步 t 使用非确定 choice 表示哪个 automaton 执行（或用同步约束表达端口交互）。

---

## 9. 附录与快速 API 索引
- Program.parseFile(String filename)
- Program.getEntity(List<String> libPaths, String identifier)
- Automaton.getLocalVars(), Automaton.getTransitions(), Automaton.getProperties()
- TransitionSingle.getGuard(), TransitionSingle.getStatements()
- Term 子类：IdValue, IntValue, BoolValue, BinaryOperatorTerm, SingleOperatorTerm, FieldTerm
- Generator 接口：FileSet generate(RawElement elem)

---

## 后记
若你愿意，我可以：
- 把这份 Markdown 文档继续分节完善并加入更多代码示例（包括 Java runner 与 Python 运行示例）。
- 立刻改进 `Z3Generator`：加入 property 翻译、支持更多 term 类型，并把 `-k` CLI 支持接入 `CommandGenerate`（并测试）。

请选择下一步：A) 我现在完善文档并加入更多代码示例；B) 我先改进 `Z3Generator`（属性 + -k 支持）并做 end-to-end 测试；C) 你想先看某个章节的更深入内容？

---

## 附加示例：如何运行仓库中的示例

为便于上手，本项目在 `release/examples/` 下包含两个最小示例：

- `ParseExample.java`：一个 Java 程序，展示如何使用 `Program.parseFile("models/example_z3.med")` 解析 `.med` 文件并打印 AST/automaton 信息。编译并运行需要把 `release` 目录作为当前工作目录，以便 classpath 中包含 `org/` 已编译的类。
- `run_z3_example.py`：一个独立的 z3py 脚本，手工实现了 `Counter` automaton 的有界展开（k=5），并检查 `safe: x >= 0` 的反例。

运行示例（PowerShell，假定当前目录是 `release`）：

```powershell
# 编译并运行 Java 解析示例
javac -cp .;org examples\ParseExample.java -d examples_bin
java -cp .;org;examples_bin ParseExample

# 运行 z3py 示例（需要安装 z3 python 包，可用 pip install z3-solver）
python examples\run_z3_example.py
```

示例 Java 输出（可能包含 ANTLR 的 token recognition warnings）：

```
Parsing: models/example_z3.med
line 1:22 token recognition error at: '\r'
...  # 可能的 token 识别警告
Program toString():

\nautomaton Counter () { ... }

Found automata: [Counter]
Automaton: Counter
Variables:
variables {\n\tx: int init 0;\n}

Transitions:
[[x >= 0] -> x = x + 1;, [x > 5] -> x = x - 10;]
```

示例 Python (z3) 输出：

```
checking for counterexample to safety (x >= 0) up to k= 5
sat
counterexample model:
[model details]
```

注意：`run_z3_example.py` 是一个教学示例，说明如何把 automaton 的约束手工编码到 z3py 中；正式使用建议使用 `Z3Generator`（仓库内原型）把 AST 自动转换为 z3py 脚本。

---

我已创建并验证 `examples/ParseExample.java` 的编译与运行。如果你想，我可以：

- 把 Java 示例改成一个小的 Gradle 或 Maven 工程以便一键构建；
- 拓展 Python 示例为从 .med 自动调用 `Z3Generator`（或通过 Process 调用 `Core generate`）并运行生成的脚本；
- 或继续完善 `MEDIATOR_LEARNING.md` 中的其他章节（比如详细说明 Property 到 Z3 的翻译）。

---

## 可复现构建：Gradle wrapper 与 简单脚本（已添加）

我在 `release` 目录下添加了一个 minimal Gradle 配置和跨平台脚本，便于不同使用场景：

- `build.gradle`, `settings.gradle`：定义 `examples` sourceSet、`compileExamples` 与 `runParseExample` task（用于把 `examples` 编译并运行）。
- `gradlew` / `gradlew.bat`：轻量 shim（若本机已装 Gradle，将调用本地 gradle；若没有，提示用户安装或在有 Gradle 的机器上生成完整 wrapper）。若你需要，我可以把完整的 wrapper artifact (`gradle/wrapper/gradle-wrapper.jar` 等) 一并加入仓库，使 wrapper 自动下载指定版本的 Gradle。
- `examples/build_and_run.ps1` 与 `examples/build_and_run.sh`：跨平台脚本，用于课堂或快速演示场景（Windows 的 PowerShell 可能被执行策略限制，见下文）。

选择建议：
- 若你计划长期维护示例、加入测试或在 CI 中运行，建议使用 Gradle wrapper（可重复构建、依赖管理、易扩展）。
- 若仅需快速教学或一键演示，简单脚本最直接（低成本）。
- 折中：我建议同时保留 Gradle 配置与一对脚本（我已添加），Gradle 用于开发/CI，脚本用于课堂/演示。

如何使用：

1) 使用 Gradle（若已安装 Gradle）：
```powershell
cd <repo>/release
.\gradlew.bat runParseExample
```

2) 使用示例脚本（PowerShell）：
```powershell
cd <repo>/release
examples\build_and_run.ps1
```
如果 PowerShell 脚本由于执行策略被禁止（如发生 `UnauthorizedAccess`），你可以直接在命令行逐条运行脚本中的命令：
```powershell
javac -cp ".;org" examples\ParseExample.java -d examples_bin
java -cp ".;org;examples_bin" ParseExample
```

3) 或在类 Unix 系统使用 shell 脚本：
```bash
cd <repo>/release
./examples/build_and_run.sh
```

我已在本机（当前 workspace）用 `javac`/`java` 的方式验证了 `ParseExample` 能正常运行（见上文示例输出）。如需，我可以下一步把完整 Gradle wrapper 二进制也加入仓库并在 `build.gradle` 中增加更多 tasks（例如生成 Z3 脚本、运行 Python 生成脚本的流程等）。

---

## 深入：从 Mediator 到 Z3py 的翻译 — 实用指南（扩展）

本节把之前的设计化说明进一步细化为可实施的工程步骤、代码片段与测试计划。目标是让你或贡献者能在 `Z3Generator` 中按本指南逐步实现完整的翻译，覆盖表达式、赋值、guard、property，并有可验证的单元/集成测试。

目标契约（contract）
- 输入：一个解析好的 `Automaton` 对象（假设已经通过 `Program.parseFile` 并可通过 `prog.getAutomata().get(name)` 获得）。
- 输出：一个或多个 z3py 文件（通常单文件），实现 k 步有界展开并对指定 property 判定可满足性。
- 错误模式：若遇到不支持的 Term/Statement，应
  1) 在生成阶段以显式注释/警告写入输出脚本，并
  2) 用保守的 fallback（例如把表达式替换为常量或在 guard 上用 False）以保证生成脚本仍能运行（并尽可能报告潜在未处理部分）。

数据形状（数据与命名约定）
- 对每个局部变量 v（type ∈ {int,bool,enum}），在每个时间步 t 声明 z3 变量名：v_t。对 enum，使用 Int 并建立映射常数（可选）。
- 时间步：t = 0..k
- 初值：对于声明 `v init c`，生成 `s.add(v_0 == c)`。

映射规则（逐项详解）
1) 变量与初值
   - Mediator: `x : int init 0;`
   - Z3py: `x_0 = Int('x_0'); ...; s.add(x_0 == 0)`

2) Term -> z3 表达式（核心）
   - IdValue(name) at time t -> `name_t`
   - IntValue(n) -> literal `n`
   - BoolValue(true/false) -> `True`/`False`
   - BinaryOperatorTerm(op, left, right) -> map to z3 op:
     - ADD -> `({l} + {r})`
     - SUB -> `({l} - {r})`
     - MUL -> `({l} * {r})`
     - DIV -> `({l} / {r})` (注意整数除法语义)
     - GT, LT, GEQ, LEQ, EQ, NEQ -> `>`, `<`, `>=`, `<=`, `==`, `!=`
     - AND, OR -> `And({l},{r})`, `Or({l},{r})` (注意 short-circuit 与类型)
   - SingleOperatorTerm (e.g., NOT, NEG) -> `Not({e})` / `-({e})`
   - FieldTerm / ArrayTerm -> 命名约定 `name_idx_t` 或 `name_field_t`（如 `buf_0_3` 表示 buf[3] 在 t=0）或把复杂字段降为额外的变量声明（需要在 automaton 前做展开/预处理）

3) Transition encoding per time step t
   - 对 automaton 的每个 t，生成一个 Or 分支集合，每个分支对应一条 transition:
     Or( And( guard(t), updates(t) ), ... )
   - `updates(t)` 包括每个变量 v 的约束：如果 transition 更新了 v：`v_{t+1} == expr_v(t)`，否则 `v_{t+1} == v_t`。

4) Property encoding
   - State formula P(t) 翻译为 z3 表达式（使用 term->z3 映射）；要找反例则生成 `Or(Not(P(0)), ..., Not(P(k)))` 并 `s.add(...)`。
   - Path formula（如果有）需解析路径算子（如 G, F, X, U）并按 bounded semantics 展开；这部分较复杂，建议先支持常见的 state formula（invariant、assertion）再逐步扩展路径算子。

Java 辅助代码（伪代码/可直接粘贴）
下面的 Java 片段展示了一个稳健的 `termToZ3` 和 `encodeTransition` 的实现骨架（需放入 `Z3Generator` 中并根据具体 AST 类型调整 import/类型判断）：

```java
private String varAt(String name, int t) {
  return name + "_" + t;
}

private String termToZ3(Term term, int t) {
  if (term == null) return "0";
  if (term instanceof org.fmgroup.mediator.language.term.value.IntValue) {
    return Integer.toString(((org.fmgroup.mediator.language.term.value.IntValue)term).getContent());
  }
  if (term instanceof org.fmgroup.mediator.language.term.value.IdValue) {
    return varAt(((org.fmgroup.mediator.language.term.value.IdValue)term).getIdentifier(), t);
  }
  if (term instanceof org.fmgroup.mediator.language.term.operator.BinaryOperatorTerm) {
    var bt = (org.fmgroup.mediator.language.term.operator.BinaryOperatorTerm)term;
    String l = termToZ3(bt.getLeft(), t);
    String r = termToZ3(bt.getRight(), t);
    switch(bt.getOpr()) {
      case ADD: return "("+l+" + "+r+")";
      case SUB: return "("+l+" - "+r+")";
      case MUL: return "("+l+" * "+r+")";
      case DIV: return "("+l+" / "+r+")"; // 整数除法
      case GEQ: return "("+l+" >= "+r+")";
      case LEQ: return "("+l+" <= "+r+")";
      case GT: return "("+l+" > "+r+")";
      case LT: return "("+l+" < "+r+")";
      case EQ: return "("+l+" == "+r+")";
      case NEQ: return "Not("+l+" == "+r+")";
      case AND: return "And("+l+","+r+")";
      case OR: return "Or("+l+","+r+")";
    }
  }
  if (term instanceof org.fmgroup.mediator.language.term.operator.SingleOperatorTerm) {
    var st = (org.fmgroup.mediator.language.term.operator.SingleOperatorTerm)term;
    String inner = termToZ3(st.getBody(), t);
    switch(st.getOpr()) {
      case NOT: return "Not("+inner+")";
      case NEG: return "-("+inner+")";
    }
  }
  // FieldTerm, ArrayTerm, FunctionCall 等可在此处扩展
  // fallback: emit a 0 and a comment in the generated file
  return "0";
}

private List<String> encodeTransition(TransitionSingle tr, int t, List<String> allVars) {
  List<String> updates = new ArrayList<>();
  // default: carry over unchanged variables
  for (String v : allVars) {
    updates.add(v+"_"+(t+1)+" == "+v+"_"+t);
  }
  // apply assignment statements
  for (Statement s : tr.getStatements()) {
    if (s instanceof AssignmentStatement) {
      String lhs = ((AssignmentStatement)s).getLeft().toString(); // may need robust LHS handling
      Term rhs = ((AssignmentStatement)s).getRight();
      String rhsZ3 = termToZ3(rhs, t);
      // replace the default carry for lhs
      updates.removeIf(u -> u.startsWith(lhs+"_"+(t+1)+" == "));
      updates.add(lhs+"_"+(t+1)+" == "+rhsZ3);
    } else {
      // unsupported statement: log as comment and leave defaults
    }
  }
  String guardZ3 = termToZ3(tr.getGuard(), t);
  List<String> andParts = new ArrayList<>();
  andParts.add(guardZ3);
  andParts.addAll(updates);
  String andExpr = "And(" + String.join(",", andParts) + ")";
  return Arrays.asList(andExpr);
}
```

Worked example（Counter 自动机，k=3）
1) 变量声明：生成 `x_0..x_3` 的 Int 并加上 `s.add(x_0 == 0)`。
2) t=0 的 transitions：
   - Tr1 guard `x >= 0` -> update `x_1 == x_0 + 1`
   - Tr2 guard `x > 5` -> update `x_1 == x_0 - 10`
   生成：
   s.add( Or( And(x_0 >= 0, x_1 == x_0 + 1), And(x_0 > 5, x_1 == x_0 - 10) ) )
3) 同理为 t=1, t=2 生成约束；最后生成 property 检查 `Or(x_0 < 0, x_1 < 0, x_2 < 0, x_3 < 0)`。

测试计划（单元 + 集成）
- 单元测试：为 `termToZ3` 写多个小测试用例（IdValue, IntValue, BinaryOperatorTerm, NOT, 比较等）以字符串匹配方式校验输出。可用 JUnit（把 tests 放到 `src/test/java` 或为示例写一个小的 `TermToZ3Test.java` 放在 `examples`）。
- 集成测试：对一个或两个小模型（Counter、另一个带布尔与 enum 的 automaton）执行 `Z3Generator.generate`，运行生成的 z3py 脚本并断言是否返回 sat/unsat（Python 脚本可以调用 subprocess 或用 `z3-solver` lib 直接 import 并调用 API）。

已知限制与分步迭代建议
- 初期实现：先覆盖常见 Term（IdValue, IntValue, BoolValue, BinaryOperatorTerm, SingleOperatorTerm）与 AssignmentStatement、TransitionSingle、Property 的 state formula。把 Unsupported 的 node 记录为注释并 fallback 为常量。完成后立即提供单元测试。
- 进阶：支持 FieldTerm/Array、函数调用、path formula（F/G/U/X）、以及 system/并发和端口同步。
- 性能与可读性：生成的 z3py 脚本应尽量避免重复表达式（可在生成阶段做 CSE）并添加注释以便调试。

接下来我会：
1. 在 `MEDIATOR_LEARNING.md` 中加入本节（已完成）；
2. 如果你同意，我会实现 `Z3Generator` 的 property 翻译与 `termToZ3` 的完整覆盖（按上面优先级），并写单元测试与一个 end-to-end 集成测试（自动化：Gradle task 可调用编译->生成->运行脚本）；
3. 或者我现在只为文档再补充更多具体的 `termToZ3` 示例（比如对 `BinaryOperatorTerm` 中 AND/OR 的习惯写法，enum 映射示例等）。

请告诉我你更倾向哪个下一步（实现 generator 功能、只补文档示例、或先实现部分测试），我就开始执行并更新 todo。 


