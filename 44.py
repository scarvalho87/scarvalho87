def calculopagamento():
    preco = float(input('Digite o valor do produto a ser pago: '))
    pagamento = int(input(
        'Digite a forma de pagamento: 1-Dinheiro, 2-Av Cartao, 3 -2x-Cartao, 4-3x ou mais'))

    if pagamento == 1:
        print('O valor a ser pago em dinheiro com desconto é :',
              (preco - (preco*0.10)))
    elif pagamento == 2:
        print('O valor a ser pago no cartão é :', (preco - (preco*0.05)))
    elif pagamento == 3:
        parcela = preco / 2
        print('O valor a ser pago e {} com 2 parcelas de {}:'.format(preco, parcela))
    elif pagamento == 4:
        print('O valor a ser pago e:', (preco + (preco*0.20)))


calculopagamento()
