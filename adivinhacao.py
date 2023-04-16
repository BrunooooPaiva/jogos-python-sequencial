import random


def jogar():
    mensagem_inicio_jogo()
    escolha = int(input("Dificuldade: "))

    tentativas = 0
    if (escolha == 1):
        tentativas = 20
        print("Você terá 20 tentativas!")
    elif (escolha == 2):
        tentativas = 10
        print("Você terá 10 tentativas!")
    elif (escolha == 3):
        tentativas = 5
        print("Você terá 5 tentativas!")
    else:
        print("NÚMERO DE TENTATIVAS INVÁLIDA")

    numero_sorteado = random.randrange(1, 101)
    pontos = 1000

    for rodada in range(1, tentativas + 1):

        while True:
            print(f"Rodada {rodada} de {tentativas}")
            usuario = int(input("Chute um número [1 - 100]: "))

            if (usuario < 1 or usuario > 100):
                print("Número de chute inválido")
                continue
            else:
                break

        acertou = usuario == numero_sorteado
        maior = usuario > numero_sorteado
        menor = usuario < numero_sorteado

        if (acertou):
            print("Boa, você venceu!! Parabéns")
            print(f"Pontos finais: {pontos}")
            break
        else:
            if (maior):
                print("Passou longe, tente um número mais baixo")
            elif (menor):
                print("Passou longe, tente um número mais alto")
            pontos_perdidos = abs(numero_sorteado - usuario)
            pontos -= pontos_perdidos

    print("FIM DE JOGO!")


def mensagem_inicio_jogo():
    print("*********************")
    print("-JOGO DA ADIVINHAÇÃO-")
    print("*********************")

    print("Escolha um modo de jogo:")
    print("[1] FÁCIL [2] MÉDIO [3] DIFÍCIL")


if (__name__ == "__main__"):
    jogar()
