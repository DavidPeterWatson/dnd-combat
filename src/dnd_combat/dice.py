from functools import reduce
import random
from enum import Enum
from typing import List, Dict

from numpy import add

class Die(Enum):
    d4 = 4
    d6 = 6
    d8 = 8
    d10 = 10
    d12 = 12
    d20 = 20
    d100 = 100

class SetOfDice:
    
    def __init__(self, number: int, die: Die):

        self.number = number
        self.die = die


class SelectionOfDice:
    
    def __init__(self, sets_of_dice: List[SetOfDice], modifier_func):
        self.sets_of_dice = sets_of_dice
        self.modifier_func = modifier_func


def roll_die(die: Die) -> int:
    return random.randint(1, die.value)


def roll_set_of_dice(set_of_dice: SetOfDice) -> int:
    return reduce(add, map(roll_die, [set_of_dice.die] * set_of_dice.number)) 


def roll_selection_of_dice(selection_of_dice: SelectionOfDice) -> int:
    return reduce(add, map(roll_set_of_dice, selection_of_dice.sets_of_dice)) + selection_of_dice.modifier_func()
