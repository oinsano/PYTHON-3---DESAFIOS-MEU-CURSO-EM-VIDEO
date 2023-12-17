times = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Fluminense', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print('=-=-' * 20)
print(len(times)) #quantidade na tupla
print('=-=-' * 20)
print(f'A lista de times no brasileirao é: {times}') #tupla
print('=-=-' * 20)
print(f'Os 5 primeiros colocados sao: {times[:5]}') #5 primeiros
print('=-=-' * 20)
print(f'Os lanternas sao: {times[-4:]}') # 4 ultimos
print('=-=-' * 20)
print(f'A ordem alfabetica dos times: {sorted(times)}')   # ordem alfabetica
print('=-=-' * 20)
# que posicao ta o fortaleza?
print(f'O Fortaleza esta na {times.index("Fortaleza") + 1}')
print('=-=-' * 20)
