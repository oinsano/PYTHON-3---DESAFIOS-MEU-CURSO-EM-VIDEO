n = [[], []]
for i in range(0, 7):
    x = int (input('Digite um numero: '))
    if x % 2 == 0:
        n[0].append(x)
    else:
        n[1].append(x)
print(f'Os numeros pares digitados foram: {sorted(n[0])}')
print(f'Os numeros impares digitados foram: {sorted(n[1])}')
