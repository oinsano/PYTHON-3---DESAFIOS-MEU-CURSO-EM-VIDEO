pessoa = list()
dado = list()
pesado = list()
leve = list()
maior = menor = 0
while True:
    dado.append(str (input('Digite o nome: ')))
    dado.append(int (input('Digite seu peso: ')))
    if len(pessoa) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoa.append(dado[:])
    dado.clear()
    x = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if x == 'N':
        break
for p in pessoa:
    if p[1] == maior:
        pesado.append(p[0])
    elif p[1] == menor:
        leve.append(p[0])
print(f'Foram cadastradas {len(pessoa)} pessoas.')
print(f'Essas pessoas são as mais pesadas pesando {maior}: {pesado}')
print(f'Essas pessoas são as mais leves pensnado {menor}: {leve}')
