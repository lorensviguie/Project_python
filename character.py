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
    def __init__(self, name:str = "Anonymous", attack:int = 8, defense:int = 3, max_hp:int = 20, attack_range=0, dice:Dice=Dice(6),height=1, width=1, weight=5, speed=5 ,**kwargs) -> None:
        super().__init__(**kwargs)

        self._name = name

        self._max_health = max_hp
        self._current_health = max_hp
        self._weight = weight
        self._speed = speed
        self._attack_power = attack
        self._defense_power = defense
        self._attack_range = attack_range
        self._sensor_range = 2
        self._height = height
        self._width = width

        self._is_jumping = False
        self._gravity = True
        self._is_attacking = False

        self.look_direction = 1    # 1 -> left   -1 -> right
        self._dice = dice

        self.jump_speed = 2
        self.y_speed = 0

    def update(self):
        if not self.touch_floor() and self.enabled:
            self.fall()
        
        self.ray_detection()
    


    # Méthodes de status

    def touch_floor(self)->bool:
        for entity in self.intersects().entities:
            if entity.y <= self.y:
                return True
        return False
    
    def touch_roof(self)->bool:
        for entity in self.intersects().entities:
            if entity.y >= self.y:
                return True
        return False
    
    def touch_left_side(self)->bool:   # //! Ne marche pas
        for entity in self.intersects().entities:
            if entity.x <= self.x:   # //TODOO Check la position y de l'objet pour voir si c'est pas l'obstacle du dessous (actuellement bloque le perso quand il est au sol)
                return True
        return False
    
    def touch_right_side(self)->bool:  # //! Ne marche pas
        for entity in self.intersects().entities:
            if entity.x >= self.x:   # //TODOO Check la position y de l'objet pour voir si c'est pas l'obstacle du dessous (actuellement bloque le perso quand il est au sol)
                return True
        return False
    
    def is_alive(self)->bool:
        return self._current_health > 0
    
    # Méthodes d'actions

    def jump(self)->None:
        if self.touch_roof(): return

        self.y_speed = self.jump_speed
        self.y += self.jump_speed * time.dt
        return
    
    def move_left(self)->None:
        #? Patch to used : if self.touch_left_side(): return

        self.x -= self._speed * time.dt
        return
    
    def move_right(self)->None:
        #? Patch to used : if self.touch_right_side(): return

        self.x += self._speed * time.dt
        return
    
    def ray_detection(self):
        pass

    def fall(self):
        if self._gravity:
            self.y_speed -= self._weight * time.dt
            self.y += self.y_speed * time.dt

    def take_damage(self, amount):
        if amount < 0: return
        if self._current_health - amount < 0:
            amount = self._current_health
        self._current_health -= amount
    
    def defense_self(self, damages:int, attacker:Character):
        roll = self._dice.roll()
        wounds = self.defense(damages, roll, attacker)
        self.take_damage(wounds)
    
    def attack_target(self, target:Character)->None:
        if not self.is_alive(): return

        roll = self._dice.roll()
        damages = self.damage(roll, target)
        target.defense_self(damages, self)
    

    
    # Méthodes d'information

    @property
    def name(self)->str:
        return self._name
    
    @property
    def attack_range(self)->int:
        return self._attack_range
    
    @property
    def current_zone(self)->(int,int):
        return (round(self.x*2)/2,round(self.y*2)/2)
    
    def damage(self, roll, target:Character):
        return self._attack_power + roll
    
    def defense(self, damages, roll, attacker:Character):
        return damages - self._defense_power - roll

    # Autres méthodes
    
    def points_on_circle(self, num_points, center=(0, 0)):
        radius = 360*num_points
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        return points
    
    def demi_cercle_coords(self, angle_start=-110, angle_end=80, centre=(0,0)):
        pas_angle=20
        coords = []
        for angle in range(angle_start, angle_end + 1, pas_angle):
            angle_rad = math.radians(angle)
            x = centre[0] + self._sensor_range * math.cos(angle_rad)
            y = centre[1] + self._sensor_range * math.sin(angle_rad)
            coords.append((x, y))
        return coords

