import sys

with open(sys.argv[1]) as f:
    content = f.read().splitlines()
times = map(int, content[0].split()[1:])
distances = map(int, content[1].split()[1:])

accum = 1
for time, dist in zip(times, distances):
    accum *= len([1 for v in range(1, time) if v * (time - v) > dist])
print('P1 or P2 depending on input: ', accum)