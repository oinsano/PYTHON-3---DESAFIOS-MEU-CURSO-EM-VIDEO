import desafio107M

a = int( input('Digite um valor: '))
print(f'O dobro de {desafio107M.moeda(a)} é {desafio107M.moeda(desafio107M.dobro(a))}')
print(f'A metade de {desafio107M.moeda(a)} é {desafio107M.moeda(desafio107M.metade(a))}')
print(f'10% de aumento de {desafio107M.moeda(a)} é {desafio107M.moeda(desafio107M.aumentar(a, 10))}')
print(f'13% de reduzindo de {desafio107M.moeda(a)} é {desafio107M.moeda(desafio107M.diminuir(a, 13))}')
