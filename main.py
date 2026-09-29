from jogador import Jogador
from navios import Navio
from tabuleiro import Tabuleiro
from replay import Replay
from computador import Computador
import utils
import menu
from estatisticas import Estatisticas


def posicionarNavios(jogador):

    tipos = [("Encouraçado", 2),("Porta-Aviões", 2)]

    for tipo, quantidade in tipos:

        for i in range(quantidade):

            while True:
                try:
                    utils.limparTerminal()

                    print(f"\n{jogador.getNome()}, defina a posição dos seus navios.")
                    print(f"\nTabuleiro de {jogador.getNome()}:\n")
                    jogador.tabuleiro.exibirTabuleiro()

                    print(f"\nNavios já posicionados:")
                    
                    if len(jogador.getNavios()) == 0:
                        print("Nenhum")

                    for navio in jogador.getNavios():
                        print(f"Navio {navio.getTipo()} - {navio.getPosicoes()}")

                    coordenada = input(f"\nDigite a coordenada inicial do {tipo} {i + 1} (ex: A1): ")

                    orientacao = input("Digite a orientação (direita, esquerda, cima ou baixo): ")

                    navio = Navio(coordenada, tipo, orientacao)
                    jogador.adicionarNavio(navio)

                    print("\nNavio posicionado")

                    input("\nPressione Enter para continuar...")
                    break

                except ValueError as e:
                    print(f"\nErro: {e}. Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    utils.limparTerminal()
    
    print("\nSeu tabuleiro ficou assim:\n ")
    jogador.tabuleiro.exibirTabuleiro()
    
    for navio in jogador.getNavios():
        print(f"Navio {navio.getTipo()} - {navio.getPosicoes()}")
        
    input("\nPressione Enter para continuar...")
    
    
def turno(jogador, adversario, rodada, replay):

    utils.limparTerminal()
    
    print(f"\nJogada do {jogador.getNome()}.")
    input("\nPressione Enter quando estiver pronto...")

    while True:
        utils.limparTerminal()

        try:
            print(f"\nRodada {rodada}")
            
            print(f"\n\tSeu tabuleiro\n")
            jogador.tabuleiro.exibirTabuleiro()
    
            print(f"\n\tTabuleiro de {adversario.getNome()}\n")
            adversario.tabuleiro.exibirTabuleiroAtaque()
    
            print(f"\nVez do jogador {jogador.getNome()}.\n")
            
            coordenada = input("Digite a coordenada que deseja atacar (ex: A1): ")
            resultado = jogador.atacar(adversario, coordenada)
            if resultado is None:
                print("\nVocê já atacou essa coordenada.")
                input("\nPressione Enter para continuar...")
                continue
            ocorrido = "Acertou" if resultado else "Errou"
            
            utils.limparTerminal()
            
            print(f"\nO {jogador.getNome()} atacou {coordenada}.")
            if ocorrido == "Acertou":
                print(f"\nO {jogador.getNome()} acertou navio de {adversario.getNome()}!")
            else:
                print(f"\nO {jogador.getNome()} errou!")

            replay.adicionarJogada(rodada, jogador.getNome(), adversario.getNome(), coordenada, ocorrido)
            input("\nPressione Enter para continuar...")
            break

            
        
        except ValueError as e:
            print(f"\nErro: {e}. Tente novamente.")
            input("\nPressione Enter para continuar...")
    
    utils.limparTerminal()
    
    print(f"\nMapa de {adversario.getNome()} após o ataque:\n")
    adversario.tabuleiro.exibirTabuleiroAtaque()

    input("\nPressione Enter para continuar...")
    
    if ocorrido == "Acertou":
        return 1
    
    return 0

def lerNome(numero):
    while True:
        nome = input(f"\nDigite o nome do jogador {numero}: ").strip()

        if nome:
            return nome

        print("\nNome inválido. O nome não pode ser vazio.\n")
    

opcao = True
replay = Replay()
estatisticas = Estatisticas()

while not opcao == 0:

    opcao = menu.iniciarMenu()
    
    if opcao == 1:
        replay.limparReplay()
        print(f"\tBATALHA NAVAL - Jogador vs Jogador")

        jogador1 = Jogador(lerNome(1), 12)
        jogador2 = Jogador(lerNome(2), 12)

        input("\nPressione Enter para iniciar o jogo...")
        
        utils.limparTerminal()
        
        print("\n\tEste é o mapa do jogo, você poderá definir a posição de seus navios, e ao decorrer das rodadas, \n"
            "poderá atacar o inimigo, e tentar afundar todos os navios dele, para vencer a partida.\n")

        Tabuleiro("~").exibirTabuleiro()

        print("\nNo mapa, '~' é o mar, 'P' é o porta-aviões(ocupa 4 casas), e 'E' é o encouraçado(ocupa 2 casas).")
        print("\nA definição dos navios é feita inserindo a coordenada inicial e sua direção.\n")
        
        print(f"Jogador 1: {jogador1.getNome()} | Vida: {jogador1.getVida()}")
        print(f"Jogador 2: {jogador2.getNome()} | Vida: {jogador2.getVida()}")
        
        input("\nPressione Enter para continuar...")
        
        utils.limparTerminal()
        
        posicionarNavios(jogador1)
        
        posicionarNavios(jogador2)
        
        utils.limparTerminal()

        
        cont = 1

        while True:
            acerto = True
            while acerto and jogador2.verificarEstaVivo():
                acerto = turno(jogador1, jogador2, cont, replay)
                
            if not jogador2.verificarEstaVivo():
                break
            
            acerto = True 
            
            while acerto and jogador1.verificarEstaVivo():
                acerto = turno(jogador2, jogador1, cont, replay)
            
                    
            if not jogador1.verificarEstaVivo():
                break

            utils.limparTerminal()
            print(f"\nFim da rodada {cont}!\n")
            print(f"Jogador 1: {jogador1.getNome()} | Vida: {jogador1.getVida()}")
            print(f"Jogador 2: {jogador2.getNome()} | Vida: {jogador2.getVida()}")
            input("\nPressione Enter para continuar...")

            cont += 1

        utils.limparTerminal()
            
        if jogador1.verificarEstaVivo():
            print(f"\nParabéns {jogador1.getNome()}! Você venceu a partida!")
        else:
            print(f"\nParabéns {jogador2.getNome()}! Você venceu a partida!")
        
        input("\nPressione Enter para continuar...")
            
        numJogadas1 = 0
        numAcertos1 = 0
        numJogadas2 = 0
        numAcertos2 = 0

        for jogada in replay.jogadas:
            rodada, nomeJogador, alvo, coordenada, ocorrido = jogada

            if nomeJogador == jogador1.getNome():
                numJogadas1 += 1

                if ocorrido == "Acertou":
                    numAcertos1 += 1

            elif nomeJogador == jogador2.getNome():
                numJogadas2 += 1

                if ocorrido == "Acertou":
                    numAcertos2 += 1

        estatisticas.adicionarEstatisticas(
            jogador1.getNome(),
            numJogadas1,
            numAcertos1,
            1
        )

        estatisticas.adicionarEstatisticas(
            jogador2.getNome(),
            numJogadas2,
            numAcertos2,
            1
        )

        estatisticas.salvarEstatisticas()
        replay.salvarReplay()

    elif opcao == 2:
        replay.limparReplay()

        print(f"\tBATALHA NAVAL - Jogador vs Computador")
        jogador = Jogador(lerNome(1), 12)
        computador = Computador(12)
        
        input("\nPressione Enter para iniciar o jogo...")
        
        utils.limparTerminal()
        
        print(f"Jogador 1: {jogador.getNome()} | Vida: {jogador.getVida()}")
        print(f"Jogador 2: {computador.getNome()} | Vida: {computador.getVida()}")
        
        input("\nPressione Enter para continuar...")
            
        utils.limparTerminal()
            
        posicionarNavios(jogador)
        
        computador.posicionarNavios()
        
        print("\nNavios do computador:")
        computador.tabuleiro.exibirTabuleiro()

        input("\nPressione Enter para continuar...")
        
        utils.limparTerminal()
        
        cont = 1 
        while True:
            acerto = True
            while acerto and computador.verificarEstaVivo():
                acerto = turno(jogador, computador, cont, replay)
                
            if not computador.verificarEstaVivo():
                break
            
            acerto = True 
            
            while acerto and jogador.verificarEstaVivo():
                coordenada, acerto = computador.atacar(jogador)
                replay.adicionarJogada(cont, computador.getNome(), jogador.getNome(), coordenada, "Acertou" if acerto else "Errou")
                print(f"\nO computador atacou {coordenada}.")

                if acerto:
                        print("O computador acertou seu navio!")
                else:
                        print("O computador errou!")

                input("\nPressione Enter para continuar...")
                
            if not jogador.verificarEstaVivo():
                break
            
            utils.limparTerminal()
            print(f"\nFim da rodada {cont}!\n")
            print(f"Jogador 1: {jogador.getNome()} | Vida: {jogador.getVida()}")
            print(f"Computador | Vida: {computador.getVida()}")
            input("\nPressione Enter para continuar...")
                
            cont += 1
            
            utils.limparTerminal()
                
        if jogador.verificarEstaVivo():
            print(f"\nParabéns {jogador.getNome()}! Você venceu a partida!")
        else:
            print(f"\nParabéns {computador.getNome()}! Você venceu a partida!")
        
        input("\nPressione Enter para continuar...")
                
            
        numJogadasJogador = 0
        numAcertosJogador = 0

        numJogadasComputador = 0
        numAcertosComputador = 0

        for jogada in replay.jogadas:
            rodada, nomeJogador, alvo, coordenada, ocorrido = jogada

            if nomeJogador == jogador.getNome():
                numJogadasJogador += 1

                if ocorrido == "Acertou":
                    numAcertosJogador += 1

            elif nomeJogador == computador.getNome():
                numJogadasComputador += 1

                if ocorrido == "Acertou":
                    numAcertosComputador += 1
                    
        estatisticas.adicionarEstatisticas(
            jogador.getNome(),
            numJogadasJogador,
            numAcertosJogador,
            1
        )

        estatisticas.adicionarEstatisticas(
            computador.getNome(),
            numJogadasComputador,
            numAcertosComputador,
            1
        )

        estatisticas.salvarEstatisticas()
            
        replay.salvarReplay()
        
    elif opcao == 3:
        replay.exibirReplay()
        input("\nPressione Enter para sair...")
        
    elif opcao == 4:
        estatisticas.exibirEstatisticas()
        input("\nPressione Enter para sair...")
        

from jogador import Jogador
from navios import Navio
from tabuleiro import Tabuleiro
from replay import Replay
from computador import Computador
import utils
import menu


def posicionarNavios(jogador):

    tipos = [("Encouraçado", 2),("Porta-Aviões", 2)]

    for tipo, quantidade in tipos:

        for i in range(quantidade):

            while True:
                try:
                    utils.limparTerminal()

                    print(f"\n{jogador.getNome()}, defina a posição dos seus navios.")
                    print(f"\nTabuleiro de {jogador.getNome()}:\n")
                    jogador.tabuleiro.exibirTabuleiro()

                    print(f"\nNavios já posicionados:")
                    
                    if len(jogador.getNavios()) == 0:
                        print("Nenhum")

                    for navio in jogador.getNavios():
                        print(f"Navio {navio.getTipo()} - {navio.getPosicoes()}")

                    coordenada = input(f"\nDigite a coordenada inicial do {tipo} {i + 1} (ex: A1): ")

                    orientacao = input("Digite a orientação (direita, esquerda, cima ou baixo): ")

                    navio = Navio(coordenada, tipo, orientacao)
                    jogador.adicionarNavio(navio)

                    print("\nNavio posicionado")

                    input("\nPressione Enter para continuar...")
                    break

                except ValueError as e:
                    print(f"\nErro: {e}. Tente novamente.")
                    input("\nPressione Enter para continuar...")
    
    utils.limparTerminal()
    
    print("\nSeu tabuleiro ficou assim:\n ")
    jogador.tabuleiro.exibirTabuleiro()
    
    for navio in jogador.getNavios():
        print(f"Navio {navio.getTipo()} - {navio.getPosicoes()}")
        
    input("\nPressione Enter para continuar...")
    

def atacar(jogador, coordenada):
    
        if jogador.tabuleiro.getSprite(coordenada) == "~":
            jogador.tabuleiro.setSprite("X", jogador.tabuleiro.coordenada(coordenada))
            print(f"\nO ataque em {coordenada.upper()} não acertou nenhum navio.")
            return True
        elif jogador.tabuleiro.getSprite(coordenada) in ["H", "X"]:
            print(f"\nO ataque em {coordenada.upper()} já foi realizado.")
            input("\nPressione Enter para continuar...")
            return False
        else:
            jogador.tabuleiro.setSprite("H", jogador.tabuleiro.coordenada(coordenada))
            jogador.diminuirVida()
            print(f"\nO ataque em {coordenada.upper()} acertou um navio inimigo.")
            return True
        
        
def turno(jogador, adversario, rodada, replay):

    utils.limparTerminal()
    
    print(f"\nJogada do {jogador.getNome()}.")
    input("\nPressione Enter quando estiver pronto...")

    while True:
        utils.limparTerminal()

        print(f"\nRodada {rodada}")

        print(f"\n\tSeu tabuleiro\n")
        jogador.tabuleiro.exibirTabuleiro()

        print(f"\n\tTabuleiro de {adversario.getNome()}\n")
        adversario.tabuleiro.exibirTabuleiroAtaque()

        print(f"\nVez do jogador {jogador.getNome()}.\n")

        try:
            coordenada = input("Digite a coordenada que deseja atacar (ex: A1): ")
            resultado = atacar(adversario, coordenada)

            if resultado:
                ocorrido = ("Acertou" if adversario.tabuleiro.getSprite(coordenada) == "H" else "Errou")

                replay.adicionarJogada(rodada, jogador.getNome(), adversario.getNome(), coordenada, ocorrido)
                
                break

            input("\nPressione Enter para continuar...")
        
        except ValueError as e:
            print(f"\nErro: {e}. Tente novamente.")
            input("\nPressione Enter para continuar...")
        
    print(f"\nMapa de {adversario.getNome()} após o ataque:\n")
    adversario.tabuleiro.exibirTabuleiroAtaque()

    input("\nPressione Enter para continuar...")
    
    if ocorrido == "Acertou":
        return 1
    
    return 0

def lerNome(numero):
    while True:
        nome = input(f"\nDigite o nome do jogador {numero}: ").strip()

        if nome:
            return nome

        print("\nNome inválido. O nome não pode ser vazio.\n")
    

opcao = menu.iniciarMenu()
replay = Replay()

if opcao == 1:
    print(f"\tBATALHA NAVAL - Jogador vs Jogador")

    jogador1 = Jogador(lerNome(1), 12)
    jogador2 = Jogador(lerNome(2), 12)

    input("\nPressione Enter para iniciar o jogo...")
    
    utils.limparTerminal()
    
    print("\n\tEste é o mapa do jogo, você poderá definir a posição de seus navios, e ao decorrer das rodadas, \n"
          "poderá atacar o inimigo, e tentar afundar todos os navios dele, para vencer a partida.\n")

    Tabuleiro("~").exibirTabuleiro()

    print("\nNo mapa, '~' é o mar, 'P' é o porta-aviões(ocupa 4 casas), e 'E' é o encouraçado(ocupa 2 casas).")
    print("\nA definição dos navios é feita inserindo a coordenada inicial e sua direção.\n")
    
    print(f"Jogador 1: {jogador1.getNome()} | Vida: {jogador1.getVida()}")
    print(f"Jogador 2: {jogador2.getNome()} | Vida: {jogador2.getVida()}")
    
    input("\nPressione Enter para continuar...")
    
    utils.limparTerminal()
    
    posicionarNavios(jogador1)
    
    posicionarNavios(jogador2)
    
    utils.limparTerminal()

    
    cont = 1

    while True:
        acerto = True
        while acerto and jogador2.verificarEstaVivo():
            acerto = turno(jogador1, jogador2, cont, replay)
            
        if not jogador2.verificarEstaVivo():
            break
        
        acerto = True 
        
        while acerto and jogador1.verificarEstaVivo():
            acerto = turno(jogador2, jogador1, cont, replay)
        
                   
        if not jogador1.verificarEstaVivo():
            break

        utils.limparTerminal()
        print(f"\nFim da rodada {cont}!\n")
        print(f"Jogador 1: {jogador1.getNome()} | Vida: {jogador1.getVida()}")
        print(f"Jogador 2: {jogador2.getNome()} | Vida: {jogador2.getVida()}")
        input("\nPressione Enter para continuar...")

        cont += 1

    utils.limparTerminal()
        
    if jogador1.verificarEstaVivo():
        print(f"\nParabéns {jogador1.getNome()}! Você venceu a partida!")
    else:
        print(f"\nParabéns {jogador2.getNome()}! Você venceu a partida!")
    
    replay.salvarReplay()

elif opcao == 2:
    print(f"\tBATALHA NAVAL - Jogador vs Computador")
    jogador = Jogador(lerNome(1), 12)
    computador = Computador(12)
    
    input("\nPressione Enter para iniciar o jogo...")
    
    utils.limparTerminal()
    
    print(f"Jogador 1: {jogador.getNome()} | Vida: {jogador.getVida()}")
    print(f"Jogador 2: {computador.getNome()} | Vida: {computador.getVida()}")
    
    input("\nPressione Enter para continuar...")
        
    utils.limparTerminal()
        
    posicionarNavios(jogador)
    
    computador.posicionarNavios()
    
    print("\nNavios do computador:")
    computador.tabuleiro.exibirTabuleiro()

    input("\nPressione Enter para continuar...")
    
    utils.limparTerminal()
    
    cont = 1 
    while True:
        acerto = True
        while acerto and computador.verificarEstaVivo():
            acerto = turno(jogador, computador, cont, replay)
            
        if not computador.verificarEstaVivo():
            break
        
        acerto = True 
        
        while acerto and jogador.verificarEstaVivo():
           coordenada, acerto = computador.atacar(jogador)
           print(f"\nO computador atacou {coordenada}.")

           if acerto:
                print("O computador acertou seu navio!")
           else:
                print("O computador errou!")

        input("\nPressione Enter para continuar...")
        
        if not jogador.verificarEstaVivo():
            break
        
        utils.limparTerminal()
        print(f"\nFim da rodada {cont}!\n")
        print(f"Jogador 1: {jogador.getNome()} | Vida: {jogador.getVida()}")
        print(f"Computador | Vida: {computador.getVida()}")
        input("\nPressione Enter para continuar...")
            
        cont += 1
        
        utils.limparTerminal()
            
        if jogador.verificarEstaVivo():
            print(f"\nParabéns {jogador.getNome()}! Você venceu a partida!")
        else:
            print(f"\nParabéns {computador.getNome()}! Você venceu a partida!")
        
        replay.salvarReplay()
    
    
    
elif opcao == 3:
    replay.exibirReplay()
    


