# Import the "arcade" library
import arcade


def setup_background():
    # Color de fondo
    arcade.set_background_color(arcade.color.LIGHT_BLUE)

def draw_background():
    # Carretera con linea
    arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.GRAY)
    for i in range(50, 800, 100):
        arcade.draw_lrbt_rectangle_filled(i, i + 40, 95, 105, arcade.color.YELLOW)

    # Palmera 1
    # Tronco de la palmera
    arcade.draw_lrbt_rectangle_filled(185, 215, 200, 450, arcade.color.BROWN)

    # Hojas de la palmera (usamos varias elipses para las hojas)
    arcade.draw_ellipse_filled(200 - 40, 400 + 30, 80, 30, arcade.color.ARCADE_GREEN)
    arcade.draw_ellipse_filled(200 + 40, 400 + 30, 80, 30, arcade.color.BUD_GREEN)
    arcade.draw_ellipse_filled(200 - 30, 400 + 50, 70, 30, arcade.color.ANDROID_GREEN)
    arcade.draw_ellipse_filled(200 + 30, 400 + 50, 70, 30, arcade.color.DARK_GREEN)

    # Palmera 2
    # Tronco de la palmera
    arcade.draw_lrbt_rectangle_filled(585, 615, 200, 450, arcade.color.BROWN)

    # Hojas de la palmera (usamos varias elipses para las hojas)
    arcade.draw_ellipse_filled(600 - 40, 400 + 30, 80, 30, arcade.color.ARCADE_GREEN)
    arcade.draw_ellipse_filled(600 + 40, 400 + 30, 80, 30, arcade.color.BUD_GREEN)
    arcade.draw_ellipse_filled(600 - 30, 400 + 50, 70, 30, arcade.color.ANDROID_GREEN)
    arcade.draw_ellipse_filled(600 + 30, 400 + 50, 70, 30, arcade.color.DARK_GREEN)


def draw_coche(x, y):
    # Desfase horizontal y vertical según la posición base x, y

    # Carrocería del coche
    arcade.draw_lrbt_rectangle_filled(x, x + 130, y, y + 120, arcade.color.RED)
    arcade.draw_lrbt_rectangle_filled(x - 40, x + 220, y, y + 60, arcade.color.RED)
    arcade.draw_triangle_filled(x, y + 120, x - 30, y + 60, x, y + 60, arcade.color.RED)
    arcade.draw_triangle_filled(x + 130, y + 120, x + 190, y + 60, x + 130, y + 60, arcade.color.RED)

    # Ventanas
    arcade.draw_triangle_filled(x, y + 115, x - 25, y + 60, x, y + 60, arcade.color.LIGHT_BLUE)
    arcade.draw_triangle_filled(x + 130, y + 115, x + 185, y + 60, x + 130, y + 60, arcade.color.LIGHT_BLUE)
    arcade.draw_lrbt_rectangle_filled(x + 90, x + 130, y + 60, y + 115, arcade.color.LIGHT_BLUE)
    arcade.draw_lrbt_rectangle_filled(x + 5, x + 85, y + 60, y + 115, arcade.color.LIGHT_BLUE)

    # Ruedas
    arcade.draw_circle_filled(x, y, 25, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 180, y, 25, arcade.color.BLACK)


# Open up a window.
arcade.open_window(800, 600, "Coche en la carretera")
setup_background()
arcade.start_render()
draw_background()
draw_coche(100, 100)
# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()























# Keep the window up until someone closes it.
arcade.run()