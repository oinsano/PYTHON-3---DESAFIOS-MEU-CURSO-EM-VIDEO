#calcular a hipotenusa
x=float(input('Insira o numero de um cateto: ') )
y=float(input('insira o outro catetto: ') )
import math
print('A hipotenusa é {:.2f}'.format(math.hypot( x, y)))