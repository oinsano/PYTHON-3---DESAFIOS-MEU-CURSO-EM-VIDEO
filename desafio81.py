x = []
while True:
    x.append(int (input('Digite um valor: ')))
    p = str (input('Deseja continuar? [S/N]: ')).upper().strip()
    if p == 'N':
        break
print('=-=-' * 10)
print(f'Foram digitados {len(x)} valores')
x.sort(reverse=True)
print(f'Os valores em ordem decrescente: {x}')
if 5 in x:
    print(f'O valor 5 esta na lista, e foi digitado {x.count(5)} vezes')
else:
    print('O valor 5 não está na lista.')
print('=-=-' * 10)