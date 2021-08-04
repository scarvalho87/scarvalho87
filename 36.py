# Fazer um programa de aprovacao imprestimo bancario
def financiamento():
    valorfinanciado = float(
        input('Digite o valor do imovel a ser financiado: '))
    anos = int(input('Em quantos anos deseja financiar: '))
    salario = float(input('Digite o valor do seu salario: '))
    mesesfinanciamento = anos * 12
    valorparcela = (valorfinanciado / mesesfinanciamento)

    if valorparcela > (salario*0.3):
        print('Seu emprestimo não pode ser feito pois excedeu os 30 porcento da renda')
    else:
        print('Seu emprestimo foi aprovado em {} anos, com {} meses no valor de R$ {:.2f} por parcela '.format(
            anos, mesesfinanciamento, valorparcela))


financiamento()
