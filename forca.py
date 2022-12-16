def jogar():
    print('Jogando....')

    palavra = 'python'.upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input('Qual a letra ?')
        chute = chute.strip().upper()

        letra = palavra.find(chute)



        if chute in palavra:
            index = 0
            for letra in palavra:
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
