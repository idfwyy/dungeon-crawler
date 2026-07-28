class Character:
    def __init__(self,name,health,attack_power,weapon = None):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.weapon = weapon

    def take_damage(self, amount):
        self.health = self.health - amount
        self.health = max(0,self.health)
        return self.health
    
    def attack(self,target):
        if self.weapon is None:
            target.take_damage(self.attack_power)
        else:
            return target.take_damage(self.attack_power + self.weapon.power)
        
    def is_alive(self):
        if self.health > 0:
            return True
        return False


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
    


sword = Weapon("Iron rail",6)
hero = Player("SpiderMan",100,3,sword)
goblin = Goblin("DR.OCTOPUS")

while hero.is_alive() and goblin.is_alive():
    hero.attack(goblin)
    print(goblin.health)
    if goblin.is_alive():
        goblin.attack(hero)
        print(hero.health)
    
if hero.is_alive():
    print("Hero won!")
else:
    print("Goblin won!")


