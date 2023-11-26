from __future__ import annotations
from dice import Dice
from ursina import *


"""
Valeur par default :

Character :
- attack : 4
- defense : 0
- max_hp : 10
- attack_range : 0

Enemis :
Default
- attack_range : 1

Player:
- attack : 8
- defense : 3
- max_hp : 20
"""


class Character(Entity):
    def __init__(self, name:str = "Anonymous", attack:int = 8, defense:int = 3, max_hp:int = 20, attack_range=0, dice:Dice=Dice(6), **kwargs) -> None:
        super().__init__(**kwargs)

        self._name = name
        self._attack_value = attack
        self._defense_value = defense
        self._max_hp = max_hp
        self._current_hp = 5
        self._dice = dice
        self.y_speed = 0
        self.gravity = 5
        self._attack_range = attack_range
        self.gravity_impact = False

    def update(self):
        self.ray_detection()
        self.fall()

        if not self.intersects().hit:
            self.gravity_impact = True
        else:
            self.gravity_impact = False
    
    def points_on_circle(self, num_points, center=(0, 0)):
        radius = 360*num_points
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        return points


    def ray_detection(self):
        pass

    def __str__(self)->str:
        return f"{self._name} the Character enter the arena with attack : {self._attack_value} and defense : {self._defense_value}"
    
    @property
    def name(self):
        return self._name
    
    @property
    def defense_value(self):
        return self._defense_value
    
    @property
    def attack_range(self):
        return self._attack_range
    
    def is_alive(self)->bool:
        return self._current_hp > 0
    
    def decrease_health(self, amount):
        if amount < 0: return
        if self._current_hp - amount < 0:
            amount = self._current_hp
        self._current_hp -= amount

    def compute_damages(self, roll, target:Character):
        return self._attack_value + roll
    
    def compute_defense(self, damages, roll, attacker:Character):
        return damages - self._defense_value - roll

    def attack(self, target:Character)->None:
        if not self.is_alive(): return

        roll = self._dice.roll()
        damages = self.compute_damages(roll, target)
        target.defense(damages, self)

    def defense(self, damages:int, attacker:Character):
        roll = self._dice.roll()
        wounds = self.compute_defense(damages, roll, attacker)
        self.decrease_health(wounds)

    def fall(self):
        if self.gravity_impact:
            self.y_speed -= self.gravity * time.dt
            self.y += self.y_speed * time.dt