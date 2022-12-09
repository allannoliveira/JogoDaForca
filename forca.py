def jogar():
    print('Jogando....')
    
    palavra = 'Python'

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):
        chute = input('Qual a letra ?')

        letra = palavra.find(chute)

        index = 1

        for letra in palavra:
            if chute == letra:
                print("Encontrei a letra {} na posicao {}".format(letra, index))
            index = index + 1


        




if (__name__  == '__main__'):
    jogar()