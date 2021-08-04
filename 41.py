
from datetime import date


def calculofaixa():
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '))
    hoje = date.today().year
    idade = (hoje - ano)
    print(idade)

# Calculos dos IF para validar as categorias

    if idade <= 9:
        print('O atléta tem {} anos e é MIRIM: '.format(idade))
    elif idade >= 10 and idade <= 14:
        print('O atleta tem {} anos e é INFANTIL: '.format(idade))
    elif idade >= 15 and idade <= 19:
        print('O tleta tem {} anos e é JUNIOR:'.format(idade))
    elif idade >= 20 and idade <= 25:
        print('O tleta tem {} anos e é SENIOR:'.format(idade))
    elif idade >= 26:
        print('O tleta tem {} anos e é MASTER:'.format(idade))


calculofaixa()
