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
| UnforgivingTitForTat | 12804 |
| TwoHitsForOne        | 12513 |
| Unforgiving          | 12435 |
| GoByMajority         | 12065 |
| TitForTatPatterns    | 12050 |
| TitForTat            | 12034 |
| HelpTheHelpers       | 12025 |
| AdaptiveTitForTat    | 12023 |
| ForgivingTitForTat   | 11845 |
| Equality             | 11475 |
| SneakyTitForTat      | 11317 |
| TitForTwoTats        | 11240 |
| AlwaysCooperate      | 10578 |
| TitForTatWithPokes   | 10459 |
| AlternateCooperate   | 10095 |
| MostlyTitForTat      | 10042 |
| AlternateDefect      |  9710 |
| ThreeInARow          |  9519 |
| Random               |  8952 |
| AlwaysDefect         |  8680 |
| TatForTit            |  8582 |

## Winning strategies

The tournament can be rerun repeatedly, dropping the lowest scoring strategy,
until all strategies have the same high score. This always results in the same
10 winners which cooperate in every round of every game. `TitForTat` achieves
this with the fewest lines of code in `tournament_sudden_death.py`.
