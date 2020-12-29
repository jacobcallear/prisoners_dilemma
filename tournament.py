'''Plays each Prisoner's Dilemma strategy against all the others to find the winner.
'''

from collections import defaultdict
from itertools import combinations

import strategies
from play import play_game

TOTAL_SCORES = defaultdict(int)

STRATEGIES_LIST = [
    strategies.AlwaysCooperate,
    strategies.AlwaysDefect,
    strategies.SneakyTitForTat,
    strategies.TitForTat,
    strategies.TitForTwoTats,
    strategies.Random
]


def play_game_and_add_to_total(strategy_1, strategy_2):
    '''Play strategy 1 against strategy 2. Print scores and add to total.'''
    scores = play_game(strategy_1(), strategy_2())
    print(f'{str(strategy_1())}: {scores[0]}, '
          f'{str(strategy_2())}: {scores[1]}')
    for strategy, score in zip((strategy_1(), strategy_2()), scores):
        TOTAL_SCORES[str(strategy)] += score

# ==============================
# PLAY

# Play all combinations of strategies
for strategy_1, strategy_2 in combinations(STRATEGIES_LIST, 2):
    play_game_and_add_to_total(strategy_1, strategy_2)

# Play each strategy against itself
for strategy in STRATEGIES_LIST:
    play_game_and_add_to_total(strategy, strategy)

# ==============================
# PRINT

# Sort strategies by ascending score
sorted_scores = sorted(
    TOTAL_SCORES.items(),
    key=lambda x: TOTAL_SCORES[x[0]],
    reverse=True
)

# Print table header
left_align = 15
right_align = 5
width = left_align + right_align + 3

print(f'''
{'TOTAL SCORES':^{left_align + right_align}}
{'-' * width}

{'Strategy':<{left_align}} | {'Score':>{right_align}}
{'-' * width}'''
)

# Print scores
for strategy, score in sorted_scores:
    print(f'{strategy:<15} | {score:>5}')
