# TODO abstrair a função main para um objeto Game, responsável pela execução do código, o objetivo é legibilidade
from codigo_fonte.Jogo import *


if __name__ == '__main__':
    jogo = Jogo()
    jogo.executar()
