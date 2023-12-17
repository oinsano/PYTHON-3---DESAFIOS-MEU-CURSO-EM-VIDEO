x = float(input('Qual a distancia da sua viagem? ') )
if x <= 200:
    p = x*0.5
    print('Sua passagem é R${:.2f}.'.format(p))
else:
    p = x*0.45
    print('Sua passagem é R${:.2f}.'.format(p) )
