i = int(input('Qual seu ano de nascimento? '))
#i = 2023 - ano
if i < 10:
    print('Sua categoria é MIRIM')
elif i > 9 and i < 15:
    print('Sua categoria é INFANTIL')
elif i > 14 and i < 20:
    print('Sua categoria é JUNIOR')
elif i > 19 and i < 21:
    print('Sua categoria é SÊNIOR')
else:
    print('Sua categoria é MASTER')
print(i)