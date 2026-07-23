class Character:
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health = self.health - amount
        return self.health
    
    def attack(self,target):
        target.take_damage(self.attack_power)


class Player(Character):
    pass

class Enemy(Character):
    pass

class Goblin(Enemy):
    def __init__(self, name):
        super().__init__(name,100,5)


goblin = Goblin("Grunk")
print(goblin.name)
print(goblin.health)
print(goblin.attack_power)

hero = Player("AARON", 100, 32)
hero.take_damage(40)
print(hero.health)

goblin.take_damage(20)
print(goblin.health)

