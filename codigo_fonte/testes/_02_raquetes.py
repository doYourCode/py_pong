# Import the pygame library and initialise the game engine
import pygame
from codigo_fonte.utils.constantes import *


class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(COR_PRETO)
        self.image.set_colorkey(COR_PRETO)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()


def game_run():
    pygame.init()

    # Open a new window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    paddle_a = Paddle(COR_BRANCO, 10, 100)
    paddle_a.rect.x = 20
    paddle_a.rect.y = 200

    paddle_b = Paddle(COR_BRANCO, 10, 100)
    paddle_b.rect.x = 670
    paddle_b.rect.y = 200

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the paddles to the list of sprites
    all_sprites_list.add(paddle_a)
    all_sprites_list.add(paddle_b)

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carry_on = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while carry_on:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carry_on = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    carry_on = False

                    # --- Game logic should go here
        all_sprites_list.update()

        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(COR_PRETO)
        # Draw the net
        pygame.draw.line(screen, COR_BRANCO, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(60)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
