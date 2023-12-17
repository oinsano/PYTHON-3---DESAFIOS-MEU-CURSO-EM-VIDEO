n = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESEIS', 'DEZESSETE', 'DEZOTO', 'DEZENOVE', 'VINTE')
while True:
    while True:
        x = int (input('Digite um numero entre 0 e 20: '))
        if x >= 0 and x <= 20:
            break
        else:
            print('O numero digitado incorreto, digite um numero entre 0 e 20: ')
    print(f'Voê digitou o numero \033[0;30;41m{n[x]}\033[m')
    s = str (input('Deseja continuar? [S/N] ')).upper()
    if s == 'N':
        break