def tipotriangulo():
    r1 = float(input('Digite o primeiro segmento: '))
    r2 = float(input('Digite o segundo segmento: '))
    r3 = float(input('Digite o terceiro segmento: '))

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('Os segumentos acima podem formar um triangulo: ', end='')
        if r1 == r2 == r3:
            print('Equilatero')
        elif r1 != r2 != r3 != r1:
            print('Escaleno')
        else:
            print('Isoceles')
    else:
        print('Os elementos a cima não podem formar triangulo: ')


tipotriangulo()
