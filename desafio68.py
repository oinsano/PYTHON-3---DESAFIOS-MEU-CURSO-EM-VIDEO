from random import randint
print('*' * 10, 'JOGO PAR OU IMPAR', '*' * 10)
c = 0
while True:
    m = randint(1, 10)
    print(m)
    print('*' * 50)
    u = int (input('Digite um valor: '))
    e = str (input('Par ou impar? [P/I]: ').strip().upper())
    j = m + u
    if e == 'P':
        if j % 2 == 0:
            print(f'Você jogou = {u}, Computador = {m}, TOTAL = {j} - Deu PAR Você GANHOU')
            print('Vamos jogar mais uma vez')
            print('*' * 50)
        else:
            print(f'Você jogou = {u}, Computador = {m}, TOTAL = {j} - Deu IMPAR você PERDEU')
            print(f'GAME OVER - Você venceu {c} vezes')
            break
    if e == 'I':
        if j % 2 == 0:
            print(f'Você jogou = {u}, Computador = {m}, TOTAL = {j} - Deu PAR você PERDEU')
            print(f'GAME OVER - Você venceu {c} vezes')
            break
        else:
            print(f'Você jogou = {u}, Computador = {m}, TOTAL = {j} - Deu IMPAR Você GANHOU')
            print('Vamos jogar mais uma vez')
            print('*' * 50)
    c += 1
