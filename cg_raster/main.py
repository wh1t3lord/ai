import slangpy as spy
from pathlib import Path

DIR_ROOT = Path(__file__).parent.parent
DIR_DATA = DIR_ROOT / 'data'

g_app_close = False

class App:
    def __init__(self):
        self.current_scene = None

        self.__init_register_scenes()

    def __init_register_scenes(self):
        pass

    def set_current_scene(self, scene_name : str):
        pass

    def update(self):
        if self.current_scene == None:
            return

    def render(self):
        if self.current_scene == None:
            return

    def shutdown(self):
        if self.current_scene == None:
            return



if __name__ == "__main__":
    print(f'root dir: {DIR_ROOT}')
    print(f'data dir: {DIR_DATA}')

    if not DIR_ROOT.exists():
        raise "failed to determine root path"

    if not DIR_DATA.exists():
        raise "failed to determine data path"


    app = App()

    app.shutdown()