class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        self.health = self.health - amount
        return self.health 
    
hero = Player("AARON", 100)
hero.take_damage(40)
print(hero.health)