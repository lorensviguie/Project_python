from ursina import *
from Character.enemis import Enemis, Wolf, Human, Frog
from Character.Player import Player
from Map.Zone import Zone,Sol,Mur,SolVolant,MurPlein,MurCassable,Heal,Activable,End,Levier
import numpy as np

class Map(Entity):

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
        11:"Levier",
        "E":"End"
    }

    def __init__(self):
        self._player = None
        self._map_is_initiate = False
        self._leviers = {
            0:False,
            1:False
        }

        self._mapTab = [
            [0,0,0,0,0,0,0,0,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,4,0,0],
            [2,4,0,0,0,0,3,3,0,0,3,3,3,3,3,0,0,0,0,0,0,0,3,2,0,0,0,3,3,3,2],
            [2,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0,3,0,0,2,0,5,0,7,7,7,0],
            [2,0,0,0,3,3,0,0,0,3,0,0,0,0,0,0,0,0,0,0,4,0,0,0,3,3,0,7,7,7,0],
            [0,0,0,2,0,0,0,0,0,0,3,0,0,0,0,0,0,0,3,3,3,0,0,0,0,0,3,3,3,7,2],
            [0,7,0,2,8,0,0,0,0,0,0,0,3,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,9,0,2],
            [11,2,0,0,3,0,0,0,3,3,0,0,0,0,3,3,0,2,0,4,0,0,0,0,0,4,7,'E',9,0,2],
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
            [2,0,0,0,0,0,0,0,0,8,2,0,0,3,0,0,0,0,0,10,0,0,3,0,0,0,2,0,0,0,2],
            [2,3,0,3,3,3,3,3,3,3,3,4,0,0,0,0,4,2,9,9,9,2,8,0,0,0,2,0,0,0,2],
            [0,0,11,0,0,0,0,0,0,0,0,3,3,3,3,0,3,2,0,0,0,2,3,3,3,0,2,4,0,4,2],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,3,3,3,3,3,3,3,3,3,3]
        ]
    
    def spawnPlayer(self, classe):
        self._player = classe(position=(0,11/2,0), enabled=True)
        self.player._gravity = True

    @property
    def player(self)->Player:
        return self._player

    @property
    def levier(self):
        return self._leviers

    async def initMap(self):
        self._mapTab.reverse()
        for y, ligne in enumerate(self._mapTab):
            for x, valeur in enumerate(ligne):

                if valeur == 0 or valeur == "S": continue

                self._mapTab[y][x] = getattr(sys.modules[__name__], Map.intToZone[valeur])(map=self,position=(x/2, y/2))

        self._map_is_initiate = True
    
    def showMap(self):
        if not self._map_is_initiate: return
        for l, ligne in enumerate(self._mapTab):
            for h, zone in enumerate(ligne):
                if zone == 0 or zone == "S": continue
                if issubclass(type(zone), Zone) and not zone.is_spawn:
                    zone.disable()
                elif zone.x in np.arange(self.player.current_zone[0]-Player.VISION[0], self.player.current_zone[0]+Player.VISION[0], 0.5) and zone.y in np.arange(self.player.current_zone[1]-Player.VISION[1], self.player.current_zone[1]+Player.VISION[1], 0.5) :
                    zone.enable()
                    if issubclass(type(zone), Enemis) and not zone.is_alive():
                        zone.disable()
                else:
                    if l != len(self._mapTab)-1:
                        if issubclass(type(self._mapTab[l+1][h]),Enemis) and type(self._mapTab[l+1][h]).enabled: continue
                    zone.disable()
    
    def clearMap(self):
        for ligne in self._mapTab:
            for zone in ligne:
                if not issubclass(type(zone), Entity): continue
                destroy(zone)
    
    def changeLevierStatus(self, key,value):
        self._leviers[key]=value
