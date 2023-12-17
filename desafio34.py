x = float(input('Qual seu salário? '))
if x > 1250:
    y = x + (x * 10/100)
else:
    y = x + (x * 15/100)
print('Seu novo salário será {:.2f}'.format(y))