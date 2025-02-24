# Import the "arcade" library
import arcade

# Open up a window.
arcade.open_window(800, 600, "Villa oculta de la hoja")

# Color de fondo
gris_claro = (194,194,194)
arcade.set_background_color(gris_claro)

# Listo para dibujar
arcade.start_render()

# Comenzamos con la hoja

# Dibujar la espiral
arcade.draw_arc_outline(300, 300, 200, 200, arcade.color.BLACK, 0, 270, 10)
arcade.draw_arc_outline(300, 300, 150, 150, arcade.color.BLACK, 0, 270, 10)
arcade.draw_arc_outline(300, 300, 100, 100, arcade.color.BLACK, 0, 270, 10)
arcade.draw_arc_outline(300, 300, 50, 50, arcade.color.BLACK, 0, 270, 10)

# Dibujar el triángulo inferior
arcade.draw_triangle_filled(180, 200, 280, 200, 230, 120, arcade.color.BLACK)

# Dibujar las líneas inclinadas
arcade.draw_line(400, 400, 460, 460, arcade.color.BLACK, 10)
arcade.draw_line(190, 290, 250, 350, arcade.color.BLACK, 10)

# Dibujar el círculo exterior
arcade.draw_circle_outline(300, 300, 220, arcade.color.BLACK, 10)

# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()























# Keep the window up until someone closes it.
arcade.run()