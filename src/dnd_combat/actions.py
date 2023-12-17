from dnd_combat.creature import Creature
from dnd_combat.dice import *
from typing import List

def roll_for_initiative(combatant: Creature):
    return roll_selection_of_dice(combatant.initiative_roll)

def determine_combat_order(combatants: List[Creature]):
    return sorted(combatants, key=lambda x: -roll_for_initiative(x))