print('* ' * 10 , 'LOJA VAGABUNDA', ' *' * 10)
s = i = c = 0
bb = ''
while True:
    c += 1
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$'))
    s += preco
    if c == 1 or b > preco:
        b = preco
        bb = produto
    while True:
        x = str (input('Quer continuar? [S/N]: ')).upper().strip()
        if x in 'SN':
            break
    if preco > 1000:
        i += 1
    if x == 'N':
        break
print('-' * 5, 'FIM DA COMPRA', '-' * 5)
print(f'O total gasto na compra foi R${s:.2f}')
print(f'Temos {i} produtos custando mais de R$1000,00')
print(f'O produto mais barato foi {bb} que custa R${b:.2f}')
