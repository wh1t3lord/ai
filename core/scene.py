from enum import Enum


class RenderingType(Enum):
    FORWARD = 0
    DEFERRED = 1


class IScene:
    def __init__(self):
        pass

    def init(self, )