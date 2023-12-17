#TRANSFOMAR UM NUMERO EM BINARIO, OCTAL OU HEXODECIMAL
x = int (input('Digite um numero: ') )
print('Para qual sistema numerico você gostaria de converter?')
print('1 - BINARIO')
print('2 - OCTAL')
print('3 - HEXODECIMAL')
y = int (input('Qual sua escolha: ') )
if y == 1:
    print('O numero {} convertido para BINARIO é {}'.format(x, bin(x)[2:]))
elif y == 2:
    print('O numero {} convertido para OCTAL é {}'.format(x, oct(x)[2:]))
elif y == 3:
    print('O numero {} convertido para HEXODECIMAL é {}'.format(x, hex(x)[2:]))
else:
    print('Comando inexistente tente novamente')