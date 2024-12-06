import re

with open('input.txt') as f:
    data = f.read()

# Find all matches of the pattern mul(X,Y) where X and Y are 1-3 digits
pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
matches = re.finditer(pattern, data)

total = 0
for match in matches:
    num1 = int(match.group(1))
    num2 = int(match.group(2))
    total += num1 * num2

print(total)