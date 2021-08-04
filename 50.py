def exer50():
    soma = 0
    for i in range(1, 7):
        num = int(input('Digite um {} numero'.format(i)))
        if i % 2 == 0:
            soma = soma + num
    print('A soma dos valores e pares é', soma)


exer50()
