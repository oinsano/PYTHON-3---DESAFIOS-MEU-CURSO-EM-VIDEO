palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[p].upper()} temos: ', end='')
    for letra in palavras[p]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
            