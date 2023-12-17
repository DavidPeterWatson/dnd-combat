class Motive:

    
    def __init__(self, name, score, bonus = 0):
        self.name = name
        self.score = score
        self.bonus = bonus
        self.modifier_func = self.calculate_modifier