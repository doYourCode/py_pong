import pygame
from codigo_fonte.componentes.IComponente import *
from codigo_fonte.utils.constantes import *
from random import randint


class Bola(IComponente):

    def __init__(self, jogo, x, y, width, height, color):
        super().__init__(jogo, x, y)
        # Component's' sprite
        self.sprite = pygame.sprite.Sprite()
        # Pass in the color of the ball, its width and height.
        # Set the background color and set it to be transparent
        self.sprite.image = pygame.Surface([width, height])
        self.sprite.image.fill(COR_PRETO)
        self.sprite.image.set_colorkey(COR_PRETO)
        # Draw the ball (a rectangle!)
        pygame.draw.rect(self.sprite.image, color, [0, 0, width, height])
        # Fetch the rectangle object that has the dimensions of the image.
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y
        # Set random velocity
        self.velocity = pygame.Vector2(randint(4, 8), randint(-8, 8))

    def carregar(self):
        pass

    def desenhar(self):
        pass

    def atualizar(self, delta):
        self.sprite.rect.x += self.velocity.x * delta
        self.sprite.rect.y += self.velocity.y * delta
        self.velocity = self.velocity.normalize() * 6

        self._verificar_bordas()

    def _quicar(self):
        self.velocity.x = -self.velocity[0]
        self.velocity.y = randint(-8, 8)

    def _reiniciar(self):
        self.sprite.rect.x = TELA_CENTRO_X - (BALL_WIDTH / 2)
        self.sprite.rect.y = TELA_CENTRO_Y - (BALL_HEIGHT / 2)
        # self.velocity = pygame.Vector2(randint(4, 8), randint(-8, 8))

    def _verificar_bordas(self):
        # Check if the ball is bouncing against any of the 4 walls:
        if self.sprite.rect.x > TELA_MARGEM_DIREITA:
            self.velocity[0] = -self.velocity[0]
            # score_a += 1
            self._reiniciar()
        if self.sprite.rect.x < TELA_MARGEM_ESQUERDA:
            self.velocity[0] = -self.velocity[0]
            # score_b += 1
            self._reiniciar()
        if self.sprite.rect.y > TELA_MARGEM_INFERIOR:
            self.sprite.rect.y = TELA_MARGEM_INFERIOR - 1
            self.velocity[1] = -self.velocity[1]
        if self.sprite.rect.y < TELA_MARGEM_SUPERIOR:
            self.sprite.rect.y = TELA_MARGEM_SUPERIOR + 1
            self.velocity[1] = -self.velocity[1]
