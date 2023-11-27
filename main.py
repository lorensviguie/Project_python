from ursina import *
from Player import Player
from dice import Dice
from enemis import Enemis
import map
import asyncio

IS_DEBUG_MODE = False
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE


app = Ursina()
loop = asyncio.get_event_loop()
player = loop.run_until_complete(map.initMap())


def update():
    camera.position = (player.x, player.y, -15)

app.run()

