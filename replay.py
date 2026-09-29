from tabuleiro import Tabuleiro
import json
from pathlib import Path
import os

class Replay():
    def __init__(self):
        self.jogadas = []
        self.arquivo = Path("data") / "replay.json"
        
        os.makedirs("data", exist_ok=True)
        
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
        
        if not self.jogadas:
            print("\nNão houve nenhuma partida!")
            return 0
            
        tabuleiros = {}  

        print("\nReplay da partida anterior:")

        for rodada, jogador, alvo, coordenada, ocorrido in self.jogadas:
            if alvo not in tabuleiros:
                tabuleiros[alvo] = Tabuleiro("~")

            tabuleiro = tabuleiros[alvo]
            sprite = "H" if ocorrido == "Acertou" else "X"
            tabuleiro.setSprite(sprite, tabuleiro.coordenada(coordenada))

            print(
                f"\nRodada {rodada}:"
                f"\n{jogador} atacou {alvo} na coordenada {coordenada}"
                f"\nResultado: {ocorrido}"
            )
            print(f"\nTabuleiro de {alvo}:")
            tabuleiro.exibirTabuleiro()

            if input("\nPressione Enter para continuar ou 0 para sair do replay: ") == "0":
                break

        print("\nFim do replay.")

    def getJogadas(self):
        return self.jogadas
    
    def limparReplay(self):
        self.jogadas = []
        self.salvarReplay()
