from ursina import *
from Character.Player import *
from Character.enemis import Enemis
from gamemanager import GameManager
from Map.map import Map

IS_DEBUG_MODE = False
ON_PLAYER_VISION = False
Map.ON_PLAYER_VISION = ON_PLAYER_VISION
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE
Player.IS_DEBUG_MODE = IS_DEBUG_MODE

app = Ursina()

gamemanager = GameManager(camera)

gamemanager.mainWindow.showWindow()

def update():
    gamemanager.update()


app.run()
