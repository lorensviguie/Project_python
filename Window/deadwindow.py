from ursina import *
from Window.window import Window

class DefeatWindow(Window):
    def __init__(self, camera, cameraPosition=(-10,-10)):
        super().__init__(camera=camera, cameraPosition=cameraPosition)

    def createWindow(self):
        self.text = Text(text="DEFEAT!", scale=4, origin=(0, -3))
        self.retry_button = Button(text='Retry', color=color.red, scale=(0.2, 0.1), origin=(0, 2.5), on_click=self.on_retry_click,
                                   highlight_color=color.white)

    def on_retry_click(self):
        if Window.CURRENT_WINDOW != 2: return
        self.destroy_window()
        Window.CURRENT_WINDOW = 0  

    def destroy_window(self):
        destroy(self.text)
        destroy(self.retry_button)
