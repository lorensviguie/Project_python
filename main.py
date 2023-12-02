from ursina import *
from Character.Player import *
from Character.enemis import Enemis
from gamemanager import GameManager

IS_DEBUG_MODE = False
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE
Player.IS_DEBUG_MODE = IS_DEBUG_MODE

app = Ursina()

gamemanager = GameManager(camera)

gamemanager.mainWindow.showWindow()

def update():
    gamemanager.update()


app.run()
