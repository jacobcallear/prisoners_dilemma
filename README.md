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
| HelpTheHelpers       |  7595 |
| Unforgiving          |  7420 |
| TitForTatPatterns    |  7140 |
| TitForTat            |  7116 |
| ForgivingTitForTat   |  7013 |
| SneakyTitForTat      |  6911 |
| TitForTwoTats        |  6756 |
| Equality             |  6625 |
| AlwaysCooperate      |  6105 |
| TatForTit            |  5312 |
| Random               |  5304 |
| AlwaysDefect         |  5228 |

With the worst four strategies removed, the results are very different:

| Strategy             | Score |
| -------------------- | ----- |
| TitForTat            |  5399 |
| TitForTatPatterns    |  5399 |
| ForgivingTitForTat   |  5399 |
| Equality             |  5201 |
| TitForTwoTats        |  5199 |
| HelpTheHelpers       |  5199 |
| SneakyTitForTat      |  5064 |
| Unforgiving          |  5007 |
