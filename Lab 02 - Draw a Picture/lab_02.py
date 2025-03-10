# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Coche en la carretera")

# Color de fondo
gris_claro = (194,194,194)
arcade.set_background_color(arcade.color.SKY_BLUE)

# Listo para dibujar
arcade.start_render()

# Carretera con linea
arcade.draw_lrbt_rectangle_filled(0,800,0,200,arcade.color.GRAY)
for i in range(50, 800, 100):
    arcade.draw_lrbt_rectangle_filled(i,i+40,95,105,arcade.color.YELLOW)

# Carroceria del coche
arcade.draw_lrbt_rectangle_filled(250,380,130,250,arcade.color.RED)
arcade.draw_lrbt_rectangle_filled(210,470,130,190,arcade.color.RED)
arcade.draw_triangle_filled(250,250,220,190,250,190,arcade.color.RED)
arcade.draw_triangle_filled(380,250,440,190,380,190,arcade.color.RED)

# Ventanas
arcade.draw_triangle_filled(250,245,225,190,250,190,arcade.color.LIGHT_BLUE)
arcade.draw_triangle_filled(380,245,435,190,380,190,arcade.color.LIGHT_BLUE)
arcade.draw_lrbt_rectangle_filled(340,380,190,245,arcade.color.LIGHT_BLUE)
arcade.draw_lrbt_rectangle_filled(255,335,190,245,arcade.color.LIGHT_BLUE)

# Ruedas
arcade.draw_circle_filled(250,130,25,arcade.color.BLACK)
arcade.draw_circle_filled(430,130,25,arcade.color.BLACK)


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

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()























# Keep the window up until someone closes it.
arcade.run()