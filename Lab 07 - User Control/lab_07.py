import arcade
from pyglet.event import EVENT_HANDLE_STATE
from background import setup_background, draw_background, draw_coche

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):


    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 User control")
        setup_background()
        self.coche_x = 250
        self.coche_y = 130
    def on_draw(self):
        self.clear()
        draw_background()
        draw_coche(self.coche_x, self.coche_y)
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.coche_x = x
        self.coche_y = y

def main():
    window = MyGame()
    arcade.run()
main()
