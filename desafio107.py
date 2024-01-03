import moeda

a = int( input('Digite um valor: '))
print(f'O dobro de {a} é {moeda.dobro(a)}')
print(f'A metade de {a} é {moeda.metade(a)}')
print(f'10% de aumento de {a} é {moeda.aumentar(a, 10)}')
print(f'13% de reduzindo de {a} é {moeda.diminuir(a, 13)}')
