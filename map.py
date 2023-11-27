from ursina import *
from enemis import Enemis
from Player import Player
import numpy as np

class Map(Entity):

    #     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant    4 -> Enemis    5->Player   6-> mur plein

    mapTab = [
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,2],
        [2,0,0,0,4,0,0,0,0,0,0,1,1,0,0,0,4,0,0,0,0,0,0,1,1,2],
        [2,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,3,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,2],
        [2,0,0,0,0,0,4,0,0,0,0,0,0,0,0,0,0,0,4,0,0,0,0,0,0,2],      #24/15
        [6,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
        [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2],
        [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2],
        [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2],
        [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2],
        [6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,2]
    ]

    def __init__(self):
        self._player = Player(position=(2/2,9/2,0), texture='Assets/base.png', enabled=False)
        self._map_is_initiate = False


    @property
    def player(self)->Player:
        return self._player

    async def initMap(self):
        Map.mapTab.reverse()
        for y, ligne in enumerate(Map.mapTab):
            for x, valeur in enumerate(ligne):
                if(valeur == 2):
                    Map.mapTab[y][x] = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), collider='box', texture='Assets/mur.png', enabled=False)
                if(valeur == 1):
                    Map.mapTab[y][x] = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/sol.png', collider='box', enabled=False)
                if(valeur == 3):
                    Map.mapTab[y][x] = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/sol.png', collider='box', enabled=False)
                if(valeur == 6):
                    Map.mapTab[y][x] = Entity(model='quad', scale=(1/2, 1/2), position=(x/2, y/2), texture='Assets/murplein.png', enabled=False)
                if(valeur == 4):
                    Map.mapTab[y][x] = Enemis(position=(x/2, y/2), enabled=False)
        self.player.enable()
        self._map_is_initiate = True
    
    def showMap(self):
        if not self._map_is_initiate: return
        for l, ligne in enumerate(Map.mapTab):
            for h, zone in enumerate(ligne):
                if type(zone) != Entity and type(zone) != Enemis: continue
                if zone.x in np.arange(self.player.current_zone[0]-8, self.player.current_zone[0]+8, 0.5) and zone.y in np.arange(self.player.current_zone[1]-4, self.player.current_zone[1]+4, 0.5) :
                    zone.enable()
                else:
                    if l != len(Map.mapTab)-1:
                        if type(zone) is Entity and type(Map.mapTab[l+1][h]) is Enemis and type(Map.mapTab[l+1][h]).enabled: continue
                    zone.disable()


