h = i = m20 = 0
while True:
    print('NOVO CADASTRO')
    while True:
        sexo = str (input('Sexo [M/F]: ')).upper().strip()
        if sexo in 'MF':
            break
    idade = int (input('Idade: '))
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    if idade >= 18:
        i += 1
    print('= ' * 15)
    while True:
        x = str(input('Continuar? [S/N]: ')).upper().strip()
        if x in 'SN':
            break
    if x == 'N':
        break
    print('=-' * 20)

print('* * ' * 10)
print(f'Ao todo temos {h} homens cadastrados.')
print(f'E temos {m20} mulheres com menos de 20 anos.')
print(f'E temos {i} pessoas com mais de 18 anos.')
