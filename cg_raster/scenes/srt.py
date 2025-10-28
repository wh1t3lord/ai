import core

import slangpy as spy
from pathlib import Path

class SceneRasterTriangle(core.IScene):
    def __init__(self):
        pass

    def _init(
            self,
            device : spy.Device, 
            shaders_path : Path
        ):
        print(f'{self.__class__.__name__}: init called')

        self.device = device

    def _update(
            self
        ):
        pass

    def _render(
            self
        ):
        pass

    def _shutdown(
            self
        ):
       print(f'{self.__class__.__name__}: shutdown called')