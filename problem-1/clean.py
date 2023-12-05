import sys

map_digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
              'four': 'f4r', 'five': 'f5e', 'six': 's6x',
              'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

def calibrate(all_lines):
    buffer = []
    for line in all_lines:
        for k,v in map_digits.items():
            line = line.replace(k,v)
        buffer.append(line)
    return buffer

def fold(all_lines):
    tally = 0
    for line in all_lines:
        buffer = [item for item in line if item.isdigit()]
        tally += (10*int(buffer[0]) + int(buffer[-1]))
    return tally

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
print('P1: ', fold(content))
print('P2: ', fold(calibrate(content)))