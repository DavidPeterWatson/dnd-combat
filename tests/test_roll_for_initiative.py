from dnd_combat.actions import roll_for_initiative, determine_combat_order
from dnd_combat.creature import Skills
from dnd_combat.goblin import standard_goblin

def test_roll_for_initiative_is_int():
    # given
    goblin = standard_goblin()
    # when
    initiative = roll_for_initiative(goblin)
    # then
    assert type(initiative) is int

def test_roll_for_initiative_is_in_range():
    # given
    goblin = standard_goblin()
    # when
    initiative = roll_for_initiative(goblin)
    # then
    assert initiative >= 3
    assert initiative <= 30

def test_initiative_is_rolled_on_call_for_initiative():
    # given a goblin
    goblin = standard_goblin()
    combatants = [goblin]
    # when roll for initiative is called
    ordered_combatants = determine_combat_order(combatants)

    # then list of combatants must contain a goblin
    assert len(ordered_combatants) == 1
    assert goblin in ordered_combatants

def test_initiative_for_2_goblins_is_sorted():
    # given a goblin
    alert_goblin = standard_goblin()
    alert_goblin.skills[Skills.Dex].bonus = 10
    day_dreaming_goblin = standard_goblin()
    day_dreaming_goblin.skills[Skills.Dex].bonus = -10

    combatants = [day_dreaming_goblin, alert_goblin]
    # when roll for initiative is called
    ordered_combatants = determine_combat_order(combatants)

    # then list of combatants must contain a goblin
    assert len(ordered_combatants) == 2
    assert ordered_combatants[0] == alert_goblin
    assert ordered_combatants[1] == day_dreaming_goblin
