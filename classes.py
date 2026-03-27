from abc import ABC, abstractmethod

class Weapons(ABC):
    def __main__(self,name):
        self.name = name

    @abstractmethod
    def attack():
        pass
