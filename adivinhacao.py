def jogar():
    from random import randint

    print('=-'*17)
    print('Bem vindo ao jogo de ADIVINHAÇÃO')
    print('=-'*17)

    numero_secreto = randint(1, 100)
    total_tentativas = 0
    rodada = 1
    pontos = 1000

    print('''Selecione o nível de dificuldade:
    1 - Fácil
    2 - Médio
    3 - Difícil''')
    nivel = int(input('Escolha o nível: '))
    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    while rodada <= total_tentativas:
        print('~'*17)
        print(f'Tentativa {rodada} de {total_tentativas}')
        print('~' * 17)

        numero_jogador = int(input('Digite um número entre 1 e 100: '))

        if numero_jogador < 1 or numero_jogador > 100:
            print('Você deve digitar um número entre 1 a 100!')
            continue

        acertou = numero_jogador == numero_secreto
        maior = numero_jogador > numero_secreto
        menor = numero_jogador < numero_secreto

        if acertou:
            print(f'Você ACERTOU e fez {pontos} pontos!')
            break
        else:
            if maior:
                print('Você ERROU! O seu chute foi maior do que o número secreto!')
            elif menor:
                print('Você ERROU! O seu chute foi menor do que o número secreto!')
            pontos_perdidos = abs(numero_secreto - numero_jogador)
            pontos -= pontos_perdidos

        rodada += 1

    print('FIM DO JOGO!')


if __name__ == '__main__':
    jogar()
