from ursina import *
from Player import Player
from dice import Dice
from enemis import Enemis
from map import Map
import asyncio

IS_DEBUG_MODE = False
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE
Player.IS_DEBUG_MODE = IS_DEBUG_MODE


app = Ursina()
loop = asyncio.get_event_loop()

map = Map()
loop.run_until_complete(map.initMap())
player = map.player

def update():
    camera.position = (player.x, player.y, -15)
    map.showMap()

app.run()

