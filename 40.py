def nota():
    n1 = float(input('Digite a sua primeira nota'))
    n2 = float(input('Digite a sua segunda nota'))
    md = (n1+n2)/2
    if md < 5:
        print('Sua media {} é menor do que 5: REPROVADO'.format(md))
    elif md >= 5 and md <= 6.9:
        print('Voce esta em RECUPERACAO com a sua nota {}'.format(md))
    elif md >= 7:
        print('Sua media é {}, você esta APROVADO '.format(md))
    else:
        return()


nota()
