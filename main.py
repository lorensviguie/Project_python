from ursina import *
from direct.actor.Actor import Actor
import map

app = Ursina()

map.initMap()
camera.position = (5, 5, -20)

app.run()
