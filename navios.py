class Navio():
    def __init__(self, coordenada, tipo, orientacao):
        coordenada = coordenada.strip()

        if len(coordenada) < 2:
            raise ValueError("Coordenada inválida. Use o formato letra + número (ex: A1)")

        x = ord(coordenada[0].upper()) - ord('A') + 1

        try:
            y = int(coordenada[1:])
        except ValueError:
            raise ValueError("Coordenada inválida. Use o formato letra + número (ex: A1)")

        if x > 10 or x < 1:
            raise ValueError("A letra da coluna deve estar entre A e J")

        if y > 10 or y < 1:
            raise ValueError("O número da linha deve estar entre 1 e 10")

        if tipo.lower() == 'porta-aviões':
            self.tamanho = 4

        elif tipo.lower() == 'encouraçado':
            self.tamanho = 2

        else:
            raise ValueError("Tipo de navio inválido. Escolha entre 'Porta-Aviões' ou 'Encouraçado'.")

        self.orientacao = orientacao.lower().strip()
        self.posX = x
        self.posY = y
        self.tipo = tipo
        self.posicoes = self.definirPosicoes()

    def definirPosicoes(self):
        direcoes = {
            "direita": (1, 0),
            "esquerda": (-1, 0),
            "baixo": (0, 1),
            "cima": (0, -1)
        }

        if self.orientacao.lower().strip() not in direcoes:
            raise ValueError("Orientação inválida")

        dx, dy = direcoes[self.orientacao.lower().strip()]

        posicoes = []

        for i in range(self.tamanho):
            x = self.posX + (dx * i)
            y = self.posY + (dy * i)

            if x < 1 or x > 10 or y < 1 or y > 10:
                raise ValueError("O navio ultrapassa o limite do tabuleiro")

            posicoes.append([x, y])

        return posicoes

    def getTamanho(self):
        return self.tamanho
    
    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getTipo(self):
        return self.tipo

    def getOrientacao(self):
        return self.orientacao

    def getPosicoes(self):
        return self.posicoes


    

