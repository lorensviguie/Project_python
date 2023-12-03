from ursina import *

class Window:

    CURRENT_WINDOW = 0

    def __init__(self, camera, cameraPosition=(0,0)):
        self._camera = camera
        self._cameraPosition = cameraPosition
    
    def showWindow(self):
        self._camera.x, self._camera.y = self._cameraPosition
        self.createWindow()
    
    def update(self):
        pass
    
    def destroyWindow(self):
        pass

    def createWindow(self):
        pass