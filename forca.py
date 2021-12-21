def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if erros == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if erros == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if erros == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if erros == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if erros == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if erros == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if erros == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    from random import randint

    print('=-' * 14)
    print('Bem vindo ao jogo da FORCA')
    print('=-' * 14)

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = randint(0, len(palavras))

    palavra_secreta = palavras[numero]
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = str(input('Escolha uma letra: ')).strip().upper()

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[posicao] = chute
                posicao += 1
        else:
            print(f'Você errou! Agora você tem {6 - tentativas} tentativa(s)!')
            tentativas += 1
            desenha_forca(tentativas)

        enforcou = tentativas == 7
        acertou = '_' not in letras_acertadas

        for letra in letras_acertadas:
            print(letra, end='')
        print('')

        if acertou:
            print('Você GANHOU!')
        if enforcou:
            print('Você PERDEU!')
            print(f'A palavra era {palavra_secreta}')

    print('FIM DO JOGO!')


if __name__ == '__main__':
    jogar()
