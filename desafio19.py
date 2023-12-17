#sorteio de aluno
a=('Aninha')
b='joao'
c='paulo'
d='maria'
import random
aluno = [a, b, c, d]

'''x=random.randint(1, 4)
if x == 1:
    print(a)
if x == 2:
    print(b)
if x == 3:
    print(c)
if x == 4:
    print(d)'''

y=random.choice(aluno)
print('O aluno escolhido foi {}'.format(y) )