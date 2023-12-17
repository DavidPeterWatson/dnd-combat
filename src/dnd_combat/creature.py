from dnd_combat.dice import *
from math import floor
from typing import Dict, List
import uuid

class Skills(Enum):
    Str = 'Strength'
    Dex = 'Dexterity'
    Con = 'Constitution'
    Int = 'Intellegence'
    Wis = 'Wisdom'
    Cha = 'Charisma'


class Skill:
    
    def __init__(self, name, score, bonus = 0):
        self.name = name
        self.score = score
        self.bonus = bonus
        self.modifier_func = self.calculate_modifier

    def calculate_modifier(self):
        return floor((self.score + self.bonus - 10) / 2)

class Creature:

    def __init__(self, name, skills: Dict[str, Skill]):
        self.id = str(uuid.uuid4())
        self.name = name
        self.skills = skills
        self.initiative_roll = SelectionOfDice([SetOfDice(1, Die.d20)], self.skills[Skills.Dex].modifier_func)

