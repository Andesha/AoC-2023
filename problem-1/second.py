import sys

map_digits = {'one': 'o1e', 'two': 't2o', 'three': 't3e',
              'four': 'f4r', 'five': 'f5e', 'six': 's6x',
              'seven': 's7n', 'eight': 'e8t', 'nine': 'n9e'}

with open(sys.argv[1]) as f:
    tally = 0
    for line in f.read().splitlines():
        for k,v in map_digits.items():
            line = line.replace(k,v)
        
        buffer = [item for item in line if item.isdigit()]
        tally += (10*int(buffer[0]) + int(buffer[-1]))

print(tally)