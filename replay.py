from tabuleiro import Tabuleiro
import json

class Replay():
    def __init__(self):
        self.jogadas = []
        self.arquivo = "replay.json"
        
        self.carregarReplay()
    
    def adicionarJogada(self, rodada, jogador, alvo, coordenada, ocorrido ):
        self.jogadas.append((rodada, jogador, alvo, coordenada, ocorrido))
        
    def salvarReplay(self):
        with open(self.arquivo, "w", encoding= "utf8") as arquivo:
            json.dump(self.jogadas, arquivo, ensure_ascii=False, indent=4)
        
    def carregarReplay(self):
        try: 
            with open(self.arquivo, "r", encoding="utf-8") as arquivo:
                self.jogadas = json.load(arquivo)
                
        except FileNotFoundError:
            self.jogadas = []
            
    def exibirReplay(self):
        
        tabuleiro1 = Tabuleiro("~")
        tabuleiro2 = Tabuleiro("~")

        print("\nReplay da partida anterior:")

        for jogada in self.jogadas:

            rodada, jogador, alvo, coordenada, ocorrido = jogada

            if ocorrido == "Acertou":

                if alvo == "Jogador 1":
                    tabuleiro1.setSprite(
                        "H",
                        tabuleiro1.coordenada(coordenada)
                    )
                else:
                    tabuleiro2.setSprite(
                        "H",
                        tabuleiro2.coordenada(coordenada)
                    )

            elif ocorrido == "Errou":

                if alvo == "Jogador 1":
                    tabuleiro1.setSprite(
                        "X",
                        tabuleiro1.coordenada(coordenada)
                    )
                else:
                    tabuleiro2.setSprite(
                        "X",
                        tabuleiro2.coordenada(coordenada)
                    )

            print(
                f"\nRodada {rodada}:"
                f"\nJogador {jogador} atacou {alvo}"
                f" na coordenada {coordenada}"
                f"\nResultado: {ocorrido}"
            )

            print(f"\nTabuleiro de {alvo}:")

            if alvo == "Jogador 1":
                tabuleiro1.exibirTabuleiro()
            else:
                tabuleiro2.exibirTabuleiro()

            opcao = input(
                "\nPressione Enter para continuar "
                "ou 0 para sair do replay: "
            )

            if opcao == "0":
                break

        print("\nFim do replay.")

    def getJogadas(self):
        return self.jogadas
    
    def limparReplay(self):
        self.jogadas = []
        self.salvarReplay()
