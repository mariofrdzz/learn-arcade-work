
import arcade

SPRITE_SCALING_NATHAN = 0.05
SPRITE_SCALING_REBOTE = 0.2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

REBOTE_SPEED = 5
NATHAN_SPEED = 5

class Rebote(arcade.Sprite):

    def __init__(self, x, y):
        super().__init__("rebote.png", SPRITE_SCALING_REBOTE)
        self.center_x = x
        self.center_y = y
        self.change_y = 0

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class Nathan(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.top < 0:
            self.bottom = SCREEN_HEIGHT

class MyGame(arcade.Window):

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Nathan pobreton")

        # Variables that will hold sprite lists.
        self.player_list = None
        self.coin_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BABY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from kenney.nl
        self.player_sprite = arcade.Sprite("nathan.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            # Create the coin instance
            coin = Coin("coin.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # Add the coin to the lists
            self.coin_list.append(coin)

    def on_draw(self):
        self.clear()
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.coin_list) == 0:
            output = f"NATHAN DEJÓ LA POBREZA"
            arcade.draw_text(output, 10, SCREEN_HEIGHT/2, arcade.color.WHITE, 52)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        for coin in self.coin_list:
            coin.update()

        # Generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()