# Prisoner's Dilemma

See wikipedia for a description of the
[prisoner's dilemma](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)

## Tournament

`tournament.py` runs an iterated prisoner's dilemma tournament to find the most
effective strategy. Each strategy plays every other strategy and themselves for
200 rounds each. In each round, each strategy chooses to *defect* or *cooperate*
with the following payoffs: 

| Player 1  | Player 2  | Payoff to player 1 |
| --------- | --------- | ------------------ |
| Cooperate | Defect    | 0                  |
| Defect    | Defect    | 1                  |
| Cooperate | Cooperate | 3                  |
| Defect    | Cooperate | 5                  |

## Results

With all strategies in the tournament:

| Strategy             | Score |
| -------------------- | ----- |
| HelpTheHelpers       |  8078 |
| Unforgiving          |  7972 |
| TitForTat            |  7725 |
| TitForTatPatterns    |  7710 |
| GoByMajority         |  7594 |
| ForgivingTitForTat   |  7568 |
| SneakyTitForTat      |  7407 |
| TitForTwoTats        |  7339 |
| Equality             |  7237 |
| AlwaysCooperate      |  6732 |
| Random               |  6072 |
| TatForTit            |  5731 |
| AlwaysDefect         |  5444 |

With the worst four strategies removed, the results are very different:

| Strategy             | Score |
| -------------------- | ----- |
| TitForTat            |  5999 |
| TitForTatPatterns    |  5999 |
| ForgivingTitForTat   |  5999 |
| GoByMajority         |  5900 |
| Equality             |  5801 |
| TitForTwoTats        |  5799 |
| HelpTheHelpers       |  5799 |
| Unforgiving          |  5607 |
| SneakyTitForTat      |  5564 |
