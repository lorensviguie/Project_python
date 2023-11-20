from ursina import *
from direct.actor.Actor import Actor

app = Ursina()

entity = Entity()
#animations are stored within the file
actor = Actor("filename.gltf")
actor.reparent_to(entity)

actor.loop("animation_name")  # use .play() instead of loop() to play it once.

app.run()
