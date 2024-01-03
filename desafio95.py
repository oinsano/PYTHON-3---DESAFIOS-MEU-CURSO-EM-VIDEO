geral = []
jogo = {}
while True:
    jogo.clear
    jogo['nome'] = str(input('Nome do Jogador: '))
    lo = int(input(f'Quantas partidas {jogo['nome']} jogou?  '))
    gol = []
    t = 0
    for c in range(1, lo + 1):
          x = int(input(f'Quantos gols na partida {c}? '))
          gol.append(x)
          t += x
    jogo['gols'] = gol
    jogo['total'] = t
    geral.append(jogo.copy())
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(geral)
print('-=' * 50)
print(f'{"cod":<4}{"nome":<15}{"gols":<15}{"Total":^5}')
print('-='*30)
for k, v in enumerate(geral):
    print(f'{k+1:<4}', end='')
    for j in v.values():
        print(f'{str(j):<15}', end='')
    print()
print('-='*30)
while True:
    b = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if b == 999:
        break
    if b > len(geral):
        print('ERRO - Tente novamente')
    else:
        print(f'Levantamento do Jogador {geral[b-1]['nome']}')
        for i, v in enumerate(geral[b-1]['gols']):
               print(f'    => Na partida {i + 1} marcou {v} gols')
print('>>> VOLTE SEMPRE <<<')
