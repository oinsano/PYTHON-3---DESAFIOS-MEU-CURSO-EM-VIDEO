from random import randint
def sorteia(lista):
    s = 0
    print('Sorteando 5 valores da lista ', end='')
    for c in range(0, 5):
        num = randint(1, 10)
        print(num, end=' ')
        lista.append(num)
    print('Pronto!!')


def somapar(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {lista}, temos {s}')


lista = []
sorteia(lista)
somapar(lista)
