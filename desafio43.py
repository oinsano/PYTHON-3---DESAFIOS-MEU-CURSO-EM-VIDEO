a = float(input('Altura(M): '))
p = float(input('Peso(Kg): '))
imc = p / (a ** 2)
print('IMC = {:.1f}'.format(imc))
if imc <= 18.5:
    print('MAGREZA')
elif imc > 18.5 and imc <= 24.9:
    print('SAUDAVEL')
elif imc >= 25 and imc <= 29.9:
    print('SOBREPESO')
elif imc >= 30 and imc <= 34.9:
    print('OBESIDADE GRAU I')
elif imc >= 35 and imc <= 39.9:
    print('OBESIDADE GRAU II')
else:
    print('OBESIDADE GRAU III')
