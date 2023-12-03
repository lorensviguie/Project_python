from ursina import *
from Window.window import Window

class VictoryWindow(Window):
    def __init__(self, camera, cameraPosition=(-10,-10)):
        super().__init__(camera=camera, cameraPosition=cameraPosition)

    def createWindow(self):
        self.text = Text(text="VICTORY!", scale=4, origin=(0, -3))
        self.play_again_button = Button(text='Play Again', color=color.green, scale=(0.2, 0.1), origin=(0, 2.5), on_click=self.on_play_again_click,
                                        highlight_color=color.white)

    def on_play_again_click(self):
        if Window.CURRENT_WINDOW != 3: return
        self.destroy_window()
        Window.CURRENT_WINDOW = 0

    def destroy_window(self):
        destroy(self.text)
        destroy(self.play_again_button)
