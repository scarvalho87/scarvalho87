def numeromaior():
    num1 = int(input('Digite um numero inteiro'))
    num2 = int(input('Digite um segundo numero inteiro'))

    if num1 > num2:
        print('O primeiro numero {} e maior que o segundo {} : '.format(num1, num2))

    elif num2 > num1:
        print('O segundo numero {} e maior do que o primeiro {} : '.format(num2, num1))
    else:
        print('Não existe valor maior, os dois são iguais {} e {} '.format(num1, num2))


numeromaior()
