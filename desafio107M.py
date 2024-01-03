def dobro(n, formato=False):
    if formato == True:
        return f'R${n*2:.2f}'
    return n*2

def metade(n, formato=False):
    if formato == True:
        return f'R${n/2:.2f}'
    return n/2


def aumentar(n, porcentagem, formato=False):
    if formato == True:
        return f'R${n + (n * porcentagem/100):.2f}'
    return n + (n * porcentagem/100)


def diminuir(n, porcentagem, formato=False):
    if formato == True:
        return f'R${n - (n * porcentagem/100):.2f}'
    return n - (n * porcentagem/100)


def moeda(n):
    return f'R${n:.2f}'


def resumo(n, aumento, reducao):
    r = 'RESUMO DE VALOR'
    print('-' * (len(r) + 10))
    print(f'     {r}')
    print('-' * (len(r) + 10))
    print(f'{'Preco Analizado'}------{moeda(n)}')
    print(f'{'Dobro do preco'}-------{dobro(n, True)}')
    print(f'{'Metade do preco'}------{metade(n, True)}')
    print(f'{aumento}% de aumento-------{aumentar(n, aumento, True)}')
    print(f'{reducao}% de reducao-------{diminuir(n, reducao, True)}')
