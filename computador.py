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
        
        
        self.ultimoAcerto = None
        self.direcao = None

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
    
    def obterDirecao(self, origem, destino):

        x1, y1 = origem
        x2, y2 = destino

        if x2 > x1:
            return "direita"

        if x2 < x1:
            return "esquerda"

        if y2 > y1:
            return "baixo"

        if y2 < y1:
            return "cima"

        return None
    
    def obterProximaPosicao(self, coordenada, direcao):

        x, y = coordenada

        movimentos = {
            "direita": (1, 0),
            "esquerda": (-1, 0),
            "baixo": (0, 1),
            "cima": (0, -1)
        }

        dx, dy = movimentos[direcao]

        novaPosicao = (x + dx, y + dy)

        if 1 <= novaPosicao[0] <= 10 and 1 <= novaPosicao[1] <= 10:
            return novaPosicao

        return None

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

        if self.ultimoAcerto is not None and self.direcao is not None:

            proxima = self.obterProximaPosicao(
                self.ultimoAcerto,
                self.direcao
            )

            if (
                proxima is not None
                and proxima not in self.coordenadasAtacadas
            ):
                return proxima

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
    
    def adicionarAlvos(self, coordenada):

        for vizinha in self.obterVizinhas(coordenada):

            if vizinha not in self.coordenadasAtacadas:
                if vizinha not in self.alvos:
                    self.alvos.append(vizinha)
                    
    def atacar(self, jogador):

        coordenada = self.gerarCoordenada()

        self.coordenadasAtacadas.add(coordenada)

        coordenadaTxt = self.converterCoordenada(coordenada)

        sprite = jogador.tabuleiro.getSprite(coordenadaTxt)

    
        if sprite == '~':

            jogador.tabuleiro.setSprite(
                "X",
                list(coordenada)
            )

    
            self.direcao = None
            self.ultimoAcerto = None

            return coordenadaTxt, False

        else:

            jogador.tabuleiro.setSprite(
                "H",
                list(coordenada)
            )

            jogador.diminuirVida()

        
            if self.ultimoAcerto is not None:

                self.direcao = self.obterDirecao(
                    self.ultimoAcerto,
                    coordenada
                )

            self.ultimoAcerto = coordenada

            self.adicionarAlvos(coordenada)

            return coordenadaTxt, True
    
    def posicionarNavios(self):

        tipos = [
            ("Encouraçado", 2),
            ("Porta-Aviões", 2)
        ]
        
        orientacoes = [
            "direita",
            "esquerda",
            "cima",
            "baixo"
        ]

        for tipo, quantidade in tipos:
            for i in range(quantidade):
                while True:

                    try:
                        x = random.randint(1, 10)
                        y = random.randint(1, 10)

                        letra = chr(ord("A") + x - 1)
                        coordenada = letra + str(y)


                        orientacao = random.choice(orientacoes)

                        navio = Navio(coordenada, tipo, orientacao)
                        self.adicionarNavio(navio)
                        break

                    except ValueError:
                        pass
        



    
