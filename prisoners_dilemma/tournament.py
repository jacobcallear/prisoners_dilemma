'''Plays each Prisoner's Dilemma strategy against all the others to find the winner.
'''

from collections import defaultdict
from itertools import combinations

import strategies
from play import play_game
from print_table import convert_to_table, sort_by_value

TOTAL_SCORES = defaultdict(int)

STRATEGIES_LIST = [
    strategies.AlwaysCooperate,
    strategies.AlwaysDefect,
    strategies.SneakyTitForTat,
    strategies.TitForTat,
    strategies.TitForTwoTats,
    strategies.Random,
    strategies.Unforgiving,
    strategies.HelpTheHelpers,
    strategies.TatForTit,
    strategies.TitForTatPatterns
]

# ==============================
# PLAY

# Play all combinations of strategies
for strategy_1, strategy_2 in combinations(STRATEGIES_LIST, 2):
    play_game(strategy_1, strategy_2, counter=TOTAL_SCORES)

# Play each strategy against itself
for strategy in STRATEGIES_LIST:
    play_game(strategy, strategy, counter=TOTAL_SCORES)

# ==============================
# PRINT

sorted_scores = sort_by_value(TOTAL_SCORES)
print(convert_to_table(sorted_scores, heading_1='Strategy', heading_2='Score'))
