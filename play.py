'''Provides function to play two Prisoner's Dilemma strategies against each other.
'''


def __get_payoff(my_move, their_move):
    '''Return payoff for `my_move` if player two plays `their_move`.'''
    PAYOFFS = {
        'COOPERATE': {
            'DEFECT': 0,
            'COOPERATE': 3
        },
        'DEFECT': {
            'DEFECT': 1,
            'COOPERATE': 5
        }
    }
    return PAYOFFS[my_move][their_move]


def __play_one_round(strategy_1, strategy_2):
    '''Returns payoff for each strategy and adds to self.history.'''
    player_ones_move = strategy_1.play()
    player_twos_move = strategy_2.play()
    strategy_1.my_history.append(player_ones_move)
    strategy_1.their_history.append(player_twos_move)
    strategy_2.my_history.append(player_twos_move)
    strategy_2.their_history.append(player_ones_move)
    return (
        __get_payoff(player_ones_move, player_twos_move),
        __get_payoff(player_twos_move, player_ones_move)
    )


def play_game(strategy_1, strategy_2, rounds=200):
    '''Plays n rounds of Prisoner's Dilemma and returns scores for each strategy.
    '''
    player_one_score = 0
    player_two_score = 0
    for _ in range(rounds):
        scores = __play_one_round(strategy_1, strategy_2)
        player_one_score += scores[0]
        player_two_score += scores[1]
    return (player_one_score, player_two_score)
