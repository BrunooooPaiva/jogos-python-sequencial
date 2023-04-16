import random


def jogar():

    exibe_mensagem()
    palavra_secreta = carrega_palavra_secreta()

    palavra_reservada = inicializa_palavra_reservada(palavra_secreta)
    print(palavra_reservada)

    enforcar = False
    acertar = False
    erro = 0

    while (not enforcar and not acertar):

        chute = chute_e_erro(erro)

        if (chute in palavra_secreta):
            marca_chute_correto(chute, palavra_reservada, palavra_secreta)
        else:
            erro += 1

        print(palavra_reservada)

        acertar = "_" not in palavra_reservada
        enforcar = erro == 10

        imprime_mensagem_ganhador_ou_perdedor(
            acertar, enforcar, palavra_secreta)


def exibe_mensagem():
    print("***************")
    print("-JOGO DA FORCA-")
    print("***************")


def carrega_palavra_secreta():
    arquivo = open("palavrinhas.txt", "r", encoding="UTF-8")
    lista_palavra = []

    for linha in arquivo:
        linha = linha.strip()
        lista_palavra.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(lista_palavra))
    palavra_secreta = lista_palavra[numero].upper()
    return palavra_secreta


def inicializa_palavra_reservada(palavra):
    return ["_" for palavra in palavra]


def chute_e_erro(erro):
    print(f"Erros cometidos até agora: {erro} de {10}")
    return input("Chute uma letra: ").strip().upper()


def marca_chute_correto(chute, palavra_reservada, palavra_secreta):
    index = 0
    for palavra in palavra_secreta:
        if (chute == palavra):
            palavra_reservada[index] = palavra
        index += 1


def imprime_mensagem_ganhador_ou_perdedor(acertar, enforcar, palavra_secreta):
    if (acertar):
        print("Parabéns, você ganhou!")
    elif (enforcar):
        print(f"Você perdeu! A palavra correta era {palavra_secreta}")


if (__name__ == "__main__"):
    jogar()
