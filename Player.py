from ursina import *
from character import Character
from dice import Dice

class Player(Character):
    LEFT = 'a'
    RIGHT = 'd'
    JUMP = 'space'
    ATTACK = 'w'
    __texture = ''

    def get_texture(self):
        return str(self.__texture)

    def __init__(self,name='player',max_hp= 10,attack=2,defense=3,dice = Dice(6), texture_creation='guerrier', move_left_choice='a', move_right_choice='d', jump_choice='space',attack_choice = 'w', texture='Assets/floor.png', position=(0,0,0)):
        super().__init__(name=name,
                        max_hp=max_hp,
                        attack=attack,
                        defense=defense,
                        dice=dice,
                        texture_creation=texture_creation,
                        texture=texture, position=position, scale=(1/2,1/2), model='quad', collider="box")

        self._move_left = move_left_choice
        self._move_right = move_right_choice
        self._jump = jump_choice
        #self._attack = attack_choice
        self.__texture = texture_creation
        self.jump_height = 1

        self.health_bar = HealthBar(self)
        #self.y_speed = 0
        #self.is_attacking = False


    def update(self):
        super().update()

        if held_keys[Player.JUMP] and self.touch_floor():
            self.jump()
        #if self.is_attacking:
        #    temp = str('./asset/'+ self.get_texture().split('.')[0] +'_attack.png')            
        #    self.texture = temp

        # Gestion du déplacement avec les touches du clavier
        if held_keys[Player.LEFT]:
            self.move_left()
        if held_keys[Player.RIGHT]:
            self.move_right()
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

class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_health * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_health * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.48, x=0.4, scale=0.05)

    def updateHealth(self):
        self.health.scale_x = self.player._current_health / self.player._max_health * self.border.scale_x


