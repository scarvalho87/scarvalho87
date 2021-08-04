def aula12():
    nome = str(input('Digite seu nome'))
    if nome == 'Soeslei':
        print('Seu Nome {} e muito foda!'.format(nome))
    elif nome in 'Graciele Lucas Pedro':
        print('Seu nome {} e familiar'.format(nome))
    else:
        print('Seu nome {} e normal'.format(nome))


aula12()
