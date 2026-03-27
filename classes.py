from abc import ABC, abstractmethod

class Weapons(ABC):
    def __main__(self,name):
        self.name = name
    
    # All sub classes need this method attack
    @abstractmethod
    def attack():
        pass

class Sword(Weapons):
    def attack():
        print("The player swings their sword!")


class Bow(Weapons):
    def attack():
        print("The player fires their bow!")