import random

def jogar():
    #randrange faz de 1 a 51 porque ele começa no 0
    numero_secreto = random.randrange(1,51)
    acertou = False
    tentativas = 5
    pontos = 1000
    nivel = 0

    print("\nBem vindo ao jogo de adivinhação\n")
    print("Qual a nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    while (nivel == 0):
        nivel = int(input("Defina nível: "))

        if (nivel < 1 or nivel > 3):
            print("Nível de estar entre 1 e 3")
            nivel = 0


    if (nivel == 1):
        numero_secreto = random.randrange(1,21)
    elif (nivel == 2):
        numero_secreto = random.randrange(1,51)
    else:        
        numero_secreto = random.randrange(1,100)

    print("\n")

    for tentativa in range(1, tentativas+1):
        #Solicita e recupera um valor do terminal
        chute = int(input("Digite o seu número ou 0 para sair: "))
        
        if (chute == 0):
            print("Pediu pra sair!!")
            break

        if (chute < 1 or chute > 50):
            print("\nVocê deve digitar um número entre 1 e 50")
            print("\n")
            continue

        acertou = numero_secreto == chute
        
        if (acertou):
            print("* Parabéns, você acertou e levou {} pontos!!\n\n".format(pontos))
            break
        else: 
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            print("\nErrrouuuuu")

            #Imprime resultado e dica quando a diferença for grande
            if (chute > numero_secreto):
                resultado = "Chutou acima do número secreto"
            else:
                resultado = "Chutou abaixo do número secreto"
            diferenca = numero_secreto - chute
            if(diferenca >= 10 or diferenca <=-10):
                print(resultado, "passando longe", sep=" ")
            else:
                print(resultado)

        #Imprime tentativas ou avisa que finalizou
        if (tentativas == tentativa):
            print("\n* Você perdeu, o número secreto era: ", numero_secreto)
        else:
            print(("Tentativa {} de {}").format(tentativa, tentativas))    
        print("\n")

if(__name__ == "__main__"):
    jogar() 