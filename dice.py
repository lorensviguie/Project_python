from random import randint

class Dice:

    def __init__(self, faces:int = 6)->None:
        self._faces = faces

    def __str__(self)->str:
        return f"I'm a {self._faces} faces dice"

    def roll(self)->int:
        return randint(1,self._faces)

class RiggedDice(Dice):
    
    def roll(self, rigged: bool = False)->int:
        return self._faces if rigged else super().roll()
