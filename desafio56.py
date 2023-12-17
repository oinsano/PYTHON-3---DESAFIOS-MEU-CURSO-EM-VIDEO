somaidade = 0
maioridade = 0
mediaidade = 0
nomevelho = ''
ttmulher20 = 0
for p in range(1, 5):
    print('------ {} pessoa -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        ttmulher20 += 1
mediaidade = somaidade / 4
print('A media de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridade, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(ttmulher20))
