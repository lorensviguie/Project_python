from __future__ import annotations
from ursina import *
from character import Character
from dice import Dice
import datetime

class Player(Character):
    IS_DEBUG_MODE= False
    LEFT = 'a'
    RIGHT = 'd'
    JUMP = 'space'
    ATTACK = 'left mouse'
    __texture = ''
    ATTACK_SOUND = Audio("Quack.mp3")

    def get_texture(self):
        return str(self.__texture)

    def __init__(self,name='player', height=1/3, width=1/3, weight=2, attack_duration=1, speed=3,max_hp= 10,attack=2,attack_range=2,defense=3,dice = Dice(6), texture_creation='guerrier', move_left_choice='a', move_right_choice='d', jump_choice='space',attack_choice = 'w', texture='Assets/floor.png', position=(0,0,0), enabled=False):
        super().__init__(name=name,
                         attack_range=attack_range,
                        max_hp=max_hp,
                        attack=attack,
                        enabled=enabled,
                        speed=speed,
                        defense=defense,
                        dice=dice,
                        weight=weight,
                        texture_creation=texture_creation,
                        texture=texture, position=position, scale=(width,height), model='quad', collider="box")

        self._move_left = move_left_choice
        self._move_right = move_right_choice
        self._jump = jump_choice
        #self._attack = attack_choice
        self.__texture = texture_creation
        self.jump_height = 1

        self.health_bar = HealthBar(self)
        self._attack_duration = attack_duration
        self.last_attack:datetime=datetime.datetime.now()
        #self.y_speed = 0
        #self.is_attacking = False


    def update(self):
        super().update()
        if held_keys[type(self).JUMP] and self.touch_floor():
            self.jump()

        if held_keys[type(self).LEFT]:
            self.move_left()
            self.texture='Assets/base2.png'
            self.look_direction = -1
        if held_keys[type(self).RIGHT]:
            self.move_right()
            self.texture='Assets/base.png'
            self.look_direction = 1
        if held_keys[type(self).ATTACK]:
            self.attack()
    
    def attack_ray(self:Player)->(bool,Entity):
        for y in self.demi_cercle_coords(centre=(self.x, self.y)):
            hit_info = raycast(self.position, direction=(y[0]*self.look_direction, y[1], 0), distance=self._attack_range, ignore=[self], debug=type(self).IS_DEBUG_MODE)
            if not hit_info.hit: continue

            target:Entity = hit_info.entity
            if target.name != "enemis": continue

            return (True, target)
        return (False, None)
    
    def ray_detection(self:Player):
        self.attack_ray()


        # Rétablir le skin original après la fin de l'attaque
        #if not self.is_attacking:
        #    self.texture =str('./asset/'+ str(self.get_texture()))

    def defense_self(self, damages:int, attacker:Character):
        super().defense_self(damages, attacker)
        self.health_bar.updateHealth()

    #def attack_animation(self):
    #    self.is_attacking = True
    #    invoke(self.end_attack_animation, delay=0.2)  # Appeler end_attack_animation après 0.5 secondes

    #def end_attack_animation(self):
    #    self.is_attacking = False
    
    def attack(self):
        Player.ATTACK_SOUND.play()
        can_attack, target = self.attack_ray()
        if can_attack:
            if (datetime.datetime.now()-self.last_attack).total_seconds() < self._attack_duration: return
            self.last_attack = datetime.datetime.now()
            self.attack_target(target)

class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_health * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_health * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.48, x=0.4, scale=0.05)

    def updateHealth(self):
        self.health.scale_x = self.player._current_health / self.player._max_health * self.border.scale_x


