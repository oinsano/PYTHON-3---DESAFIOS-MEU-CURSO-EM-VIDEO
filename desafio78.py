c = []
for x in range(0, 5):
    c.append(int(input(f'Digite um valor na posicão {x}: ')))
print('-=-=' * 10)
print(f'Você digitou os valores {c}')

print('-=-=' * 10)
print(f'O maior valor digitado foi {max(c)} nas posicoes: ', end=f'')
for i, v in enumerate(c):
    if v == max(c):
        print(f'{i}... ', end='')

print(f'\nO menor valor digitado foi {min(c)} nas posicoes: ', end=f'')
for i, v in enumerate(c):
    if v == min(c):
        print(f'{i}... ', end='')
print('\n', '-=-=' * 10)

