a = int (input('Digite um numero: '))
b = int (input('Digite outro numero: '))
c = int (input('Digite mais um numero: '))
if a > b and a > c:
    print('{} maior numero'.format(a))
if b > a and b > c:
    print('{} maior numero'.format(b))
if c > a and c > b:
    print('{} maior numero'.format(c))
if a < b and a < c:
    print('{} menor numero'.format(a))
if b < a and b < c:
    print('{} menor numero'.format(b))
if c < a and c < b:
    print('{} menor numero'.format(c))