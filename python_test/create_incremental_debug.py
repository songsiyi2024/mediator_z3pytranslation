
import re

with open(r'c:\Users\Tangzc\home\SMS\courses\CP\paper\mediator\mediator\release\python_test\testbench_z3_check.py', 'r') as f:
    content = f.read()

parts = content.split('s.add(Or(')

new_content = parts[0]

for i in range(1, len(parts)):
    part = parts[i]
    
    if "Property m_safe violation condition" in part:
        new_content += 's.add(Or(' + part
        continue

    new_content += 's.add(Or(' + part
    
    check_code = f'''
print("Checking step {i}...")
if s.check() == unsat:
    print("Unsat at step {i}")
    exit()
else:
    print("Sat at step {i}")
'''
    new_content += check_code

with open(r'c:\Users\Tangzc\home\SMS\courses\CP\paper\mediator\mediator\release\python_test\debug_z3_incremental.py', 'w') as f:
    f.write(new_content)
