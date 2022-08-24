# Import the pygame library and initialise the game engine
import pygame
from random import randint
from codigo_fonte.utils.constant import *


class Ball(pygame.sprite.Sprite):
    # This class represents a ball. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(4, 8), randint(-8, 8)]

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)


class Paddle(pygame.sprite.Sprite):
    # This class represents a paddle. It derives from the "Sprite" class in Pygame.

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Pass in the color of the Paddle, its width and height.
        # Set the background color and set it to be transparent
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        # Draw the paddle (a rectangle!)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

    def move_up(self, pixels):
        self.rect.y -= pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y < 0:
            self.rect.y = 0

    def move_down(self, pixels):
        self.rect.y += pixels
        # Check that you are not going too far (off the screen)
        if self.rect.y > 400:
            self.rect.y = 400


def game_run():
    pygame.init()

    # Open a new window
    size = (700, 500)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pong")

    paddle_a = Paddle(WHITE, 10, 100)
    paddle_a.rect.x = 20
    paddle_a.rect.y = 200

    paddle_b = Paddle(WHITE, 10, 100)
    paddle_b.rect.x = 670
    paddle_b.rect.y = 200

    ball = Ball(WHITE, 10, 10)
    ball.rect.x = 345
    ball.rect.y = 195

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    # Add the 2 paddles and the ball to the list of objects
    all_sprites_list.add(paddle_a)
    all_sprites_list.add(paddle_b)
    all_sprites_list.add(ball)

    # The loop will carry on until the user exits the game (e.g. clicks the close button).
    carry_on = True

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    # Initialise player scores
    score_a = 0
    score_b = 0

    # -------- Main Program Loop -----------
    while carry_on:
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carry_on = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:  # Pressing the x Key will quit the game
                    carry_on = False

        # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_a.move_up(5)
        if keys[pygame.K_s]:
            paddle_a.move_down(5)
        if keys[pygame.K_UP]:
            paddle_b.move_up(5)
        if keys[pygame.K_DOWN]:
            paddle_b.move_down(5)

            # --- Game logic should go here
        all_sprites_list.update()

        # Check if the ball is bouncing against any of the 4 walls:
        if ball.rect.x >= 690:
            score_a += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.x <= 0:
            score_b += 1
            ball.velocity[0] = -ball.velocity[0]
        if ball.rect.y > 490:
            ball.velocity[1] = -ball.velocity[1]
        if ball.rect.y < 0:
            ball.velocity[1] = -ball.velocity[1]

            # Detect collisions between the ball and the paddles
        if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
            ball.bounce()

        # --- Drawing code should go here
        # First, clear the screen to black.
        screen.fill(BLACK)
        # Draw the net
        pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        all_sprites_list.draw(screen)

        # Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(score_a), True, WHITE)
        screen.blit(text, (250, 10))
        text = font.render(str(score_b), True, WHITE)
        screen.blit(text, (420, 10))

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # --- Limit to 60 frames per second
        clock.tick(150)

    # Once we have exited the main program loop we can stop the game engine:
    pygame.quit()
