from datetime import date
ano = date.today().year
x = int (input('QUal o seu ano de nascimento? '))
if 18 == ano - x:
    print('Você deve se alistar esse ano')
elif 18 > ano - x:
    print('Ainda não é tempo de se alistar.')
    t = 18 - (ano - x)
    print('Faltam {} anos para seu ano de alistamento'.format(t))
else:
    print('Já passou do seu ano de alistamento')
    t = (ano - x) - 18
    print('Se ainda não se alistou você esta atrasodo {} anos.'.format(t))