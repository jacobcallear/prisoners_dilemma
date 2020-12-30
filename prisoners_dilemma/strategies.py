'''Defines strategies for Prisoner's Dilemma.
'''

from random import choice, random


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

    def __increment_betrayals(self):
        '''Record if cooperations are reciprocated.'''
        if len(self.my_history) < 2:
            return
        if self.my_history[-2] == 'COOPERATE':
            if self.their_history[-1] == 'COOPERATE':
                self.count_helps += 1
            else:
                self.count_betrayals += 1

    def play(self):
        self.__increment_betrayals()
        if len(self.my_history) <= 2:
            return 'COOPERATE'
        # Cooperate if the other player tends to reciprocate
        if self.count_betrayals == 0:
            return 'COOPERATE'
        if self.count_helps / self.count_betrayals > 0.6:
            return 'COOPERATE'
        return 'DEFECT'


class TatForTit(Strategy):
    '''Cooperates with defectors, and defects with cooperators.
    '''
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'COOPERATE':
            return 'DEFECT'
        return 'COOPERATE'


class TitForTatPatterns(Strategy):
    '''TitForTat, but defects if it thinks opponent is defecting every n moves.
    '''

    def __defect_pattern(self):
        '''Returns *n* if opponent defects every *n* moves; otherwise 0.
        '''
        # Look backwards through opponents history in 5 steps of `num`
        # If these 5 steps contain 3 consecutive defects, return `num`
        consecutive = 0
        for num in range(3, 10):
            counter = 0
            for i in range(len(self.their_history) - 1, -1, -num):
                if counter > 5:
                    break
                if consecutive >= 3:
                    return num
                if self.their_history[i] == 'DEFECT':
                    consecutive += 1
                else:
                    consecutive = 0
                counter += 1
        return 0

    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        pattern = self.__defect_pattern()
        if pattern:
            if (len(self.my_history) + 1) % pattern == 0:
                return 'DEFECT'
        return self.their_history[-1]


class Equality(Strategy):
    '''Cooperates if both players had the same move; otherwise defects.'''
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.my_history[-1] == self.their_history[-1]:
            return 'COOPERATE'
        return 'DEFECT'


class ForgivingTitForTat(Strategy):
    '''Always cooperates when opponent cooperates. Sometimes forgives defection.
    '''
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'COOPERATE':
            return 'COOPERATE'
        if self.my_history[-1] == 'COOPERATE':
            if random() >= 0.124:
                return 'DEFECT'
            return 'COOPERATE'
        if self.my_history[-1] == 'DEFECT':
            if random() >= 0.25:
                return 'DEFECT'
            return 'COOPERATE'

class GoByMajority(Strategy):
    '''Cooperates if opponent mostly cooperates. Otherwise defects.
    '''
    def __init__(self):
        super().__init__()
        self.cooperate_count = 0
        self.defect_count = 0

    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'COOPERATE':
            self.cooperate_count += 1
        else:
            self.defect_count += 1
        if self.cooperate_count > self.defect_count:
            return 'COOPERATE'
        return 'DEFECT'


class TwoHitsForOne(Strategy):
    '''Cooperates if opponent cooperates. Defects twice if opponent defects.'''
    def __init__(self):
        super().__init__()
        self.one_more_defect = False

    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'DEFECT':
            self.one_more_defect = True
            return 'DEFECT'
        if self.one_more_defect:
            return 'DEFECT'
        return 'COOPERATE'


class MostlyTitForTat(Strategy):
    '''80% tit for tat; 20% tat for tit.'''
    def play(self):
        probability = 0.8
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'COOPERATE':
            if random() < probability:
                return 'COOPERATE'
            return 'DEFECT'
        if random() < probability:
            return 'DEFECT'
        return 'COOPERATE'


class AlternateDefect(Strategy):
    '''Alternate 'Defect'/'Cooperate'.'''
    def play(self):
        if self.my_history == []:
            return 'DEFECT'
        if self.my_history[-1] == 'DEFECT':
            return 'COOPERATE'
        return 'DEFECT'


class AlternateCooperate(Strategy):
    '''Alternate 'Cooperate'/'Defect'.'''
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.my_history[-1] == 'COOPERATE':
            return 'DEFECT'
        return 'COOPERATE'


class TitForTatWithPokes(Strategy):
    '''Tit for tat, but defects every 10 moves.'''
    def __init__(self):
        super().__init__()
        self.counter = 0
    def play(self):
        self.counter += 1
        if self.counter == 1:
            return 'COOPERATE'
        if self.counter == 10:
            self.counter = 0
            return 'DEFECT'
        return self.their_history[-1]


class ThreeInARow(Strategy):
    '''Three cooperates followed by a defection.'''
    def __init__(self):
        super().__init__()
        self.counter = 0
    def play(self):
        self.counter += 1
        if self.counter <= 3:
            return 'COOPERATE'
        self.counter = 0
        return 'DEFECT'


class AdaptiveTitForTat(Strategy):
    '''Tries to model likelihood of opponent cooperating.'''
    def __init__(self):
        super().__init__()
        self.should_cooperate = 0.5
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        # Calculate likelihood of opponent cooperating
        if self.their_history[-1] == 'COOPERATE':
            self.should_cooperate += 0.5 * (1 - self.should_cooperate)
        else:
            self.should_cooperate += 0.5 * (0 - self.should_cooperate)
        # Cooperate or defect
        if self.should_cooperate >= 0.5:
            return 'COOPERATE'
        return 'DEFECT'


class UnforgivingTitForTat(Strategy):
    '''Tit for Tat, but switches to all 'DEFECT' if opponent defects > 5 times.
    '''
    def __init__(self):
        super().__init__()
        self.total_betrayals = 0
    def play(self):
        if self.my_history == []:
            return 'COOPERATE'
        if self.their_history[-1] == 'DEFECT':
            self.total_betrayals += 1
        if self.total_betrayals > 5:
            return 'DEFECT'
        return self.their_history[-1]
