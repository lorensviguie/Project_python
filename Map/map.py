from ursina import *
from Character.enemis import Enemis, Wolf, Human, Frog
from Character.Player import Player
from Map.Zone import Zone,Sol,Mur,SolVolant,MurPlein,MurCassable,Heal,Activable,End
import numpy as np

class Map(Entity):

    #     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant    4 -> Frog   6-> mur plein  7 -> mur cassable  8-> heal  9-> activable 5 -> Wolf 10->Human

    intToZone = {
        0:"",
        1:"Sol",
        2:"Mur",
        3:"SolVolant",
        4:"Frog",
        5:"Wolf",
        6:"MurPlein",
        7:"MurCassable",
        8:"Heal",
        9:"Activable",
        10:"Human",
        "E":"End"
    }


    mapTab = [
        [0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,4,0,0],
        [2,4,0,0,0,0,3,3,0,0,3,3,3,3,3,0,0,0,0,0,0,0,3,2,0,0,0,3,3,3,2],
        [2,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,2,0,5,0,7,7,7,0],
        [2,0,0,0,3,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0,4,0,0,0,3,3,0,7,7,7,0],
        [0,0,0,2,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,3,3,3,7,2],
        [0,7,0,2,8,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,0,2],
        [9,2,0,0,3,0,0,0,3,3,0,0,0,0,3,3,0,2,0,4,0,0,0,0,0,4,7,'E',9,0,2],
        [3,0,0,0,0,0,0,0,0,0,0,3,0,0,4,0,0,2,3,3,7,3,3,3,3,3,3,3,3,0,2],
        [0,0,0,0,0,0,0,3,0,0,0,0,0,3,3,3,0,2,0,0,0,0,0,0,2,0,0,0,0,0,2],
        ['S',0,0,0,0,0,0,0,0,0,3,3,3,0,0,0,0,2,0,0,0,0,0,0,2,0,0,0,0,3,2],
        [3,7,3,3,0,0,0,0,0,3,0,0,0,0,4,3,3,2,0,0,0,0,4,2,0,3,3,0,0,0,2],
        [4,0,0,0,0,3,3,3,3,0,0,2,0,3,3,0,0,2,0,8,0,0,2,2,0,0,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,7,3,2,0,0,0,0,0,2,3,3,3,0,2,2,0,0,0,0,3,0,2],
        [2,0,3,3,3,3,3,3,3,0,0,0,3,0,0,0,0,0,0,0,0,0,2,2,0,3,0,0,0,0,2],
        [2,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,3,3,0,2],
        [2,0,4,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
        [2,0,3,3,0,0,0,0,3,3,2,3,0,0,0,0,0,0,0,0,0,0,0,3,3,0,0,0,0,3,2],
        [2,0,0,0,0,0,0,0,0,8,2,0,0,0,0,0,0,0,0,10,0,0,3,0,0,0,2,0,0,0,2],
        [2,3,0,3,3,3,3,3,3,3,3,4,0,0,0,0,4,2,9,9,9,2,8,0,0,0,2,0,0,0,2],
        [0,0,9,0,0,0,0,0,0,0,0,3,3,3,3,0,3,2,0,0,0,2,3,3,3,0,2,4,0,4,2],
        [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,3,3,3,3,3,3,3,3,3,3],
    ]

    def __init__(self):
        self._player = None
        self._map_is_initiate = False
    
    def spawnPlayer(self, classe):
        self._player = classe(position=(0,11/2,0), enabled=True)
        self.player._gravity = True

    @property
    def player(self)->Player:
        return self._player

    #     0 -> Air    1 -> Sol    2 -> Mur 3 -> Sol Volant    4 -> Enemis   6-> mur plein  7 -> mur cassable  8-> heal  9-> activable
    async def initMap(self):
        Map.mapTab.reverse()
        for y, ligne in enumerate(Map.mapTab):
            for x, valeur in enumerate(ligne):

                if valeur == 0 or valeur == "S": continue

                Map.mapTab[y][x] = getattr(sys.modules[__name__], Map.intToZone[valeur])(position=(x/2, y/2))

        self._map_is_initiate = True
    
    def showMap(self):
        if not self._map_is_initiate: return
        for l, ligne in enumerate(Map.mapTab):
            for h, zone in enumerate(ligne):
                if zone == 0 or zone == "S" or (not issubclass(type(zone), Enemis) and not zone.is_spawn): continue
                if zone.x in np.arange(self.player.current_zone[0]-Player.VISION[0], self.player.current_zone[0]+Player.VISION[0], 0.5) and zone.y in np.arange(self.player.current_zone[1]-Player.VISION[1], self.player.current_zone[1]+Player.VISION[1], 0.5) :
                    zone.enable()
                    if issubclass(type(zone), Enemis) and not zone.is_alive():
                        zone.disable()
                else:
                    if l != len(Map.mapTab)-1:
                        if issubclass(type(Map.mapTab[l+1][h]),Enemis) and type(Map.mapTab[l+1][h]).enabled: continue
                    zone.disable()


