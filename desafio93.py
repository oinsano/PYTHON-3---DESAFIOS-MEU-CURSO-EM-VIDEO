jogo = {}
jogo['nome'] = str(input('Nome do Jogador: '))
jogo['partidas'] = int(input(f'Quantas partidas {jogo['nome']} jogou?  '))
gol = []
t = 0
for c in range(1, jogo['partidas'] + 1):
      x = int(input(f'Quantos gols na partida {c}? '))
      gol.append(x)
      t += x
jogo['gols'] = gol
jogo['total'] = t
print('-='*30)
print(jogo)
print('-='*30)
for k, v in jogo.items():
    print(f'O campo {k} tem {v}')
print('-='*30)
print(f'O jogador {jogo['nome']} jogou {jogo['partidas']} partidas.')
for i, v in enumerate(jogo['gols']):
    print(f'    => Na partida {i + 1} marcou {v} gols')
print(f'Marcou um total de {jogo['total']} gols')
print('-='*30)