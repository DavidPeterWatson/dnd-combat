from dnd_combat.creature import Creature, Skill, Skills

def standard_goblin():
    return Creature('Goblin', {Skills.Dex : Skill(Skills.Dex, 12)})
    