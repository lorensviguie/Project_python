from ursina import *
from Player import *
from enemis import Enemis
from map import Map
import asyncio

IS_DEBUG_MODE = False
Enemis.IS_DEBUG_MODE = IS_DEBUG_MODE
Player.IS_DEBUG_MODE = IS_DEBUG_MODE

SOUND_ON = False

is_Homewindow_Open = True
classe = "Warrior"

def get_window_status():
    return is_Homewindow_Open

def set_window_status(status=False):
    global is_Homewindow_Open
    is_Homewindow_Open = status

class GameWindow(Entity):
    def __init__(self):
        super().__init__()

        self.create_game_window()

    def on_warrior_button_click(self):
        global classe
        classe = "Warrior"
        print("Bouton Warrior cliqué !")

    def on_mage_button_click(self):
        global classe
        classe = "Mage"
        print("Bouton Mage cliqué !")

    def on_thief_button_click(self):
        global classe
        classe = "Thief"
        print("Bouton Thief cliqué !")

    def create_game_window(self):
        self.text1 = Text(text="WELCOME TO DUCK.EXE", scale=4, origin=(0, -3))
        self.text2 = Text(text="Choose a class", scale=2, origin=(0, -3.5), color=color.cyan)
        self.warrior = Text(text="Warrior", scale=1, origin=(4, 5))
        self.mage = Text(text="Mage", scale=1, origin=(0, 5))
        self.thief = Text(text="Thief", scale=1, origin=(-6.5, 5))
        self.play_button = Button(text='PLAY', color=color.green, scale=(0.2, 0.1), origin=(0, 2.5), on_click=self.on_play_button_click,
                         highlight_color=color.white)
        
        self.warrior_button = Button(scale=(0.3, 0.3), origin=(1.2, 0), color=color.clear, on_click=self.on_warrior_button_click)
        self.mage_button = Button(scale=(0.3, 0.3), origin=(0, 0), color=color.clear, on_click=self.on_mage_button_click)
        self.thief_button = Button(scale=(0.3, 0.3), origin=(-1.2, 0), color=color.clear, on_click=self.on_thief_button_click)

        self.duck1 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(2.8, 6.5, -1))
        self.duck2 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(-1.4, 6.5, -1))
        self.duck3 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(0.7, 6.5, -1))

        if SOUND_ON:
            self.music = Audio("musique_Tetris.mp3", loop=True)
            self.music.play()

    def on_play_button_click(self):
        print("Bouton PLAY cliqué !")
        Quack = Audio("Quack.mp3")
        Quack.play()
        self.text1.disable()
        self.text2.disable()
        self.warrior.disable()
        self.mage.disable()
        self.thief.disable()
        self.play_button.disable()
        self.duck1.disable()
        self.duck2.disable()
        self.duck3.disable()
        set_window_status(False)
        self.hide()

    def hide(self):
        self.disable()


app = Ursina()
game_window = GameWindow()

loop = asyncio.get_event_loop()
 
map=Map()
player:Character = None

loop.run_until_complete(map.initMap())
camera.position=(0.5,6,-15)
def update():
    global player
    if get_window_status(): return
    if player == None:
        map.spawnPlayer(eval(classe))
        player = map.player
    else:
        if not player.is_alive():
            Character.CAN_MOVE = False
            camera.z=-15
            player.disable()
        else:
            Character.CAN_MOVE = True
            camera.position = (player.x, player.y, -10)
            map.showMap()

app.run()
