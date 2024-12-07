import re

with open('input.txt', 'r') as file:
    lines = file.read()

# Match blocks after a valid "do()" or at the start of the string
block_pattern = r"(?:^|do\(\))(.*?)(?=don't\(\)|$)"

# Match valid "mul(x, y)" within a block
mul_pattern = r"mul\((-?\d{1,3}),(-?\d{1,3})\)"

# Find all valid blocks
blocks = re.findall(block_pattern, lines)

# Extract valid mul(x, y) pairs from each block
nums = []
for block in blocks:
    nums.extend(re.findall(mul_pattern, block))



result = sum([int(pair[0]) * int(pair[1]) for pair in nums])
print(result)

