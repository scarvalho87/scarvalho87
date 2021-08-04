from datetime import date
import datetime


def alistamento():
    anonascimento = int(input('Digite o ano do seu nascimento'))
    anoatual = date.today().year
    idade = (anoatual - anonascimento)
    falta = 18 - idade
    passou = idade - 18
    if idade < 18:
        print('a Pessoa tem {} anos e ainda faltam {} para se alistar'.format(
            idade, falta))
    elif idade == 18:
        print('a Pessoa tem {} anos e precisa se alistar agora'.format(idade))
    elif idade > 18:
        print('a Pessoa tem {} anos e ja passou {} do tempo de se alistar'.format(
            idade, passou))


alistamento()
