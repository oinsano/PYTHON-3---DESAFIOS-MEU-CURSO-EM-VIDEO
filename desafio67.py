from time import sleep
print('-' * 10, ' TABUADA ', '-' * 10)
while True:
    n = int (input ('Quer ver a tabuada de qual numero: '))
    if n < 0:
        print('*********ENCERRANDO PROGRAMA*********')
        sleep(2)
        break
    for x in range(1, 11):
        print(f'{n} x {x:2} = {n*x:4}')
    print('-*' * 20)
