from enum import Enum
import slangpy as spy
from pathlib import Path

class RenderingType(Enum):
    FORWARD = 0
    DEFERRED = 1


class IScene:
    def __init__(self):
        pass

    def init(
            self, 
            device : spy.Device, 
            shaders_path : Path
        ):
        self._init(
            device, 
            shaders_path
        )

    def update(self):
        self._update()

    def render(self):
        self._render()

    def shutdown(self):
        self._shutdown()