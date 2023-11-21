from ursina import *
from direct.actor.Actor import Actor
from enemis import Enemis
import map


class Player(Entity):
    def __init__(self, position=(2, 2, 0)):
        super().__init__(
            model='sphere',
            color=color.blue,
            scale=(1, 1, 1),
            position=position,
            collider='box'
        )
        self.attack_range = 2


app = Ursina()

map.initMap()
camera.position = (5, 5, -20)
test = Enemis(position=(4,4,0))
player = Player(position=(5,4,0))

app.run()
