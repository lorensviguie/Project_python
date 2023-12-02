from ursina import *
from Window.window import Window
from Map.map import Map
from Character.Player import *
from Character.character import Character
import asyncio

class GameWindow(Window):
    def __init__(self, camera, cameraPosition=(0,0), classe="Warrior"):
        super().__init__(camera=camera, cameraPosition=cameraPosition)
        self._map:Map = None
        self._player:Player = None
        self._playerClasse = classe
    
    def showWindow(self):
        super().showWindow()
        loop = asyncio.get_event_loop()
        self._map=Map()
        loop.run_until_complete(self._map.initMap())
        self._camera.position=(0.5,6,-15)
        self._map.spawnPlayer(eval(self._playerClasse))
        self._player = self._map.player
    
    def update(self):
        if not self._player.is_alive():
            Character.CAN_MOVE = False
            camera.z=-15
            self._player.disable()
        else:
            Character.CAN_MOVE = True
            self._camera.position = (self._player.x, self._player.y, -10)
            self._map.showMap()