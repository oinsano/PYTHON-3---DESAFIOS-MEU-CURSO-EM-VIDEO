def ficha(a, b):
    if a in '':
        a ='<DESCONHECIDO>'
    if b in '':
        b = 0
    print(f'O jogador {a} fez {b} gol(s) no campeonato.')


jogagor = str(input('Nome do Jogador: '))
g = str(input('Numero de gol(s): '))
print('=-' * 20)
ficha(jogagor, gols)
