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

| Strategy        | Score |
| --------------- | ----- |
| TitForTat       |  4852 |
| SneakyTitForTat |  4850 |
| HelpTheHelpers  |  4794 |
| Unforgiving     |  4635 |
| TitForTwoTats   |  4562 |
| AlwaysCooperate |  4302 |
| Random          |  3544 |
| AlwaysDefect    |  3044 |
