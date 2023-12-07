import sys

with open(sys.argv[1]) as f:
    mappers = f.read().split('\n\n')
seeds = mappers.pop(0)

def lookup(val, mappers):
    for map_types in mappers:
        _, *ranges = map_types.split('\n')
        for r in ranges:
            dst, src, n = map(int, r.split())
            if src <= val < src+n:
                val = val-src+dst
                break
    return val

seed_buffer = []
for seed in seeds.split()[1:]:
    seed_buffer.append(lookup(int(seed), mappers))
print('P1: ', min(seed_buffer))