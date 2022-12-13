def jogar():
    print('Jogando....')

    palavra = 'banana'
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input('Qual a letra ?')
        chute = chute.strip()

        letra = palavra.find(chute)

        index = 0
        
        for letra in palavra:
            if chute.upper() == letra.upper():
                letras_acertadas[index] = letra
            index = index + 1
            print(letras_acertadas)
            
                

if __name__ == '__main__':
    jogar()