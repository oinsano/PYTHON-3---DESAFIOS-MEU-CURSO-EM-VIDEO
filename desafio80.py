x = []
for i in range(0, 5):
    n = int(input('Digite um numero: '))
    if i == 0 or n > x[len(x) - 1]:
        x.append(n)
        print('Adicionado ao final da lista')
    else:
        p = 0
        while p < len(x):
            if n <= x[p]:
                x.insert(p, n)
                print(f'Adicionado na posicao {p}')
                break
            p += 1
print(x)
