from ursina import *
from Character.enemis import *
from Character.Player import *
from Map.Zone import *
import numpy as np

class Map(Entity):

    ECHELLE = 0.5
    ON_PLAYER_VISION = False

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
            [6,2,11,2,6,6,6,6,6,6,6,3,3,3,3,0,3,2,0,0,0,2,3,3,3,0,2,4,0,4,2],
            [6,6,3,6,6,6,6,6,6,6,6,6,6,6,6,3,6,2,0,0,0,2,6,6,6,3,6,3,3,3,2]
        ]


    @property
    def player(self)->Player:
        return self._player


    @property
    def levier(self)->dict:
        return self._leviers


    def spawnPlayer(self, classe:Player)->None:
        """
        Entrée :
            - classe:str  'Contiens la classe du joueur'
        Sortie : Aucune
        
        Permet de faire apparaître le joueur sur la map avec la classe séléctionné
        """
        if classe not in [Thief, Warrior, Mage]:
            classe = Warrior
        self._player = classe(position=(0,11*Map.ECHELLE,0), enabled=True)
        self.player._gravity = True


    async def initMap(self)->None:
        """
        Entrée : Aucune
        Sortie : Aucune

        Convertie les caractères du tableau de la map en Entité visible pour le jeu        
        """
        self._mapTab.reverse()
        for y, ligne in enumerate(self._mapTab):
            for x, valeur in enumerate(ligne):

                if valeur == 0 or valeur == "S": continue

                self._mapTab[y][x] = getattr(sys.modules[__name__], Map.intToZone[valeur])(map=self,position=(x*Map.ECHELLE, y*Map.ECHELLE))

    
    def showMap(self)->None:
        """
        Entrée : Aucune
        Sortie : Aucune

        Permet l'affichage de la Map visible par le joueur
        """
        if not Map.ON_PLAYER_VISION: return
        
        for l, ligne in enumerate(self._mapTab):
            for h, zone in enumerate(ligne):

                if zone == 0 or zone == "S": continue
                
                if issubclass(type(zone), Zone) and not zone.is_spawn:
                    zone.disable()

                elif (zone.x in np.arange(self.player.current_zone[0]-Player.VISION[0], self.player.current_zone[0]+Player.VISION[0], Map.ECHELLE) 
                      and zone.y in np.arange(self.player.current_zone[1]-Player.VISION[1], self.player.current_zone[1]+Player.VISION[1], Map.ECHELLE)):
                    zone.enable()

                    if issubclass(type(zone), Enemis) and not zone.is_alive():
                        zone.disable()

                else:

                    if (l != len(self._mapTab)-1) and issubclass(type(self._mapTab[l+1][h]),Enemis) and type(self._mapTab[l+1][h]).enabled: continue
                    zone.disable()
    

    def clearMap(self)->None:
        """
        Entrée : Aucune
        Sortie : Aucune
        
        Détruit toutes les zones de la map
        """
        for ligne in self._mapTab:
            for zone in ligne:

                if not issubclass(type(zone), Entity): continue
                destroy(zone)
    

    def changeLevierStatus(self, key:int,value:bool)->None:
        """
        Entrée : 
            - key:int  'Contiens l'élément permettant d'identifié le levier à modifier
            - value:bool  'Contiens le nouvel état du levier' 
        Sortie : Aucune
        
        Permet de modifier l'état d'un levier
        """
        self._leviers[key]=value
