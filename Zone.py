from ursina import *
from character import Character

class Zone(Entity):
    def __init__(self, name="zone", texture='Assets/sol.png', position=(0,0), enabled=False, scale=(1/2,1/2)):
        super().__init__(name=name, scale=scale, collider='box', enabled=enabled, model='quad', texture=texture, position=position)
        self._is_spawn = True
    
    @property
    def is_spawn(self):
        return self._is_spawn

class Sol(Zone):
    def __init__(self, position=(0,0), texture='Assets/sol.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)
        
class SolVolant(Zone):
    def __init__(self, position=(0,0), texture='Assets/sol.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)

class Mur(Zone):
    def __init__(self, position=(0,0), texture='Assets/mur.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)

class MurPlein(Zone):
    def __init__(self, position=(0,0), texture='Assets/murplein.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)

class MurCassable(Zone):
    def __init__(self, name="cassable", position=(0,0), texture='Assets/soldestructible.png', enabled=False):
        super().__init__(name=name,position=position, texture=texture, enabled=enabled)
        self._health = 2
    
    def decrease_health(self):
        self._health -= 1
        if self._health == 0:
            self.disable()
            self._is_spawn = False

class Heal(Zone):
    def __init__(self, position=(0,0), texture='Assets/health.png', enabled=False, scale=(1/4,1/4)):
        super().__init__(position=position, texture=texture, enabled=enabled, scale=scale)
    
    def update(self):
        for entity in self.intersects().entities:
            if entity.name == "player":
                entity:Character
                entity.heal(entity.max_health/4)
                self._is_spawn = False
                self.disable()
                return

class Activable(Zone):
    def __init__(self, position=(0,0), texture='Assets/activablesol.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)

class End(Zone):
    def __init__(self, position=(0,0), texture='Assets/end.png', enabled=False):
        super().__init__(position=position, texture=texture, enabled=enabled)