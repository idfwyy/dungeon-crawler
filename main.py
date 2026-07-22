class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health = self.health - amount
        return self.health
    
    def attack(self,target):
        target.take_damage(self.attack_power)

class Enemy:
    def __init__(self,name,health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def take_damage(self,amount):
        self.health = self.health - amount
        return self.health
    
    def attack(self,target):
        target.take_damage(self.attack_power)
    
    

hero = Player("AARON", 100, 32)
hero.take_damage(40)
print(hero.health)

goblin = Enemy("Goblin", 100,65)
goblin.take_damage(20)
print(goblin.health)

hero.attack(goblin)
print(goblin.health)