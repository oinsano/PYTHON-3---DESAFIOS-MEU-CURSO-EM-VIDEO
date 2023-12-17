#Ler o nome completo de uma pessoa - mostrar o primeiro e ultimo nome
x= input('Digite seu nome completo: ').strip().split()
print('Prazer {} {}!'.format(x[0], x[len(x)-1]))