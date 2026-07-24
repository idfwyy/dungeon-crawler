class Character:
    def __init__(self,name,health,attack_power,weapon = None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon

    def take_damage(self, amount):
        self.health = self.health - amount
        return self.health
    
    def attack(self,target):
        if self.weapon is None:
            target.take_damage(self.attack_power)
        else:
            return target.take_damage(self.attack_power + self.weapon.power)

class Weapon:
    def __init__(self,name,power):
        self.name = name
        self.power = power


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


goblin.take_damage(20)
print(goblin.health)

sword = Weapon("Iron rail",22)
hero = Player("james",100,40,sword)
print(hero.weapon.name)
hero.attack(goblin)
hero.attack(dragon)
print(dragon.health)
