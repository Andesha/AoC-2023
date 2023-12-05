import sys, re
from collections import defaultdict

with open(sys.argv[1]) as f:
    engine = [list(x) for x in f.read().splitlines()]

symbols = {}
for y, line in enumerate(engine):
    for x, symbol in enumerate(line):
        if symbol not in '.0123456789':
            symbols[(x,y)] = symbol

tally = 0
potential_gears = defaultdict(list)
for y, line in enumerate(engine):
    for found in re.finditer(r'\d+', ''.join(line)):
        for (symbol_x, symbol_y), symbol in symbols.items():
            if (symbol_y -1 <= y <= symbol_y + 1):
                if (found.start() -1 <= symbol_x <= found.end()):
                    value = int(found.group())
                    tally += value
                    if symbol == '*':
                        potential_gears[(symbol_x, symbol_y)].append(value)
                    break

print('P1: ', tally)

sum_ratio = 0
for gear_loc, nums in potential_gears.items():
    if len(nums) == 2:
        sum_ratio += (nums[0] * nums[1])
print('P2: ', sum_ratio)