from ursina import *
from character import Character
from dice import Dice

class Player(Character):
    LEFT = 'a'
    RIGHT = 'd'
    JUMP = 'space'
    ATTACK = 'w'
    __texture = ''
    ATTACK_SOUND = Audio("Quack.mp3")
    _can_moove = False
    _texture_base_R = ""
    _texture_base_G = ""

    def get_texture(self):
        return str(self.__texture)
    def get_texture_base(self):
        return self._texture_base_G , self._texture_base_R
    def get_texture_base_G(self):
        return self._texture_base_G
    def get_texture_base_R(self):
        return self._texture_base_R
    def set_texture_base(self, base_G,base_D):
        self._texture_base_G = base_G
        self._texture_base_R = base_D

    def __init__(self,name='player', height=1/3, width=1/3, weight=2, speed=3,max_hp= 10,attack=2,defense=3,dice = Dice(6), texture_creation='guerrier', move_left_choice='a', move_right_choice='d', jump_choice='space',attack_choice = 'w', texture='Assets/floor.png', position=(0,0,0), enabled=False):
        super().__init__(name=name,
                        max_hp=max_hp,
                        attack=attack,
                        speed=speed,
                        defense=defense,
                        dice=dice,
                        weight=weight,
                        texture_creation=texture_creation,
                        texture=texture, position=position, scale=(width,height), model='quad', collider="box")

        self.set_texture_base("Assets/base2.png","Assets/base.png")
        self._move_left = move_left_choice
        self._move_right = move_right_choice
        self._jump = jump_choice
        #self._attack = attack_choice
        self.__texture = texture_creation
        self.jump_height = 1

        self.health_bar = HealthBar(self)
        #self.y_speed = 0
        #self.is_attacking = False
    def set_can_moove(self,move=True):
        self._can_moove = move
    def get_can_move(self):
        return self._can_moove

    def update(self):
        super().update()
        if (self.get_can_move()):
            if held_keys[Player.JUMP] and self.touch_floor():
                self.jump()

            if held_keys[Player.LEFT]:
                self.move_left()
                self.texture=self.get_texture_base_G()
            if held_keys[Player.RIGHT]:
                self.move_right()
                self.texture= self.get_texture_base_R()
            if held_keys[Player.ATTACK]:
                self.attack_animation()


        # Rétablir le skin original après la fin de l'attaque
        #if not self.is_attacking:
        #    self.texture =str('./asset/'+ str(self.get_texture()))

    def defense_self(self, damages:int, attacker:Character):
        super().defense_self(damages, attacker)
        self.health_bar.updateHealth()

    def attack_animation(self):
        self.is_attacking = True
        invoke(self.end_attack_animation, delay=0.2)  # Appeler end_attack_animation après 0.5 secondes

    def end_attack_animation(self):
        self.is_attacking = False
    
    def attack(self):
        Player.ATTACK_SOUND.play()

    def select_clas(self,classe):
            return Warrior(self)

class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_health * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_health * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.48, x=0.4, scale=0.05)

    def updateHealth(self):
        self.health.scale_x = self.player._current_health / self.player._max_health * self.border.scale_x


class Warrior(Player):
    def __init__(self, name='player', height=1 / 3, width=1 / 3, weight=2, speed=3, max_hp=10, attack=2, defense=3, dice=Dice(6), texture_creation='guerrier', move_left_choice='a', move_right_choice='d', jump_choice='space', attack_choice='w', texture='Assets/floor.png', position=(0, 0, 0), enabled=False):
        super().__init__(name, height, width, weight, speed, max_hp, attack, defense, dice, texture_creation, move_left_choice, move_right_choice, jump_choice, attack_choice, texture, position, enabled)
        self.set_texture_base("Assets/warrior2.png","Assets/warrior.png")
    