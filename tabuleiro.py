class Tabuleiro():
    def __init__(self, sprite):
        self.tamX = 10
        self.tamY = 10
        self.sprite = sprite

        self.tabuleiro = [
            [sprite for x in range(self.tamX)]
            for y in range(self.tamY)
        ]

    def coordenada(self, coordenada):
        x = ord(coordenada[0].upper()) - ord('A') + 1#No ord, A vale 0, entao o + 1 converte ele num valor acima
        y = int(coordenada[1:])

        if x < 1 or x > 10:
            raise ValueError("A linha deve estar entre A e J")

        if y < 1 or y > 10:
            raise ValueError("A coluna deve estar entre 1 e 10")

        return [x, y]

    def getSprite(self, posicao):
        x, y = self.coordenada(posicao)
        
        return self.tabuleiro[y - 1][x - 1]
    #sprites de mar, sprite de missed, sprite de destruir navio

    def setSprite(self, novoSprite, posicao):
        x, y = posicao

        self.tabuleiro[y - 1][x - 1] = novoSprite
    #modificar o sprite em base na coordenada que o usuario escolher

    def verificarPosicao(self, posicoes):
        for pos in posicoes:
            x, y = pos
            
            if self.tabuleiro[y - 1][x - 1] != self.sprite:
                return False
            
        return True
    

    def exibirTabuleiro(self):
        print("     A B C D E F G H I J")

        for y in range(self.tamY):
            print(f"{y + 1:2}   " + " ".join(self.tabuleiro[y]))
            
    def exibirTabuleiroAtaque(self):
        print("     A B C D E F G H I J")

        for y in range(self.tamY):
            linha = []

            for x in range(self.tamX):
                sprite = self.tabuleiro[y][x]
                
                if sprite == "P" or sprite == "E":
                    sprite = "~"

                linha.append(sprite)
                
            print(f"{y + 1:2}   " + " ".join(linha))


