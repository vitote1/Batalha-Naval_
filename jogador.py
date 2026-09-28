
from tabuleiro import Tabuleiro

class Jogador():

    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.tabuleiro = Tabuleiro("~")
        self.navios = []

    def getNome(self):
        return self.nome
    
    def getVida(self):
        return self.vida

    def getNavios(self):
        return self.navios

    def setNome(self, novoNome):
        self.nome = novoNome

    def diminuirVida(self):
        self.vida -= 1

    def verificarEstaVivo(self):
        return self.vida > 0

    def adicionarNavio(self, navio):
        if not self.tabuleiro.verificarPosicao(navio.getPosicoes()):
            raise ValueError("O navio não pode ser colocado nessa posição")
        
        if navio.getTipo().lower() == "porta-aviões":
            sprite = "P"
        elif navio.getTipo().lower() == "encouraçado":
            sprite = "E"
        else:
            raise ValueError("Tipo de navio inválido. Escolha entre 'Porta-Aviões' ou 'Encouraçado'.")

        for posicao in navio.getPosicoes():
            self.tabuleiro.setSprite(sprite, posicao)
        self.navios.append(navio)



    
