c = []
while True:
    x = int (input('Digite um valor: '))
    if x not in c:
        c.append(x)
        print('Numero adicionado com sucesso....')
    else:
        print('Valor duplicado. Não vou adicionar.')
    x = str(input('Quer continuar? [S/N] ')).upper().strip()
    if x == 'N':
        break
print(f'Você digitou od valores: {sorted(c)}')
