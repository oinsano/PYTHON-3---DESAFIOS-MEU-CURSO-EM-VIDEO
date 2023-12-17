a = int (input('Digite a primeira reta: '))
b = int (input('Digite a segunda reta: '))
c = int (input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < b + c:
        print('\033[4;34mPodem formar um triangulo\033[m')
        if a == b and a == c:
            print('TRIANGULO EQUILATERO')
        elif a != b and b != c and a != c:
            print('TRIANGULO ESCALENO')
        else:
            print('TRIANGULO ISOCELES')
else:
        print('\033[4;31mNÃO podem formar triangulo\033[m')