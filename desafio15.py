#ALUGUEL DE CARROS
d=int(input('Quantos dias o carro foi alugado? ') )
km=float (input('Quantos km foram rodados? ') )
pagar=(d*60)+(km*0.15)
print('O total a ser pago é R${:.2f}'.format(pagar))