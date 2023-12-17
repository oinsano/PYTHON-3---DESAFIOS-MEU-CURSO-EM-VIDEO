#saber se é palindromo
from time import sleep
a = str(input('Digite uma frase: \n')).strip().upper()
p = a.split()
j = ''.join(p)
i = ''
for l in range(len(j) - 1, -1, -1):
    i += j[l]
print('Verificando se é palindromo......')
sleep(1)
if i == j:
    print('A frase digitada é um PALÍNDROMO')
else:
    print('A frase digitada NÃO é um palindromo')
