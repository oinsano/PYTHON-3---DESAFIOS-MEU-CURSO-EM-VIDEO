def voto(a):
    from datetime import date
    idade = date.today().year - a
    if 16 <= idade < 18 or idade >= 65:
        print(f'Com {idade} anos: Voto {'OPICIONAL'}')
    elif idade < 16:
        print(f'Com {idade} anos: Voto {'NEGADO'}')
    else:
        print(f'Com {idade} anos: Voto {'OBRIGATORIO'}')

nasc = int(input('Em que ano você nasceu? '))
voto(nasc)
