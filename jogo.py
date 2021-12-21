import adivinhacao
import forca

while True:
    print('=-' * 14)
    print('Bem vindo! Escolha o jogo')
    print('=-' * 14)
    print('''1 - ADIVINHAÇÃO
2 - FORCA
3 - SAIR''')

    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        adivinhacao.jogar()
    if opcao == 2:
        forca.jogar()
    if opcao == 3:
        print('Saindo do programa! Volte Sempre!')
        break
