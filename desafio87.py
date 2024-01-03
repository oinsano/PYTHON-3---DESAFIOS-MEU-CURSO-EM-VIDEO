z = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
s = d = p = 0
for l in range(0, 3):
    for c in range(0, 3):
        z[l][c] = int(input(f'Digite um valor para a posicao [{l}, {c}]: '))
print('=-' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{z[l][c]:^5}]', end='')
        if z[l][c] % 2 == 0:
            s += z[l][c]
    print('')
print('=-' * 20)
for l in range(0, 3):
    if z[l][2]:
        d += z[l][2]
    if z[1][l] > p:
        p = z[1][l]
print('=-' * 20)
print(f'A soma dos valores pares é {s}')
print(f'A soma dos valores da 3 coluna é {d}')
print(f'A o maior valor da segunda linha é {p}')
print('=-' * 20)
