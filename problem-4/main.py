import sys
from collections import defaultdict

with open(sys.argv[1]) as f:
    content = [x.split(':')[1] for x in f.read().splitlines()]

def score_card(card_string):
    card_info = card_string.split('|')
    matches = len(set(card_info[0].split()) & set(card_info[1].split()))
    return matches, (2 ** (matches - 1)) if matches else 0

print('P1: ', sum(score_card(card_string)[1] for card_string in content))
card_counts = {k:1 for k in range(1,len(content)+1)}
for id in range(1, len(content) + 1):
    win_count, _ = score_card(content[id-1])
    for card_bump_ids in range(id + 1, id + 1 + win_count):
        card_counts[card_bump_ids] += card_counts[id]
print('P2: ', sum(card_counts.values()))
