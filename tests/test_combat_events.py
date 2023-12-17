from dnd_combat.goblin import standard_goblin


def test_creature_addex_to_battle_map():
    goblin = standard_goblin()
    battle_map = BattlemMap()
    # Subscribe to battlemap events
    events = battle_map.events
    battle_map.add(goblin)
    # Wait for event 
    
    # Assert that creature was added 
