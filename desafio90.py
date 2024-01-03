aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float (input(f'A media de {aluno["Nome"]} é : '))
if aluno['Media'] >= 7:
    aluno['Situacao'] = 'APROVADO'
elif 5 <= aluno['Media'] < 7:
    aluno['Situacao'] = 'RECUPERACAO'
else:
    aluno['Situacao'] = 'REPROVADO'
print('=-' * 20)
print(f'O Aluno é = {aluno['Nome']}')
print(f'Media é igual a {aluno['Media']}')
print(f'Situacao de {aluno['Nome']} é {aluno["Situacao"]}')
print('=-' * 20)
print(aluno)
