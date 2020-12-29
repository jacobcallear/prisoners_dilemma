'''Defines strategies for Prisoner's Dilemma.
'''

from random import choice


class Strategy:
    '''Parent class for each strategy. Keeps track of both player's history.

    Subclasses must add a `play` method that returns 'COOPERATE' or 'DEFECT'.
    '''

    def __init__(self):
        self.my_history = []
        self.their_history = []

    def __repr__(self):
        return f'{self.__class__.__name__}(my_history={self.my_history}, '\
               f'their_history={self.their_history})'

    def __str__(self):
        return self.__class__.__name__


class TitForTat(Strategy):
    '''Nice, forgiving, punishing.'''
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        return self.their_history[-1]


class AlwaysDefect(Strategy):
    '''Nasty.'''
    @staticmethod
    def play():
        return 'DEFECT'


class AlwaysCooperate(Strategy):
    '''Nice.'''
    @staticmethod
    def play():
        return 'COOPERATE'


class TitForTwoTats(Strategy):
    '''Nice, forgiving, less punishing than TitForTat.'''
    def play(self):
        if len(self.my_history) <= 2:
            return 'COOPERATE'
        if self.their_history[-2:] == ['DEFECT', 'DEFECT']:
            return 'DEFECT'
        return 'COOPERATE'


class SneakyTitForTat(Strategy):
    '''Strategy to exploit TitForTwoTats.

    - Defect first move
    - Play tit for tat if opponent defects
    - Otherwise defect every third move
    '''
    def __init__(self):
        super().__init__()
        self.playing_tit_for_tat = False

    def play(self):
        if self.my_history == []:
            return 'DEFECT'
        if self.playing_tit_for_tat:
            return self.their_history[-1]
        if self.their_history[-1] == 'DEFECT':
            self.playing_tit_for_tat = True
            return 'COOPERATE'
        if self.my_history[-2:] == ['COOPERATE', 'COOPERATE']:
            return 'DEFECT'
        return 'COOPERATE'


class Random(Strategy):
    '''Randomly cooperates / defects.'''
    @staticmethod
    def play():
        return choice(['COOPERATE', 'DEFECT'])


class Unforgiving(Strategy):
    '''Cooperates first move. Defects forever if opponent defects.'''
    def __init__(self):
        super().__init__()
        self.always_defect = False

    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'DEFECT':
            self.always_defect = True
        if self.always_defect:
            return 'DEFECT'
        return 'COOPERATE'


class HelpTheHelpers(Strategy):
    '''Cooperates with players that reciprocate cooperation.
    '''
    def __init__(self):
        super().__init__()
        self.count_helps = 0
        self.count_betrayals = 0

    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        # If my last move was cooperate, see if they reciprocated
        if self.my_history[-1] == 'COOPERATE':
            if self.their_history[-1] == 'COOPERATE':
                self.count_helps += 1
            else:
                self.count_betrayals += 1
        # Cooperate if the other player tends to reciprocate
        if self.count_betrayals == 0:
            return 'COOPERATE'
        if self.count_helps == 0:
            return 'DEFECT'
        if self.count_helps / self.count_betrayals > 0.6:
            return 'COOPERATE'
        return 'DEFECT'
