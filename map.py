from ursina import *

UNITE_DE_MESURE = 1 * 0.5


#     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant

mapTab = [
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,3,0,0,0,0,3,0,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,1,1,0,0,0,0,0,0,2],
    [2,0,0,0,0,0,0,3,0,2],
    [2,0,0,0,0,0,0,0,0,2],
    [2,1,1,1,1,1,1,1,1,2]
]

def initMap():
    for y, ligne in enumerate(mapTab):
        for x, valeur in enumerate(ligne):
            if(valeur == 2):
                Entity(model='quad', color=color.red, scale=(1, 1), position=(x, len(mapTab) - y))
            if(valeur == 1):
                Entity(model='quad', color=color.green, scale=(1, 1), position=(x, len(mapTab) - y), texture='Assets/floor.png', collider='quad')
            if(valeur == 3):
                Entity(model='quad', color=color.green, scale=(1, 0.65), position=(x, len(mapTab) - y), texture='Assets/pxArt.png', collider='quad')

