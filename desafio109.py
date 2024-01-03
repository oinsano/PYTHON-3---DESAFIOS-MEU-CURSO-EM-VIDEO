import desafio107M

a = int( input('Digite um valor: '))
print(f'O dobro de {desafio107M.moeda(a)} é {desafio107M.dobro(a, True)}')
print(f'A metade de {desafio107M.moeda(a)} é {desafio107M.metade(a, True)}')
print(f'10% de aumento de {desafio107M.moeda(a)} é {desafio107M.aumentar(a, 10, True)}')
print(f'13% de reduzindo de {desafio107M.moeda(a)} é {desafio107M.diminuir(a, 13, True)}')