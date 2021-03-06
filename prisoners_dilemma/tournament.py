'''Plays each Prisoner's Dilemma strategy against all the others to find the winner.
'''
import logging

from collections import defaultdict
from itertools import combinations

from prisoners_dilemma import strategies
from prisoners_dilemma.play import play_game
from prisoners_dilemma.print_table import convert_to_table, sort_by_value

logging.basicConfig(level=logging.INFO, format='%(message)s')

TOTAL_SCORES = defaultdict(int)

STRATEGIES_LIST = [
    strategies.SneakyTitForTat,
    strategies.TitForTat,
    strategies.TitForTwoTats,
    strategies.TitForTatPatterns,
    strategies.HelpTheHelpers,
    strategies.Unforgiving,
    strategies.Equality,
    strategies.ForgivingTitForTat,
    strategies.GoByMajority,
    strategies.TwoHitsForOne,
    strategies.MostlyTitForTat,
    strategies.AlternateCooperate,
    strategies.AlternateDefect,
    strategies.TitForTatWithPokes,
    strategies.ThreeInARow,
    strategies.Modeler,
    strategies.UnforgivingTitForTat,
    # These four strategies are always the worst, well below the others
    strategies.AlwaysCooperate,
    strategies.AlwaysDefect,
    strategies.Random,
    strategies.TatForTit
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
