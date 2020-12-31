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
| UnforgivingTitForTat | 12733 |
| Unforgiving          | 12375 |
| HelpTheHelpers       | 12321 |
| TitForTat            | 12027 |
| Modeler              | 11946 |
| TitForTatPatterns    | 11945 |
| GoByMajority         | 11855 |
| ForgivingTitForTat   | 11820 |
| TwoHitsForOne        | 11720 |
| Equality             | 11379 |
| SneakyTitForTat      | 11326 |
| TitForTwoTats        | 11207 |
| AlwaysCooperate      | 10602 |
| TitForTatWithPokes   |  9940 |
| ThreeInARow          |  9912 |
| AlternateDefect      |  9522 |
| MostlyTitForTat      |  9428 |
| Random               |  9378 |
| AlternateCooperate   |  9343 |
| TatForTit            |  9022 |
| AlwaysDefect         |  8608 |

## Winning strategies

The tournament can be rerun repeatedly, dropping the lowest scoring strategy,
until all strategies have the same high score. This always results in the same
10 winners which cooperate in every round of every game. `TitForTat` achieves
this with the fewest lines of code in `tournament_sudden_death.py`.
