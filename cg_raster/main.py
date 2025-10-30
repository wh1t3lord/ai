import slangpy as spy
from pathlib import Path
import scenes


DIR_ROOT = Path(__file__).parent.parent
DIR_DATA = DIR_ROOT / 'data'
DIR_DATA_SHADERS = DIR_DATA / 'shaders'

class App:
    def __init__(self):
        self.current_scene : scenes.IScene = None

        self.__register_scenes()
        self.__init()


        self.set_current_scene("empty")

    def __register_scenes(self):
        self.scenes = {
            "triangle": scenes.SceneRasterTriangle(),
            "empty": scenes.SceneRasterEmpty()
        }

    def __window_callback_resize(
            self,
            width : int,
            height : int
    ):
        if self.current_scene:
            if self.window:
                self.current_scene.on_resize(width,height)

    def __window_callback_mouse_event(
            self,
            event : spy.MouseEvent
    ):
        if self.ui:
            if self.ui.handle_mouse_event(event):
                return

        if self.current_scene:
            if self.window:
                self.current_scene.on_mouse_event(event)

    def __window_callback_keyboard_event(
            self,
            event : spy.KeyboardEvent
    ):
        if self.ui:
            if self.ui.handle_keyboard_event(event):
                return

        if self.current_scene:
            if self.window:
                self.current_scene.on_keyboard_event(event)

    def __init(self):
        self.window = spy.Window(
            width=640,
            height=480,
            title="",
            resizable=True
        )

        if self.window:
            self.window.on_resize = self.__window_callback_resize
            self.window.on_mouse_event = self.__window_callback_mouse_event
            self.window.on_keyboard_event = self.__window_callback_keyboard_event

        self.device = spy.Device(
            enable_debug_layers=True,
            type=spy.DeviceType.vulkan,
        )

        self.ui = None
        if self.device:
            self.ui = spy.ui.Context(self.device)

            if self.ui:
                self.ui_window = spy.ui.Window(self.ui.screen, "Scenes", size=spy.float2(self.window.width*0.25, self.window.height*0.25))
                self.ui_window_text_current_scene_name = spy.ui.Text(self.ui_window, '')

    def set_current_scene(self, scene_name : str):
        if not scene_name:
            return
        
        if len(scene_name)==0:
            return
        
        if scene_name in self.scenes:
            if self.current_scene:
                self.current_scene.shutdown()

            self.current_scene = self.scenes[scene_name]
            self.current_scene.init(
                self.device, 
                self.window,
                self.ui,
                DIR_DATA_SHADERS
            )

            if self.ui_window_text_current_scene_name:
                self.ui_window_text_current_scene_name.text = f'current scene: {self.__class__.__name__}'

    def update(self):
        if self.current_scene == None:
            return
        
        while not self.window.should_close():
            self.window.process_events()
            self.current_scene.update()
            self.current_scene.render()

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
    
    if not DIR_DATA_SHADERS.exists():
        raise 'failed to determine data/shaders path'


    app = App()
    app.update()
    app.shutdown()