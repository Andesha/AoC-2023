import sys

with open(sys.argv[1]) as f:
    tally = 0
    for line in f.read().splitlines():
        buffer = [item for item in line if item.isdigit()]
        tally += (10*int(buffer[0]) + int(buffer[-1]))

print('sum: ', tally)