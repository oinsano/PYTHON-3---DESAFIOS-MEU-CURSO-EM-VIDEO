print('=' * 50)
print(f'{'LISTA DE PRODUTOS':^50}')
print('=' * 50)
produtos = ('Lapis', 1.5, 'Borracha', 3, 'Caderno', 10, 'Estojo', 7.5, 'Transferidor', 9, 'Compasso', 4, 'Mochila', 90, 'Canetas', 10, 'Livro', 27 )
for p in range(0, len(produtos)):
    if p % 2 == 0:
        print(f'{produtos[p]:.<40}', end='')
    else:
        print(f'R${produtos[p]:>8.2f}')


print('=' * 50)