import arcade

# Abrir una ventana
arcade.open_window(600, 600, "Ventana de prueba")

# Establecer el color de fondo
arcade.set_background_color(arcade.color.WHITE)

# Función que se llama para dibujar en la pantalla
def on_draw():
    arcade.start_render()
    arcade.draw_text("¡Hola, Arcade!", 200, 300, arcade.color.BLACK, 24)

# Asignar la función `on_draw` al evento de dibujo
arcade.set_draw_function(on_draw)

# Ejecutar el juego
arcade.run()
