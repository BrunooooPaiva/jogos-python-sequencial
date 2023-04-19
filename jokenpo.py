import random
import time

def jogar():
    print("*********")
    print("-JOKENPÔ-")
    print("*********")

    time.sleep(1)

    escolhas = ["Pedra", "Papel", "Tesoura"]

    combinacoe = {"Tesoura":"Pedra",
                  "Papel":"Tesoura",
                  "Pedra":"Papel"}

    while True:

        indice_aleatorio = random.randrange(len(escolhas))
        maquina = escolhas[indice_aleatorio]
        
        usuario = input("\nEscolha entre \nPedra | Papel | Tesoura\n\nResposta:").lower().capitalize()

        time.sleep(1)
        print(f"A máquina escolheu: {maquina}")

        if (usuario == maquina):
            print("\n\nEmpate. Tente novamente\n\n")
            
        else:
            if (combinacoe[usuario] == maquina):
                print("\nMáquina venceu")
                break
            else:
                print("\nUsuário ganhou")
                break


if (__name__ == "__main__"):
    jogar()
