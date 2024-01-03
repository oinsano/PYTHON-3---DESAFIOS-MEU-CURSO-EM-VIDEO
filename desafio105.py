def notas(* n, b=False):
    lista = {}
    lista['total'] = len(n)
    lista['maior'] = max(n)
    lista['menor'] = min(n)
    lista['media'] = sum(n)/len(n)
    if b:
        if lista['media'] < 6:
            lista['situacao'] = ruim
        elif lista['media'] > 6 and me < 7:
            lista['situacao'] = razoavel
        elif lista['media'] > 7:
            lista['situacao'] = boa
    return lista


res = notas(5, 7, 6, b=True)
print(res)