casa = float (input('Qual o valor da casa?(R$) ') )
sal = float ( input('Qual seu salário?(R$) ') )
tempo = int ( input('Quer pagar em quantos anos? ') )
pres = casa / (tempo * 12)
nao = sal * 30 / 100
if pres > nao:
    print('\033[31mEmprestimo não aprovado\033[m')
    print('Prstacão no valor de R${:.2f}.'.format(pres) )
else:
    print('\033[32mEmprestimo aprovado!!\033[m')
    print('Sua prestacão mensal será de R${:.2f}.'.format(pres) )
print('{:.2f} {:.2f}'.format(pres, nao) )