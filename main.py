from ursina import *
from direct.actor.Actor import Actor

def on_play_button_click():
    print("Bouton PLAY cliqué !")

app = Ursina()
text = Text(text="WELCOME TO DUCK.EXE", scale=4, origin=(0,-2))
play_button = Button(text='PLAY', color=color.green, scale=(0.2, 0.1), origin=(0,2), on_click=on_play_button_click)

app.run()

