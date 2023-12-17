c = s = 0
while True:
    n = int (input('DIGITE UM VALOR[999 PAARA STOP]: '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram informados {c} valores, e a soma é igual a {s}')
