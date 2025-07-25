from random import choice

from data import dica, lista_palavras


class Jogador:
    def __init__(self):
        self.pts_totais = 0
        self.pts = 0
        self.chances = 5
        self.ale_dica = ''
        self.ale_palavra = ''
        self.oculto = []
        self.noticia = ' '

    def nova_palavra(self):
        self.pts = 0
        self.chances = 5
        self.oculto = []
        self.ale_dica = choice(dica)
        self.ale_palavra = choice(lista_palavras[dica.index(self.ale_dica)])
        for l in range(len(self.ale_palavra)):
            self.oculto.append('_')