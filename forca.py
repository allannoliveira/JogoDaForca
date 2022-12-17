import random
def jogar():
    print('Jogando....')


    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))

    palavras = palavras[numero].upper()


    letras_acertadas = ['_' for letra in palavras]


    

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)
    while not enforcou and not acertou:
        chute = input('Qual a letra ?')
        chute = chute.strip().upper()

        letra = palavras.find(chute)


       
        if chute in palavras:
            index = 0
            for letra in palavras:
                if chute.upper() == letra.upper():
                    letras_acertadas[index] = letra
                index += 1
                print(letras_acertadas)


        else:

            erros += 1

        enforcou = erros == 6

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print('Parabens! Você ganhou ") ')
    else:
        print('Não desanime, tente outra vez. ')

    print("FIM DO JOGO")


if __name__ == '__main__':
    jogar()
