from ursina import *
from enemis import Enemis
from Player import Player

UNITE_DE_MESURE = 1 * 0.5


#     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant    4 -> Enemis    5->Player   6-> mur plein

mapTab = [
    [2,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
    [2,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0],
    [2,0,0,0,4,0,0,0,0,0,0,1,1,0,0,0,4,0,0,0,0,0,0,1,1],
    [2,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
    [2,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0],
    [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [2,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1],
    [2,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0],
    [6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6],
    [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6]
]

async def initMap():
    mapTab.reverse()
    for y, ligne in enumerate(mapTab):
        for x, valeur in enumerate(ligne):
            if(valeur == 2):
                m = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), collider='box', texture='Assets/mur.png', enabled=True)
            if(valeur == 1):
                m = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/sol.png', collider='box', enabled=True)

            if(valeur == 3):
                m = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/sol.png', collider='box', enabled=True)

            if(valeur == 6):
                m = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/murplein.png', enabled=True)

            if(valeur == 4):
                enemis = Enemis(position=(x/2, y/2))

            if(valeur == 5):
                player = Player(position=(x/2,y/2,0), texture='Assets/base.png')
    return player

