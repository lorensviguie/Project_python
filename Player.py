from ursina import *
from character import Character
from dice import Dice

class Player(Character):
    _move_left = ''
    _move_right = ''
    _jump = ''
    _attack = ''
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
                        texture=texture, position=position, scale=(1,1), model='quad', collider="box")

        self._move_left = move_left_choice
        self._move_right = move_right_choice
        self._jump = jump_choice
        self._attack = attack_choice
        self.__texture = texture_creation
        self.gravity = 5
        self.jump_height = 1
        self.jump_speed = 4
        self.y_speed = 0
        self.is_jumping = False
        self.is_attacking = False


    def update(self):
        super().update()
        if self.is_attacking:
            temp = str('./asset/'+ self.get_texture().split('.')[0] +'_attack.png')            
            self.texture = temp

        # Gestion du déplacement avec les touches du clavier
        if held_keys[self._move_left]:
            self.x -= 5 * time.dt
        if held_keys[self._move_right]:
            self.x += 5 * time.dt

        # Gestion des collisions avec la carte
        """hit_info = raycast(self.position, self.down, distance=0.4, ignore=[self])
        if hit_info.hit:
            self.y = hit_info.world_point[1] + 0.4  # Ajustement de la hauteur après la collision
            self.y_speed = 0
            self.is_jumping = False"""

        # Gestion du saut avec la barre d'espace
        if held_keys[self._jump] and not self.is_jumping:
            self.y_speed = self.jump_speed
            self.is_jumping = True

        # Gestion de l'attaque avec la touche spécifiée
        if held_keys[self._attack]:
            self.attack_animation()

        # Rétablir le skin original après la fin de l'attaque
        if not self.is_attacking:
            self.texture =str('./asset/'+ str(self.get_texture()))


    def attack_animation(self):
        self.is_attacking = True
        invoke(self.end_attack_animation, delay=0.2)  # Appeler end_attack_animation après 0.5 secondes

    def end_attack_animation(self):
        self.is_attacking = False


