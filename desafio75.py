a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
c = int(input('Digite outro valor: '))
d = int(input('Digite outro valor: '))
x = (a, b, c, d)
print(f'Voce digitou os valores {x}')
print(f'O valor 9 apareceu {x.count(9)} vezes')
if 3 in x:
    print(f'O valor 3 apareceu na {(x.index(3)) + 1}* posicão.')
for c in range(0, len(x)):
    if x[c] % 2 == 0:
        if c == 0:
            print('Os valores pares digitados foram: ', end='')
        print(f'{x[c]} ', end='')
