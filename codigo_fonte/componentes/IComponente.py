import pygame
import abc


class IComponente(metaclass=abc.ABCMeta):

    def __init__(self, jogo, x, y):
        self.posicao = pygame.Vector2(x, y)
        self.jogo = jogo
        self.jogo.componentes.append(self)

    @abc.abstractmethod
    def carregar(self):
        pass

    @abc.abstractmethod
    def desenhar(self):
        pass

    @abc.abstractmethod
    def atualizar(self, delta):
        pass
