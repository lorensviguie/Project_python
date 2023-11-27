from ursina import *
from direct.actor.Actor import Actor

def create_game_window():
    def on_play_button_click():
        print("Bouton PLAY cliqué !")
        Quack = Audio("Quack.mp3")
        Quack.play()

    def on_warrior_button_click():
        print("Bouton Warrior cliqué !")

    def on_mage_button_click():
        print("Bouton Mage cliqué !")

    def on_thief_button_click():
        print("Bouton Thief cliqué !")

    app = Ursina()
    text1 = Text(text="WELCOME TO DUCK.EXE", scale=4, origin=(0, -3))
    text2 = Text(text="Choose a class", scale=2, origin=(0, -3.5), color=color.cyan)
    warrior = Text(text="Warrior", scale=1, origin=(4, 5))
    mage = Text(text="Mage", scale=1, origin=(0, 5))
    thief = Text(text="Thief", scale=1, origin=(-6.5, 5))
    play_button = Button(text='PLAY', color=color.green, scale=(0.2, 0.1), origin=(0, 2.5), on_click=on_play_button_click,
                         highlight_color=color.white)
    warrior_button = Button(scale=(0.3, 0.3), origin=(1.2, 0), color=color.clear, on_click=on_warrior_button_click)
    mage_button = Button(scale=(0.3, 0.3), origin=(0, 0), color=color.clear, on_click=on_mage_button_click)
    thief_button = Button(scale=(0.3, 0.3), origin=(-1.2, 0), color=color.clear, on_click=on_thief_button_click)
    duck1 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), origin=(-2, 0))
    duck2 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), origin=(0, 0))
    duck3 = Entity(model='quad', texture='/base.png', scale=(1.5, 1.5), origin=(2, 0))
    music = Audio("musique_Tetris.mp3", loop=True)
    music.play()
    app.run()

create_game_window()
