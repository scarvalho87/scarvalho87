def calcularimc():
    peso = float(input('Digite seu peso'))
    altura = float(input('Digite a sua altura'))
    imc = (peso/(altura**2))

    if imc < 18.5:
        print('Abaixo do peso ideal seu imc é {:.1f}: '.format(imc))
    if imc >= 18.5 and imc < 25:
        print('Você esta no  peso ideal, seu imc é {:.1f}:'.format(imc))
    if imc >= 25 and imc < 30:
        print('Sobrepeso, seu imc é {:.1f}: '.format(imc))
    if imc >= 30 and imc < 40:
        print('Obesidade seu imc é {:.1f}: '.format(imc))
    if imc >= 40:
        print('Obesidade Morbida')


calcularimc()
