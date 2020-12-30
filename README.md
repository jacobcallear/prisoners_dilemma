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
| -------------------- | ----: |
| UnforgivingTitForTat | 12761 |
| TwoHitsForOne        | 12435 |
| Unforgiving          | 12393 |
| TitForTat            | 12067 |
| TitForTatPatterns    | 12041 |
| Modeler              | 11982 |
| GoByMajority         | 11915 |
| ForgivingTitForTat   | 11873 |
| HelpTheHelpers       | 11767 |
| Equality             | 11471 |
| SneakyTitForTat      | 11236 |
| TitForTwoTats        | 11210 |
| AlwaysCooperate      | 10560 |
| TitForTatWithPokes   | 10450 |
| AlternateCooperate   |  9990 |
| AlternateDefect      |  9691 |
| MostlyTitForTat      |  9574 |
| ThreeInARow          |  9514 |
| Random               |  9321 |
| AlwaysDefect         |  8708 |
| TatForTit            |  8670 |

## Winning strategies

The tournament can be rerun repeatedly, dropping the lowest scoring strategy,
until all strategies have the same high score. This always results in the same
10 winners which cooperate in every round of every game. `TitForTat` achieves
this with the fewest lines of code in `tournament_sudden_death.py`.
