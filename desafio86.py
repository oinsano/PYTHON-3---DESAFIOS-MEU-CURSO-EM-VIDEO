z = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        z[l][c] = int(input(f'Digite um valor para a posicao [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{z[l][c]:^5}]', end='')
    print('')
