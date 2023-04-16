
def jogar():

    mensagem_jogo()

    tabuleiro = [["-", "-", "-"],
                 ["-", "-", "-"],
                 ["-", "-", "-"]]

    player_momento = ["X", "Y"]

    while True:

        exibir_tabuleiro(tabuleiro)

        print(f"\nPlayer [{player_momento[0]}]")

        player_linha = usuario_linha()
        player_coluna = usuario_coluna()

        if (player_linha >= 0 and player_linha <= 2):
            if (tabuleiro[player_linha][player_coluna] == "X" or tabuleiro[player_linha][player_coluna] == "Y"):
                print("\nPosição ocupada. Tente novamente!\n")
                continue
            else:
                tabuleiro[player_linha][player_coluna] = player_momento[0]
                player_momento.reverse()

                if all(tabuleiro[i][i] == "X" for i in range(3)) or all(tabuleiro[i][i] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[0][i] == "X" for i in range(3)) or all(tabuleiro[0][i] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[1][i] == "X" for i in range(3)) or all(tabuleiro[1][i] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[2][i] == "X" for i in range(3)) or all(tabuleiro[2][i] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[i][0] == "X" for i in range(3)) or all(tabuleiro[i][0] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[i][1] == "X" for i in range(3)) or all(tabuleiro[i][1] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[i][2] == "X" for i in range(3)) or all(tabuleiro[i][2] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(tabuleiro[i][2-i] == "X" for i in range(3)) or all(tabuleiro[i][2-i] == "Y" for i in range(3)):
                    mensagem_player_ganhdor(player_momento)
                    break
                elif all(not tabuleiro[i][i] == "-" for i in range(3)):
                    mensagem_empate()
                    break

        else:
            print("\nValor inválido. Tente novamente!\n")
            continue


def mensagem_empate():
    print("Ninguém venceu. Fim de jogo!")


def mensagem_player_ganhdor(player_momento):
    print(f"\nFim de jogo. Player {player_momento[1]} ganhou!!")


def usuario_coluna():
    player_coluna = int(input("Escolha a coluna: "))
    return player_coluna


def usuario_linha():
    player_linha = int(input("Escolha a linha: "))
    return player_linha


def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for elemento in linha:
            print(elemento, end='   ')
        print()


def mensagem_jogo():
    print("***************")
    print("-JOGO DA VELHA-")
    print("***************")


if (__name__ == "__main__"):
    jogar()
