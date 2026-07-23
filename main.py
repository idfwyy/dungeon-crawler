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

class Dragon(Enemy):
    def __init__(self, name):
        super().__init__(name,100, 20)

    def take_damage(self, amount):
        return super().take_damage(amount/2)
    
goblin = Goblin("Grunk")
dragon = Dragon("Smaug")
print(goblin.name)
print(goblin.health)
print(goblin.attack_power)

hero = Player("AARON", 100, 32)
hero.take_damage(40)
print(hero.health)

hero.attack(goblin)
hero.attack(dragon)
print(goblin.health)
print(dragon.health)

goblin.take_damage(20)
print(goblin.health)

