# Frog  Dog  Humans
from __future__ import annotations
from ursina import *
from character import Character
import datetime

class Enemis(Character):
    def __init__(self, max_health=10, defense=0, attack=4, attack_range=1, attack_duration=1, position=(0,0,0), texture='Assets/pxArt.png'):
        super().__init__(
            max_health=max_health,
            defense=defense,
            attack=attack,
            attack_range=attack_range,

            model='cube',
            color=color.blue,
            scale=(1,1),
            position=position,
            texture=texture
        )
        self._attack_duration = attack_duration
        self.last_attack:datetime=datetime.datetime.now()
    
    def attack_ray(self:Enemis):
        for i in range(0,101):
            j = i/10
            hit_info = raycast(self.position, direction=(self.x, self.y-j, 0), distance=self.attack_range, ignore=[self], debug=True)
            if hit_info.hit:
                if (datetime.datetime.now()-self.last_attack).total_seconds() < self._attack_duration: return
                self.last_attack = datetime.datetime.now()
    
    def sensore_ray(self:Enemis):
        for y in self.points_on_circle(360, (self.x, self.y)):
            hit_info = raycast(self.position, direction=(y[0], y[1], 0), distance=self.attack_range*2, ignore=[self], debug=True)

    def ray_detection(self:Enemis):
        self.attack_ray()
        self.sensore_ray()

