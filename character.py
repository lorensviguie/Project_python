from __future__ import annotations
from dice import Dice
from ursina import *



class Character(Entity):

    CAN_MOVE = False

    def __init__(self,
                 name:str = "Anonymous",
                 attack:int = 8,
                 defense:int = 3,
                 max_hp:int = 20,
                 attack_range:int=0,
                 attack_duration:float=0,
                 dice:Dice=Dice(6),
                 height:float=1,
                 width:float=1,
                 weight:int=5,
                 speed:int=5,
                 **kwargs) -> None:
        
        super().__init__(**kwargs)

        self._name = name

        self._max_health = max_hp
        self._current_health = max_hp
        self._weight = weight
        self._speed = speed
        self._attack_power = attack
        self._attack_duration = attack_duration
        self._defense_power = defense
        self._attack_range = attack_range
        self._sensor_range = 2
        self._height = height
        self._width = width

        self._is_jumping = False
        self._gravity = True

        self._textures = ()

        self.look_direction = 0    # 0 -> left   1 -> right
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
            if entity.y < self.y:
                return True
        return False
    
    def touch_roof(self)->bool:
        for entity in self.intersects().entities:
            if entity.y >= self.current_zone[1] and entity.x == self.current_zone[0]:
                return True
        return False
    
    def touch_left_side(self)->bool:
        for entity in self.intersects().entities:
            if entity.x <= self.x and entity.y == self.current_zone[1]:
                return True
        return False
    
    def touch_right_side(self)->bool:
        for entity in self.intersects().entities:
            if entity.x >= self.x and entity.y == self.current_zone[1]:
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
        if self.touch_left_side(): return

        self.x -= self._speed * time.dt
        return
    
    def move_right(self)->None:
        if self.touch_right_side(): return

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

    def heal(self, heal_value)->None:
        self._current_health = min(self._current_health+heal_value, self._max_health)
    
    
    # Méthodes d'information

    @property
    def name(self)->str:
        return self._name
    
    @property
    def attack_range(self)->int:
        return self._attack_range
    
    @property
    def max_health(self)->int:
        return self._max_health
    
    @property
    def current_zone(self)->(int,int):
        return (round(self.x*2)/2,round(self.y*2)/2)
    
    def damage(self, roll, target:Character):
        return self._attack_power + roll
    
    def defense(self, damages, roll, attacker:Character):
        return damages - self._defense_power - roll

    # Autres méthodes
    
    def points_on_circle(self, num_points, center=(0, 0)):
        radius = 180
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = center[0] + radius * math.cos(angle)
            y = center[1] + radius * math.sin(angle)
            points.append((x, y))
        return points
    
    def demi_cercle_coords(self, num_points=10, centre=(0, 0), angle_start=-45, angle_end=45):
        radius = 180
        if angle_start >= angle_end:

            angle_start, angle_end = angle_end, angle_start
            
        points = []
        for i in range(num_points):
            angle = math.radians(angle_start + (angle_end - angle_start) * i / (num_points - 1))
            x = centre[0] + radius * math.cos(angle)
            y = centre[1] + radius * math.sin(angle)
            points.append((x, y))
        return points
