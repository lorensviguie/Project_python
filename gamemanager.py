from ursina import *
from Window.mainwindow import MainWindow
from Window.gamewindow import GameWindow
from Window.window import Window

class GameManager:

    def __init__(self, camera):
        self._mainWindow = MainWindow(camera)
        self._gameWindow = GameWindow(camera)
        self._winWindow = ""
        self._deadWindow = ""
        self._windows = [self._mainWindow, self._gameWindow]
        self._current_window = 0
    
    @property
    def mainWindow(self):
        return self._mainWindow
    
    @property
    def gameWindow(self):
        return self._gameWindow
    
    def update(self):
        if Window.CURRENT_WINDOW != self._current_window:
            if self._current_window == 0 and Window.CURRENT_WINDOW == 1:
                self._gameWindow._playerClasse = self._mainWindow.classe
            self._current_window = Window.CURRENT_WINDOW
            self._windows[self._current_window].showWindow()
        self._windows[self._current_window].update()
