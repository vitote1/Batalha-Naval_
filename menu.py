import utils
import replay


def iniciarMenu():

    while True:

        print("================================")
        print("  BATALHA NAVAL - GPTECH GAMES")
        print("================================")
        print("[1] Iniciar Partida")
        print("[2] Ver Replay")
        print("[3] Ver estatísticas")
        print("[4] Sair")
        print("--------------------------------")

        inputUsuario = input("Escolha uma opção: ")

        if inputUsuario == "1":

            utils.limparTerminal()

            print("  Selecione o modo de jogo:")
            print("----------------------------")
            print("[1] Jogador x Jogador")
            print("[2] Jogador x Computador")
            print("[3] Voltar ao menu")

            selecaoUser = input("Selecione uma opção: ")

            if selecaoUser == "1":
                utils.limparTerminal()
                return 1

            elif selecaoUser == "2":
                utils.limparTerminal()
                return 2

            elif selecaoUser == "3":
                utils.limparTerminal()
                continue

            else:
                print("\nOpção inválida!")
                input("Pressione Enter para continuar...")
                utils.limparTerminal()

        elif inputUsuario == "2":
            utils.limparTerminal()
            return 3

        elif inputUsuario == "3":
            return 4

        elif inputUsuario == "4":
            print("Programa encerrado.")
            return 0

        else:
            print("\nOpção inválida!")
            input("Pressione Enter para continuar...")
            utils.limparTerminal()
            
