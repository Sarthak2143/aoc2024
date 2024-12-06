import re

with open('input.txt') as f:
    data = f.read()

# First, let's find all instructions (both mul and control instructions)
# We'll store them with their positions so we know their order
instructions = []

# Find multiplication instructions with their positions
mul_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
for match in re.finditer(mul_pattern, data):
    instructions.append({
        'type': 'mul',
        'position': match.start(),
        'num1': int(match.group(1)),
        'num2': int(match.group(2))
    })

# Find control instructions (do and don't)
control_pattern = r'(?:do|don\'t)\(\)'
for match in re.finditer(control_pattern, data):
    instructions.append({
        'type': 'control',
        'position': match.start(),
        'action': match.group(0)
    })

# Sort instructions by their position to process them in order
instructions.sort(key=lambda x: x['position'])

# Process instructions in order
enabled = True  # Multiplications start enabled
total = 0

for instruction in instructions:
    if instruction['type'] == 'control':
        # Update enabled state based on control instruction
        enabled = (instruction['action'] == 'do()')
    elif instruction['type'] == 'mul' and enabled:
        # Only perform multiplication if currently enabled
        result = instruction['num1'] * instruction['num2']
        total += result
        
print(total)