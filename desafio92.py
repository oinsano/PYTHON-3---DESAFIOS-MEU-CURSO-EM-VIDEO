from datetime import datetime
carteira = {}
carteira['nome'] = str(input('Nome: '))
x = int(input('Ano de nascimento: '))
carteira['idade'] = 2023 - x
carteira['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if carteira['ctps'] != 0:
    carteira['ac'] = int(input('Ano de Contratacão: '))
    carteira['salario'] = float(input('Salário R$ '))
    carteira['Aposentadoria'] = carteira['idade'] + (35 - (datetime.now().year - carteira['ac']))
print('=-' * 20)
for i, v in carteira.items():
    print(f'{i} tem o valor {v}.')
