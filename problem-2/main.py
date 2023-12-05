import sys
from collections import defaultdict
from functools import reduce

with open(sys.argv[1]) as f:
    games_table = []
    for line in [x.split(':')[1] for x in f.read().splitlines()]:
        game = defaultdict(int)
        for subsets in line.split(';'):
            for reveal in subsets.rsplit(','):
                count, color = reveal.strip().split()
                game[color] = max(game[color], int(count))
        games_table.append(game)

    tally, power_tally = 0, 0
    for id, game in enumerate(games_table):
        if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
            tally += (id + 1)
        power_tally += reduce(lambda x, y: x*y, game.values())

    print('P1: ', tally)
    print('P2: ', power_tally)