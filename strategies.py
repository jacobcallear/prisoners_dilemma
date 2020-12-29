'''Defines strategies for Prisoner's Dilemma.
'''


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
