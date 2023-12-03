from __future__ import annotations
from ursina import *
from Character.character import Character
from Character.enemis import Enemis
from dice import Dice
from Map.Zone import MurCassable, Levier
import datetime

class Player(Character):
    IS_DEBUG_MODE= False
    LEFT = 'a'
    RIGHT = 'd'
    INTERRACT = 'e'
    JUMP = 'space'
    ATTACK = 'left mouse'
    DESTROY = 'right mouse'

    VISION = (4.5,2.5)

    def __init__(self,
                 name='player',
                 height=1/3,
                 width=1/3,
                 weight=2,
                 attack_duration=0.5,
                 speed=3,
                 max_hp=10,
                 attack=2,
                 attack_range=1,
                 defense=3,
                 dice=Dice(6),
                 textures=("Assets/base2.png","Assets/base.png"),
                 position=(0,0,0),
                 enabled=True):
        super().__init__(name=name,
                         attack_range=attack_range,
                        max_hp=max_hp,
                        attack=attack,
                        attack_duration=attack_duration,
                        enabled=enabled,
                        speed=speed,
                        defense=defense,
                        dice=dice,
                        weight=weight,
                        texture=textures[0],
                        position=position,
                        scale=(width,height),
                        model='quad', collider="box")

        self._textures = textures
        self.jump_height = 1

        self.ATTACK_SOUND = Audio("Assets/Quack.mp3")

        self.health_bar = HealthBar(self)
        self.last_attack:datetime=datetime.datetime.now()
        self.last_interract:datetime=datetime.datetime.now()



    def update(self):
        super().update()
        if (Character.CAN_MOVE):
            if held_keys[Player.JUMP] and self.touch_floor():
                self.jump()

            if held_keys[Player.LEFT]:
                self.move_left()
                if self.look_direction == 1:
                    self.look_direction = 0
                    self.texture = self._textures[self.look_direction]

            if held_keys[Player.RIGHT]:
                self.move_right()
                if self.look_direction == 0:
                    self.look_direction = 1
                    self.texture = self._textures[self.look_direction]

            if held_keys[Player.ATTACK]:
                self.attack()

            if held_keys[Player.DESTROY]:
                self.destroyBlock()
                
            if held_keys[Player.INTERRACT]:
                self.interract()

    
    def attack_ray(self:Player, checkFor)->(bool,Entity):
        for y in self.demi_cercle_coords(centre=(self.x, self.y)):
            if self.look_direction == 0:
                h_direction = -1
            else:
                h_direction = 1
            hit_info = raycast(self.position, direction=(y[0]*h_direction, y[1], 0), distance=self._attack_range, ignore=[self], debug=type(self).IS_DEBUG_MODE)

            if not hit_info.hit: continue

            target:Entity = hit_info.entity

            if not issubclass(type(target),checkFor): continue
            return (True, target)
        return (False, None)


    def defense_self(self, damages:int, attacker:Character, reduce_dmg:int = 1):
        super().defense_self(damages * reduce_dmg, attacker)
        self.health_bar.updateHealth()
        
        
    def heal(self, heal_value):
        super().heal(heal_value)
        self.health_bar.updateHealth()
    

    def attack(self):
        if (datetime.datetime.now()-self.last_attack).total_seconds() < self._attack_duration: return
        self.last_attack = datetime.datetime.now()
        self.ATTACK_SOUND.play()
        can_attack, target = self.attack_ray(Enemis)
        if can_attack:
            self.attack_target(target)
    

    def destroyBlock(self):
        if (datetime.datetime.now()-self.last_attack).total_seconds() < self._attack_duration: return
        self.last_attack = datetime.datetime.now()
        self.ATTACK_SOUND.play()
        can_destroy, target = self.attack_ray(MurCassable)
        if can_destroy:
            target:MurCassable
            target.decrease_health()
    

    def interract(self):
        if (datetime.datetime.now()-self.last_interract).total_seconds() < 0.2: return
        for entity in self.intersects().entities:
            if type(entity)==Levier:
                entity:Levier
                entity.action()
                self.last_interract = datetime.datetime.now()
        return




class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_health * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_health * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.48, x=0.4, scale=0.05)

    def updateHealth(self):
        self.health.scale_x = self.player._current_health / self.player._max_health * self.border.scale_x





class Warrior(Player):
    def __init__(self,position=(0,11*0.5,0), textures=("Assets/warrior2.png","Assets/warrior.png"), enabled=True):
        super().__init__(textures=textures, enabled=enabled, position=position)
    def damage(self, roll, target: Character):
        return super().damage(roll, target) + 3 

class Mage(Player):
    def __init__(self,position=(0,11/2,0), textures=("Assets/mage1.png","Assets/mage.png"), enabled=True):
        super().__init__(textures=textures, enabled=enabled, position=position)
    def defense_self(self, damages: int, attacker: Character):
        return super().defense_self(damages, attacker,reduce_dmg=0.8)

class Thief(Player):
    def __init__(self, position=(0,11/2,0), textures=("Assets/thief.png","Assets/thief1.png"), enabled=True):
        super().__init__(textures=textures, enabled=enabled, position=position)
    def damage(self, roll, target: Character):
        return super().damage(roll, target) + target.defense_power()





