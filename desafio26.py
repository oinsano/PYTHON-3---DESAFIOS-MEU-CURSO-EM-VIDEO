#ler uma frase - quantos "A" - posicao do 1 "A" - posicao do ultimo "A"
x= str (input('Digite uma frase: ')).strip().upper()

print('Nesa frase tem {} letra A'.format(x.count('A'), x.upper))
print('A primeira letra A aparece na posicao {}'.format(x.find('A')+1))
print('A ultima letra aparece na posicao {}'.format(x.rfind('A')+1))