from datetime import date
a = 0
b = 0
o = date.today().year
for i in range (1,8):
    x = int(input('Digite seu ano de nascimento: '))
    if  o - x  >= 18:
        a = a + 1
    else:
        b = b +1
print('{} pessoas são maiores de idade.'.format(a) )
print('{} pessoas são menores de idade.'.format(b) )
