
from tabuleiro import Tabuleiro
import random
from navios import Navio

class Computador():

    def __init__(self, vida):
        self.nome = "Computador"
        self.vida = vida
        self.tabuleiro = Tabuleiro("~")
        self.navios = []
        
        self.coordenadasAtacadas = set()
        self.alvos = []

    def getNome(self):
        return self.nome
    
    def getVida(self):
        return self.vida

    def getNavios(self):
        return self.navios

    def diminuirVida(self):
        self.vida -= 1

    def verificarEstaVivo(self):
        return self.vida > 0

    def adicionarNavio(self, navio):
        if not self.tabuleiro.verificarPosicao(navio.getPosicoes()):
            raise ValueError("O navio não pode ser colocado nessa posição.")

        if navio.getTipo().lower() == "porta-aviões":
            sprite = "P"
        elif navio.getTipo().lower() == "encouraçado":
            sprite = "E"
        else:
            raise ValueError("Tipo de navio inválido. Escolha entre 'Porta-Aviões' ou 'Encouraçado'.")

        for posicao in navio.getPosicoes():
            self.tabuleiro.setSprite(sprite, posicao)
        self.navios.append(navio)
        
    def gerarCoordenada(self):
        while self.alvos:
            
            coordenada = self.alvos.pop(0)
            
            if coordenada not in self.coordenadasAtacadas:
                return coordenada

        while True:
            x = random.randint(1, 10)
            y = random.randint(1, 10)

            coordenada = (x, y)

            if coordenada not in self.coordenadasAtacadas:
                return coordenada

    def converterCoordenada(self, coordenada):
        x, y = coordenada
        letra = chr(ord("A") + x - 1)

        return letra + str(y)
        
    def obterVizinhas(self, coordenada):
        x, y = coordenada
        
        vizinhas = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        
        return [
            posicao 
            for posicao in vizinhas
            if 1 <= posicao[0] <= 10 and 1 <= posicao[1] <= 10
        ]
        
    def atacar(self, jogador):
        
        coordenada = self.gerarCoordenada()
        self.coordenadasAtacadas.add(coordenada)
        coordenadaTxt = self.converterCoordenada(coordenada)
        sprite = jogador.tabuleiro.getSprite(coordenadaTxt)
        
        if sprite == '~':
            jogador.tabuleiro.setSprite("X", list(coordenada))
            
            return coordenadaTxt, False
        else:
            jogador.tabuleiro.setSprite("H", list(coordenada))
            jogador.diminuirVida()
            
            self.alvos.extend(self.obterVizinhas(coordenada))
            
            return coordenadaTxt, True
    
    def posicionarNavios(self):

        tipos = [
            ("Encouraçado", 2),
            ("Porta-Aviões", 2)
        ]

        for tipo, quantidade in tipos:
            for i in range(quantidade):
                while True:

                    try:
                        x = random.randint(1, 10)
                        y = random.randint(1, 10)

                        letra = chr(ord("A") + x - 1)
                        coordenada = letra + str(y)

                        orientacoes = [
                            "direita",
                            "esquerda",
                            "cima",
                            "baixo"
                        ]

                        orientacao = random.choice(orientacoes)

                        navio = Navio(coordenada, tipo, orientacao)
                        self.adicionarNavio(navio)
                        break

                    except ValueError:
                        pass
        



    
