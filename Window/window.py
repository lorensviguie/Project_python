from ursina import *

class Window:

    CURRENT_WINDOW = 0

    def __init__(self, camera, cameraPosition=(0,0)):
        self._camera = camera
        self._cameraPosition = cameraPosition
    
    def showWindow(self):
        self._camera.x, self._camera.y = self._cameraPosition
    
    def update(self):
        pass