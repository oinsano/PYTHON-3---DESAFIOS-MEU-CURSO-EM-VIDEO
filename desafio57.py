#insira sexo e nunca pare
sexo = str(input ('Qual seu sexo (M/F): ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('DIGITE SEU SEXO (M/F): ')).strip().upper()
