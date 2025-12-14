import sys
import re
import argparse

def instrument_step_mode(content):
    """
    Inserts checks after s.add(Or(...)), which typically corresponds to 
    transition steps or property checks in the generated Z3 script.
    """
    # This regex looks for s.add(Or( and captures the content until the matching closing parenthesis.
    # However, matching nested parentheses with regex is hard. 
    # We will use a simpler heuristic: split by the start marker, similar to the original script,
    # but cleaner.
    
    parts = content.split('s.add(Or(')
    new_content = parts[0]
    
    print(f"Found {len(parts)-1} 's.add(Or(...))' blocks.")

    for i in range(1, len(parts)):
        part = parts[i]
        
        # Reconstruct the split token
        current_block = 's.add(Or(' + part
        
        # Add the check logic
        check_code = f'''
print(f"  [Debug] Checking after block {i}...")
if s.check() == unsat:
    print(f"  [Result] UNSAT detected at block {i}!")
    print(f"  [Info] This likely corresponds to step {{ {i}-1 }} or a property check.")
    exit()
else:
    print(f"  [Result] SAT at block {i}")
'''
        new_content += current_block + check_code
        
    return new_content

def instrument_all_mode(content):
    """
    Inserts checks after EVERY s.add(...) constraint.
    Uses a simple parser to handle nested parentheses.
    """
    new_content = ""
    depth = 0
    in_add = False
    add_count = 0
    
    i = 0
    while i < len(content):
        char = content[i]
        new_content += char
        
        # Detect start of s.add(
        if not in_add and content[i:i+6] == 's.add(':
            in_add = True
            depth = 0
            # We are at 's', the loop will continue and eventually hit '(' at i+5
        
        if in_add:
            if char == '(':
                depth += 1
            elif char == ')':
                depth -= 1
                if depth == 0:
                    in_add = False
                    add_count += 1
                    # Insert debug print
                    check_code = f'''
print(f"  [Debug] Checking constraint {add_count}...")
if s.check() == unsat:
    print(f"  [Result] UNSAT detected at constraint {add_count}!")
    exit()
'''
                    new_content += check_code
        
        i += 1
    
    print(f"Instrumented {add_count} constraints.")
    return new_content

def main():
    parser = argparse.ArgumentParser(description="Instrument a Z3 Python script with incremental checks to debug UNSAT results.")
    parser.add_argument("input_file", help="Path to the input Z3 Python script")
    parser.add_argument("-o", "--output", help="Path to the output instrumented script (default: debug_<input_file>)")
    parser.add_argument("--mode", choices=['step', 'all'], default='step', help="Instrumentation mode: 'step' (checks after transitions) or 'all' (checks after every constraint)")

    args = parser.parse_args()

    input_path = args.input_file
    output_path = args.output if args.output else "debug_" + input_path.split('/')[-1].split('\\')[-1]

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_path}' not found.")
        sys.exit(1)

    print(f"Instrumenting '{input_path}' in '{args.mode}' mode...")

    if args.mode == 'step':
        new_content = instrument_step_mode(content)
    else:
        new_content = instrument_all_mode(content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

    print(f"Done. Debug script written to '{output_path}'.")
    print(f"Run it with: python {output_path}")

if __name__ == "__main__":
    main()
