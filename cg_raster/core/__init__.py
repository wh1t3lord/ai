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
            window : spy.Window,
            shaders_path : Path
        ):
        self._init(
            device, 
            window,
            shaders_path
        )

    def update(self):
        self._update()

    def render(self):
        self._render()

    def shutdown(self):
        self._shutdown()

    def on_resize(
            self, 
            width : int, 
            height : int
        ):
        self._on_resize(width,height)

    def on_mouse_event(
            self,
            event : spy.MouseEvent
        ):
        self._on_mouse_event(event)

    def on_keyboard_event(
            self,
            event : spy.KeyboardEvent
        ):
        self._on_keyboard_event(event)