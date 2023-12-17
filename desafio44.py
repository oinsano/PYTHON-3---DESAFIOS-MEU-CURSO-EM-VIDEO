x = float (input('QUAL O VALOR DAS COMPRAS: '))
print('=*' * 20)
print('Qual foma de pagamento? ')
print('1 - A VISTA OU CHEQUE')
print('2 - A VISTA NO CARTÃO')
print('3 - ATÉ 2X NO CARTÃO')
print('4 - A3X OU MAIS NO CARTÃO')
p = int (input('ESCOLHA UMA OPCÃO: '))
print('=*' * 20)
if p == 1:
    i = x - (x * 10 / 100)
    print('Você ira pagar {:.2f}$'.format(i))
elif p == 2:
    i = x - (x * 5 / 100)
    print('Você ira pagar {:.2f}$'.format(i))
elif p == 3:
    print('Você ira pagar {}$, em duas parcelas de {}$.'.format(x, x / 2))
elif p == 4:
    i = x + (x * 20 / 100)
    par = int(input('Quantas Parcelas? ') )
    print('Você ira pagar {}$ em {} parcelas de R${}'.format(i, par, i / par))
    print('Você ira pagar {}$'.format(i))
else:
    print('FORMA DE PAGAMENTO INCORRETA, TENTE NOVAMENTE')
print('OBRIGADO PELA PREFERENCIA')
