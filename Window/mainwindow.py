from ursina import *
from Window.window import Window
from Character.Player import *

class MainWindow(Window):

    def __init__(self, camera, cameraPosition=(-10,-10)):
        super().__init__(camera=camera, cameraPosition=cameraPosition)
        self.classe = Warrior
        self._camera.z=-20
    
    def on_warrior_button_click(self):
        if Window.CURRENT_WINDOW != 0: return
        self.classe = Warrior

    def on_mage_button_click(self):
        if Window.CURRENT_WINDOW != 0: return
        self.classe = Mage

    def on_thief_button_click(self):
        if Window.CURRENT_WINDOW != 0: return
        self.classe = Thief

    def createWindow(self):
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

        self.duck1 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(-13, -10, -1))
        self.duck2 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(-10, -10, -1))
        self.duck3 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), position=(-7, -10, -1))

    def on_play_button_click(self)->str:
        if Window.CURRENT_WINDOW != 0: return
        print("Bouton PLAY cliqué !")
        Audio("Assets/Quack.mp3")
        self.destroyWindow()
        Window.CURRENT_WINDOW = 1

    
    def destroyWindow(self):
        destroy(self.text1)
        destroy(self.text2)
        destroy(self.warrior)
        destroy(self.mage)
        destroy(self.thief)
        destroy(self.play_button)
        destroy(self.duck1)
        destroy(self.duck2)
        destroy(self.duck3)
