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

| Strategy             | Score |
| -------------------- | ----- |
| TwoHitsForOne        | 10657 |
| Unforgiving          | 10655 |
| TitForTatPatterns    | 10518 |
| GoByMajority         | 10459 |
| TitForTat            | 10404 |
| HelpTheHelpers       | 10277 |
| ForgivingTitForTat   | 10268 |
| Equality             |  9757 |
| SneakyTitForTat      |  9743 |
| TitForTwoTats        |  9723 |
| TitForTatWithPokes   |  9344 |
| AlternateCooperate   |  8953 |
| AlwaysCooperate      |  8910 |
| MostlyTitForTat      |  8807 |
| Random               |  8584 |
| AlternateDefect      |  8550 |
| ThreeInARow          |  7726 |
| AlwaysDefect         |  7724 |
| TatForTit            |  7502 |

## Winning strategies

The tournament can be rerun repeatedly, dropping the lowest scoring strategy,
until all strategies have the same high score. This always results in the same
10 winners which cooperate in every round of every game. `TitForTat` achieves
this with the fewest lines of code in `tournament_sudden_death.py`.
