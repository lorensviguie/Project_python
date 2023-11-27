# Frog  Dog  Humans
from __future__ import annotations
from ursina import *
from character import Character
import datetime

class Enemis(Character):

    IS_DEBUG_MODE=False

    def __init__(self, name="enemis",max_health=10, defense=0, height=1/2, width=1/2,attack=4, attack_range=1, attack_duration=1, position=(0,0,0), texture='Assets/frog_right.png', enabled=False):
        super().__init__(
            name=name,
            max_health=max_health,
            defense=defense,
            attack=attack,
            attack_range=attack_range,
            height=height,
            width=width,
            enabled=enabled,

            model='quad',
            scale=(width,height),
            position=position,
            texture=texture,
            collider="box"
        )
        self.health_bar = HealthBar(self)
        self._attack_duration = attack_duration
        self.last_attack:datetime=datetime.datetime.now()
    
    def update(self):
        super().update()
        if not self.is_alive():
            self.disable()
        can_attack, target = self.attack_ray()
        if can_attack:
            if (datetime.datetime.now()-self.last_attack).total_seconds() < self._attack_duration: return
            self.last_attack = datetime.datetime.now()
            self.attack_target(target)
        
    
    def attack_ray(self:Enemis)->(bool,Entity):
        for y in self.demi_cercle_coords(centre=(self.x, self.y)):
            hit_info = raycast(self.position, direction=(y[0]*self.look_direction, y[1], 0), distance=self._attack_range, ignore=[self], debug=type(self).IS_DEBUG_MODE)
            if not hit_info.hit: continue

            target:Entity = hit_info.entity
            if target.name != "player": continue

            return (True, target)
        return (False, None)

    def defense_self(self, damages:int, attacker:Character):
        super().defense_self(damages, attacker)
        self.health_bar.updateHealth()
    
    def sensore_ray(self:Enemis):
        for y in self.points_on_circle(50, (self.x, self.y)):
            hit_info = raycast(self.position, direction=(y[0], y[1], 0), distance=self._sensor_range, ignore=[self], debug=type(self).IS_DEBUG_MODE)
            if hit_info.hit:
                target:Entity = hit_info.entity
                if target.name == "player":
                    if target.x > self.x and self.look_direction == -1:
                        self.look_direction = 1
                        self.texture = 'Assets/frog_right.png'
                    elif target.x < self.x and self.look_direction == 1:
                        self.look_direction = -1
                        self.texture = 'Assets/frog_left.png'


    def ray_detection(self:Enemis):
        self.attack_ray()
        self.sensore_ray()

class HealthBar:
    def __init__(self, enemis: Enemis):
        self.enemis = enemis
        self.border = Entity(parent=enemis, model='quad', z=1, y=0.6, x=0.1, color=color.black, scale_x=enemis._max_health * 0.05, scale_y=0.1)
        self.health = Entity(parent=enemis, model='quad', z=1, y=0.6, x=0.1, color=color.red, scale_x=enemis._current_health * 0.05, scale_y=0.1)

    def updateHealth(self):
        self.health.scale_x = self.enemis._current_health / self.enemis._max_health * self.border.scale_x

