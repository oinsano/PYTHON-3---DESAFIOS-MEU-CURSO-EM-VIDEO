print('=' * 30)
print('BANCO RUIM')
print('=' * 30)
x = int (input ('Qual valor voce quer sacar? R$'))
c = 50
tc = 0
while True:
    if x >= c:
        x -= c
        tc += 1
    else:
        if tc > 0:
            print(f'Total de {tc} cedula de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if x == 0:
            break
print('=' * 30)
print('Salve')