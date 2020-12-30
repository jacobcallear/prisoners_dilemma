'''Drop lowest scoring strategy in successive tournaments to find the winner.
'''
import logging
from collections import defaultdict
from itertools import combinations
from random import choice

from prisoners_dilemma import strategies
from prisoners_dilemma.play import play_game

logging.basicConfig(level=logging.WARNING)

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
    strategies.AdaptiveTitForTat,
    strategies.UnforgivingTitForTat,
    # These four strategies are always the worst, well below the others
    strategies.AlwaysCooperate,
    strategies.AlwaysDefect,
    strategies.Random,
    strategies.TatForTit
]

counter = 1
while len(STRATEGIES_LIST) > 1:
    TOTAL_SCORES = defaultdict(int)

    # Play all combinations of strategies
    for strategy_1, strategy_2 in combinations(STRATEGIES_LIST, 2):
        play_game(strategy_1, strategy_2, counter=TOTAL_SCORES)

    # Play each strategy against itself
    for strategy in STRATEGIES_LIST:
        play_game(strategy, strategy, counter=TOTAL_SCORES)

    # ==============================
    # Remove lowest score
    loser = min(
        TOTAL_SCORES.items(),
        key=lambda x: TOTAL_SCORES[x[0]]
    )
    # If multiple strategies had the same lowest score, drop one at random
    losers = []
    for name, score in TOTAL_SCORES.items():
        if score == loser[1]:
            losers.append((name, score))
    if len(losers) > 1:
        loser = choice(losers)
    # If all competitors have equal score, print all
    if len(losers) == len(STRATEGIES_LIST):
        break
    loser_name = eval(f'strategies.{loser[0]}')

    STRATEGIES_LIST.pop(STRATEGIES_LIST.index(loser_name))

    print(f'Round {counter} loser: {loser_name().__class__.__name__}')
    counter += 1

print(f'Round {counter} winner(s): ', [
        class_name().__class__.__name__
        for class_name in STRATEGIES_LIST
    ])
