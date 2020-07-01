def jogar():
    print("\n* Bem vindo ao jogo da Forca\n")
    
    palavra_secreta = "banana"
    lista_palavra_secreta = []

    #Cria um array de letras acertas com base na quantidade de letras da palavra secreta, iniciando com o valor _
    #ex (['_', '_' ])

    for letra_secreta in palavra_secreta:
        lista_palavra_secreta.append("_")

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input("Digite a palavra: ")
        chute.strip()
        
        index = 0
        for letra in palavra_secreta:
            if (letra.upper() == chute.upper()):
                lista_palavra_secreta[index] = letra
            index = index + 1
        
        print(' '.join(lista_palavra_secreta).upper())

if(__name__ == "__main__"):
    jogar()