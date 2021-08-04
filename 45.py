from random import randint
from time import sleep


def jokepo():
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = randint(0, 2)
    print("As Opcoes de Jogo são: 0-Pedra, 1-Papel, 2-Tesoura ")
    sleep(1)
    jogador = int(input('Digite o o seu jogo: '))
    sleep(1)
    print('-+'*11)
    print('O Computador escolheu {}'.format(itens[pc]))
    print('O Jogador escolheu {}'.format(itens[jogador]))
    print('-+'*11)

    if pc == 0:  # computador escolhendo o 0 - PEDRA
        if jogador == 0:
            print('Deu empate!')
        elif jogador == 1:
            print('O Jogador Venceu!')
        elif jogador == 2:
            print('O Computador Venceu!')
        else:
            print('Entrada invalida')
    elif pc == 1:  # computador escolhendo o 1 - PAPEL
        if jogador == 0:
            print('Computador Vence!')
        elif jogador == 1:
            print('Empate!')
        elif jogador == 2:
            print('O Jogador Venceu!')
        else:
            print('Entrada invalida')
    elif pc == 2:  # computador escolhendo o 2 - TESOURA
        if jogador == 0:
            print('Jogador Vence!')
        elif jogador == 1:
            print('O Computador Vence Venceu!')
        elif jogador == 2:
            print('Empate!')
        else:
            print('Entrada invalida')


jokepo()
