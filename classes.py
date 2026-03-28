from abc import ABC, abstractmethod

class Weapons(ABC):
    def __init__(self,name):
        self.name = name
    
    # All sub classes need this method attack
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapons):
    def attack(self):
        print(f"The player swings their sword named {self.name}!")


class Bow(Weapons):
    def attack(self):
        print(f"The player fires their bow named {self.name}!")


class Staff(Weapons):
    def attack(self):
        print(f"The player casts a fireball with their staff named {self.name}!")

