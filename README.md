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
| HelpTheHelpers       |  6391 |
| Unforgiving          |  6120 |
| TitForTatPatterns    |  5926 |
| TitForTat            |  5913 |
| SneakyTitForTat      |  5896 |
| TitForTwoTats        |  5534 |
| AlwaysCooperate      |  4911 |
| Random               |  4424 |
| AlwaysDefect         |  4232 |
| TatForTit            |  4204 |
