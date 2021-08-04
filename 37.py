def basenumerica():
    numero = int(input('Digite um numero inteiro'))
    opcao = int(input(
        'Agora, escolha uma base de conversao: 1-Binario, 2-Octonal ou 3-Hexadecimal'))
    if opcao == 1:
        print('Seu numero {} digitado fo convertido para binario {}'.format(
            numero, bin(numero)[2:]))
    elif opcao == 2:
        print('Seu numero {} digitado fo convertido para Octonal {}'.format(
            numero, oct(numero)[2:]))
    elif opcao == 3:
        print('Seu numero {} digitado fo convertido para Hexadecimal {}'.format(
            numero, hex(numero)[2:]))
    else:
        print('Digite 1 2 ou 3 opcao')


# tivemos que  usar o [2:] para fatirar as respostas dos numemeros...
basenumerica()
