# Z3Generator 
## 核心实现部分
- Z3Generator: 核心代码生成器，先使用Scheduler算法将system展平成automaton，随后调用函数解析mediator模型，逐层实现对term和transition的转化
- TestZ3Generation: 简单实现的测试入口

## 进一步方向
- 优化项目架构，实现与原Generator调用模式的协调
- 强化测试，验证转换程序正确性
- 尝试引入property描述与转化
- 精简内容，删除测试用脚本
- 考虑引入异步逻辑转化的可能性
