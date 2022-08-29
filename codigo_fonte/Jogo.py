import pygame
import time
from codigo_fonte.utils.constantes import *
from codigo_fonte.componentes.Bola import *
from codigo_fonte.componentes.IComponente import *


class Jogo:

    def __init__(self):
        pygame.init()
        self.componentes = []
        self.componentes.append(Bola(self, TELA_CENTRO_X - BALL_WIDTH / 2, TELA_CENTRO_Y - BALL_HEIGHT / 2,
                                     BALL_WIDTH, BALL_HEIGHT, COR_BRANCO))

        # This will be a list that will contain all the sprites we intend to use in our game.
        self.lista_sprites = pygame.sprite.Group()
        # The loop will carry on until the user exits the game (e.g. clicks the close button).
        self.jogo_ativo = True
        self.delta = 0.0
        # Cria uma nova janela
        self.screen = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
        pygame.display.set_caption("Pong")

    def carregar(self):
        for c in self.componentes:
            c.carregar()

    def desenhar(self):
        for c in self.componentes:
            c.desenhar()
        # --- Drawing code should go here
        # First, clear the screen to black.
        self.screen.fill(COR_PRETO)
        # Draw the net
        pygame.draw.line(self.screen, COR_BRANCO, [TELA_CENTRO_X, 0], [TELA_CENTRO_X, TELA_ALTURA], 16)

        # Now let's draw all the sprites in one go. (For now we only have 2 sprites!)
        self.lista_sprites.draw(self.screen)

        # Display scores:
        font = pygame.font.Font(None, 96)
        text = font.render(str("0"), True, COR_BRANCO)
        self.screen.blit(text, (TELA_E_TERCO - 48, 16))
        text = font.render(str("0"), True, COR_BRANCO)
        self.screen.blit(text, (TELA_D_TERCO, 16))

    def atualizar(self, delta):
        # --- Main event loop
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                self.jogo_ativo = False  # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Pressing the ESC Key will quit the game
                    self.jogo_ativo = False
        for c in self.componentes:
            c.atualizar(delta)
        # --- Game logic should go here
        #self.lista_sprites.update()

    def executar(self):

        for c in self.componentes:
            self.lista_sprites.add(c.sprite)

        # The clock will be used to control how fast the screen updates
        clock = pygame.time.Clock()

        # Initialise player scores
        score_a = 0
        score_b = 0

        last_time = time.time()

        # -------- Main Program Loop -----------
        while self.jogo_ativo:

            self.delta = time.time() - last_time
            self.delta *= 60
            last_time = time.time()

            self.atualizar(self.delta)

            # Moving the paddles when the use uses the arrow keys (player A) or "W/S" keys (player B)
            keys = pygame.key.get_pressed()
            #if keys[pygame.K_w]:
                #   paddle_a.move_up(5)
            #if keys[pygame.K_s]:
                #paddle_a.move_down(5)
            #if keys[pygame.K_UP]:
                #paddle_b.move_up(5)
            #if keys[pygame.K_DOWN]:
                #paddle_b.move_down(5)

                # Detect collisions between the ball and the paddles
            #if pygame.sprite.collide_mask(ball, paddle_a) or pygame.sprite.collide_mask(ball, paddle_b):
            #    ball.bounce()

            self.desenhar()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Once we have exited the main program loop we can stop the game engine:
        pygame.quit()
