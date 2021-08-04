def exer48():
    soma = 0
    for i in range(1, 501, 2):
        if i % 3 == 0:
            # Voce tamvbem pode fazer (((((((((((((((soma += 1)))))))))))))
            soma = soma + i

    print('A soma de todos os valores é {}'.format(soma))


exer48()
