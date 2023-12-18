from ursina import *
from Window.mainwindow import MainWindow
from Window.gamewindow import GameWindow
from Window.winWindow import VictoryWindow
from Window.deadwindow import DefeatWindow
from Window.window import Window

class GameManager:

    def __init__(self, camera):
        self._mainWindow = MainWindow(camera)
        self._gameWindow = GameWindow(camera)
        self._winWindow = VictoryWindow(camera)
        self._deadWindow = DefeatWindow(camera)
        self._windows = [self._mainWindow, self._gameWindow, self._deadWindow, self._winWindow]
        self._current_window = 0
        #self._music = Audio("Assets/musique_Tetris.mp3", loop=True)
    
    @property
    def mainWindow(self):
        return self._mainWindow
    
    @property
    def gameWindow(self):
        return self._gameWindow

    @property
    def victoryWindow(self):
        return self._winWindow
    
    @property
    def defeatWindow(self):
        return self._deadWindow
       
    def update(self):
        if Window.CURRENT_WINDOW != self._current_window:
            if self._current_window == 0 and Window.CURRENT_WINDOW == 1:
                self._gameWindow._playerClasse = self._mainWindow.classe
                
            self._windows[self._current_window].destroyWindow()
            self._current_window = Window.CURRENT_WINDOW
            self._windows[self._current_window].showWindow()
        self._windows[self._current_window].update()


