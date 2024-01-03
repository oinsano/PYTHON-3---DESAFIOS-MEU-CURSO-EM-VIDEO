x = []
p = []
i = []
while True:
    n = int (input('Digite um valor: '))
    x.append(n)
    if n % 2 == 0:
        p.append(n)
    else:
        i.append(n)
    t = str (input('Deseja continuar? [S/N]: ')).upper().strip()
    if t == 'N':
        break
print(f'Lista completa: {x}')
print(f'Lista de pares: {p}')
print(f'Lista de impares: {i}')
