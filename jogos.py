import forca
import adivinhacao

def escolhe_jogo():
    print()
    print("Escolha o seu jogo!")
    print()

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("Qual o jogo? "))

    if (jogo == 1):
        print()
        print("-> Jogando forca <-")
        forca.jogar()
    elif(jogo == 2):
        print()
        print("-> Jogando adivinhação <-")
        adivinhacao.jogar()
    print()

if (__name__ == "__main__"):
    escolhe_jogo()