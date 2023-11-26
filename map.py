from ursina import *
from enemis import Enemis
from Player import Player

UNITE_DE_MESURE = 1 * 0.5


#     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant    4 -> Enemis    5->Player

mapTab = [
    [2,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,3,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,3,0,0,0,0,3,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,1,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,4,0,0,3,3,0,0,0,0],
    [2,5,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,1,1,1,1,1,1,1,1,1,1,1]
]

async def initMap():
    mapTab.reverse()
    for y, ligne in enumerate(mapTab):
        for x, valeur in enumerate(ligne):
            if(valeur == 2):
                m = Entity(model='quad', color=color.red, scale=(1, 1), position=(x, y), collider='box')
                #m.collider.visible = True
            if(valeur == 1):
                m = Entity(model='quad', color=color.green, scale=(1, 1), position=(x, y), texture='Assets/floor.png', collider='box')
                #m.collider.visible = True

            if(valeur == 3):
                m = Entity(model='quad', color=color.green, scale=(1, 0.65), position=(x, y), texture='Assets/pxArt.png', collider='box')
                #m.collider.visible = True

            if(valeur == 4):
                time.sleep(1)
                enemis = Enemis(position=(x, len(mapTab) - y))

            if(valeur == 5):
                time.sleep(1)
                player = Player(position=(6,4,0), texture='Assets/base.png')
    return player

