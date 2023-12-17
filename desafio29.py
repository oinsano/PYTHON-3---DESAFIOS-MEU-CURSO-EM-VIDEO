x = float(input('Qual sua velocidade(KM/h): ') )
if x > 80:
    y = x-80
    z = y*7
    print('Você ultrapassou o limite de velocidade devera pagar R${:.2f}.'.format(z))
else:
    print('Boa viagem!')