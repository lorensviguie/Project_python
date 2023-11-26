from ursina import *
from Player import Player
from dice import Dice
from enemis import Enemis
import map
import asyncio

IS_DEBUG_MODE = False
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE

class HealthBar:
    def __init__(self, player: Player):
        self.player = player
        self.border = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.black, scale_x=player._max_hp * 0.05, scale_y=0.02)
        self.health = Entity(parent=camera.ui, model='quad', z=1, y=-0.4, x=0.4, color=color.red, scale_x=player._current_hp * 0.05, scale_y=0.015)
        self.name_text = Text(parent=camera.ui, text=player._name, z=1, y=-0.48, x=0.4, scale=0.05)

    def update(self):
        self.health.scale_x = self.player._current_hp / self.player._max_hp * self.border.scale_x



app = Ursina()
loop = asyncio.get_event_loop()
player = loop.run_until_complete(map.initMap())

health_bar = HealthBar(player=player)

def update(): 
    camera.position = (player.x, player.y, -20)
app.run()
