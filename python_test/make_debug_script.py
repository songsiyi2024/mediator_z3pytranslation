import sys

def instrument(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

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
                    new_content += f'\nprint(f"Constraint {add_count} check: {{s.check()}}")\n'
                    # Optional: if unsat, stop to avoid noise, or print reason? 
                    # For now just print check.
        
        i += 1

    with open(output_file, 'w') as f:
        f.write(new_content)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python make_debug_script.py <input> <output>")
        sys.exit(1)
    instrument(sys.argv[1], sys.argv[2])
