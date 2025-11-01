import core

import slangpy as spy
from pathlib import Path

class SceneRasterTriangle(core.IScene):
    def __init__(self):
        pass

    def _init(
            self,
            device : spy.Device, 
            window : spy.Window,
            ui : spy.ui.Context,
            shaders_path : Path
        ):
        print(f'{self.__class__.__name__}: init called')

        self.device = device

        if self.device:
            
            shader_name = shaders_path / 'raster_triangle' / 'shader.slang'
            self.program = self.device.load_program(str(shader_name), ['mainVertex', 'mainPixel'])
            input_layout = self.device.create_input_layout(
                input_elements=[
                    {
                        "semantic_name": "POSITION",
                        "semantic_index": 0,
                        "format": spy.Format.rg32_float,
                    }
                ],
                vertex_streams=[{"stride": 8}],
            )

            self.pipeline = self.device.create_render_pipeline(
                program=self.program,
                input_layout=input_layout,
                targets=[{"format": spy.Format.rgba32_float}]
            )
            

            if window:
                self.swapchain = self.device.create_surface(window)
                self.swapchain.configure(width=window.width,height=window.height)

                self.ui = ui



    def _update(
            self
        ):
        if self.device and self.swapchain:
            command_encoder : spy.CommandEncoder = self.device.create_command_encoder()
            texture_surface : spy.Texture = self.swapchain.acquire_next_image()

            if not texture_surface:
                return
            
            command_encoder.clear_texture_float(texture_surface, clear_value=[0,1,0,1])

            if self.ui:
                self.ui.new_frame(width=texture_surface.width, height=texture_surface.height)
                self.ui.render(texture=texture_surface, command_encoder=command_encoder)

            self.device.submit_command_buffer(command_encoder.finish())
            del texture_surface

            self.swapchain.present()

    def _render(
            self
        ):
        pass

    def _shutdown(
            self
        ):
       if self.device:
           self.device.wait()
           self.swapchain.unconfigure()
           del self.swapchain

    def _on_resize(
            self,
            width : int,
            height : int
        ):
        if self.device:
            self.device.wait()

        if width > 0 and height > 0:
            self.swapchain.configure(width=width,height=height)
        else:
            self.swapchain.unconfigure()

    def _on_mouse_event(
            self,
            event : spy.MouseEvent
        ):
        pass

    def _on_keyboard_event(
            self,
            event : spy.KeyboardEvent
    ):
        pass