from ursina import *
from Player import Player
from character import Dice

class GameMap(Entity):
    def __init__(self, size=20):
        super().__init__()
        self.size = size
        self.create_map()

    def create_map(self):
        for i in range(self.size):
            for j in range(self.size):
                cube = Entity(
                    model='cube',
                    texture='grass_texture.png',
                    collider='box',
                    scale=(1, 0.1, 1),
                    position=(i - self.size // 2, 0, j - self.size // 2)
                )
class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_hp * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_hp * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.45, x=0.4, scale=0.05)

    def update(self):
        self.health.scale_x = self.player._current_hp / self.player._max_hp * self.border.scale_x


app = Ursina()

# Création de la carte
game_map = GameMap(size=20)

# Création du joueur

player2 = Player(
    name="Guerrier",
    max_hp=10,
    attack=2,
    defense=3,
    texture_creation="guerrier",
    move_left_choice='j',
    move_right_choice='l',
    jump_choice='k'
)
player1 = Player(
    name="frog",
    max_hp=10,
    attack=2,
    defense=3,
    texture_creation="frog",
    move_left_choice='a',
    move_right_choice='d',
    jump_choice='space'
)
health_bar = HealthBar(player=player1)


app.run()
