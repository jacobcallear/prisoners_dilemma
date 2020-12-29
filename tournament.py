from itertools import combinations

import strategies
from play import play_game

strategies_list = [
    strategies.AlwaysCooperate,
    strategies.AlwaysDefect,
    strategies.SneakyTitForTat,
    strategies.TitForTat,
    strategies.TitForTwoTats
]
for strategy_1, strategy_2 in combinations(strategies_list, 2):
    scores = play_game(strategy_1(), strategy_2())
    print(scores)