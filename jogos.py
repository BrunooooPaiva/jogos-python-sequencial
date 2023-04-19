import adivinhacao
import forca
import velha
import jokenpo


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação (3) Jogo da velha (4) Jokenpô")

    jogo = int(input("Qual jogo? "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.jogar()
    elif (jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogar()
    elif (jogo == 3):
        print("Jogando Jogo da Velha")
        velha.jogar()
    elif (jogo == 4):
        print("Jogando Jokenpô")
        jokenpo.jogar()
    else:
        print("Opção inválida. Tente novamente")


if (__name__ == "__main__"):
    escolhe_jogo()
