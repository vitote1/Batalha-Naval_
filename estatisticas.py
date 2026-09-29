
import json
from pathlib import Path
import os

class Estatisticas():
    def __init__(self):
        self.estatisticas = []
        self.arquivo = Path("data") / "estatisticas.json"
        
        os.makedirs("data", exist_ok=True)
        
        self.carregarEstatisticas()
    
    def adicionarEstatisticas(self, jogador, numJogadas, numAcertos, numPartidas):

        for i, estatistica in enumerate(self.estatisticas):

            nome, jogadas, acertos, aproveitamento, partidas = estatistica

            if nome == jogador:

                jogadas += numJogadas
                acertos += numAcertos
                partidas += numPartidas

                aproveitamento = self.aproveitamento(acertos, jogadas)

                self.estatisticas[i] = (
                    nome, jogadas, acertos, aproveitamento, partidas)

                return

        self.estatisticas.append((jogador, numJogadas, numAcertos, self.aproveitamento(numAcertos, numJogadas), numPartidas))
    
    def aproveitamento(self, acertos, jogadas):
        if jogadas == 0:
            return 0

        return acertos / jogadas
        
    def salvarEstatisticas(self):
        with open(self.arquivo, "w", encoding = "utf-8") as arquivo:
            json.dump(self.estatisticas, arquivo, ensure_ascii=False, indent=4)
            
    def carregarEstatisticas(self):
        try:
            with open(self.arquivo, "r", encoding = "utf-8") as arquivo:
                self.estatisticas = json.load(arquivo)
        except FileNotFoundError:
            self.estatisticas = []
            
    def exibirEstatisticas(self):
        if not self.estatisticas:
            print("\nNão existem estatísticas registradas.")
            return
        
        print("\n\tEstatísticas dos Jogadores")
        print("\n------------------------------")
        
        for i, estatistica in enumerate(self.estatisticas):
            jogador, numJogadas, numAcertos, aproveitamento, numPartidas = estatistica
        
            print(f"Jogador {i + 1}")
            print(f"\n\tNome: {jogador}\n\tNúmero de partidas: {numPartidas}")
            print(f"\n\tNúmero de jogadas: {numJogadas}\n\tNúmero de acertos: {numAcertos}")
            print(f"\n\tAproveitamento : {aproveitamento:.1%}")
        

