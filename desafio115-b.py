from pack.modulo import *
from pack.arquivo import *

arq = ('EXERCICIO 115 - BIBLIOTECA.txt')
if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema' ])
    if resposta == 1:
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema . . . Até logo.')
        break
    else:
        print('\033[31mERRO! Digite uma opcao valida\033[m')