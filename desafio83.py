x = list()
i = str (input('Digite uma expressao: '))
for s in i:
    if s == '(':
        x.append(s)
    elif s == ')':
        if len(x) > 0:
            x.pop()
        else:
            x.append(')')
if len(x) == 0:
    print('Expressao valida!!!')
else:
    print('Expressao INVALIDA.')
