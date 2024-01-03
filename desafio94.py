geral = []
pessoa = {}
media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str (input('Nome: '))
    while True:
        s = str (input('Sexo [M/F]: ')).upper().strip()
        if s in 'MF':
            break
        print('ERRO! Responda apenas M ou F')
    pessoa['sexo'] = s
    x = int(input('Idade: '))
    pessoa['idade'] = x
    media += x
    geral.append(pessoa.copy())
    while True:
        re = str(input('Quer continuar? [S/N] ')).upper().strip()
        if re not in 'SN':
            print('ERRO! Responda apenas S ou N')
        else:
            break
    if re == 'S':
        print('*****' * 10)
    if re == 'N':
        break
print('=-=-' * 20)
print(geral)
print(f'A = Total de {len(geral)} pessoas cadastradas.')
print(f'B = A media de Idade é de {media/len(geral):.2f}')
print(f'C = As mulheres cadastradas foram: ', end='')
for p in geral:
    if p['sexo'] == 'F':
        print(f'{p['nome']}', end=' ')
print()
m = media/len(geral)
print('D = As pessoas acima da idade media são: ', end='')
for p in geral:
    if p['idade'] > m:
        print(f'{p['nome']}', end=' ')
print()
