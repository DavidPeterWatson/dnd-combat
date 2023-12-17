from dnd_combat.creature import *
from dnd_combat.dice import SelectionOfDice
from dnd_combat.goblin import standard_goblin

def test_creature_has_name():
    goblin = standard_goblin()
    assert type(goblin.name) is str

def test_creature_has_dex():
    goblin = standard_goblin()
    assert goblin.skills[Skills.Dex].score == 12
    assert goblin.skills[Skills.Dex].modifier_func() == 1

def test_creature_has_dex_modifier_2():
    goblin = standard_goblin()
    goblin.skills[Skills.Dex].bonus = 2
    assert goblin.skills[Skills.Dex].score == 12
    assert goblin.skills[Skills.Dex].modifier_func() == 2

def test_creature_has_id():
    # given
    goblin = standard_goblin()
    # then
    assert type(goblin.id) is str

def test_creature_has_initiative():
    goblin = standard_goblin()
    
    assert type(goblin.initiative_roll) is SelectionOfDice
