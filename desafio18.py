#mostrar um angulo qualquer e dizer o seno, cosseno e tangente
import math
x=float(input('Digite um angulo: '))
s=(math.sin(math.radians(x)))
c=(math.cos(math.radians(x)))
t=(math.tan(math.radians(x)))
print('Esse é o seno {:.2f}, cosseno {:.2f}, e a tangente {:.2f} do angulo {:.2f}'.format(s, c, t, x))