x = float (input('Digite sua primeira nota: '))
y = float (input('Digite a outra nota: '))
m = (x + y) / 2
if m < 5:
    print('\033[31mALUNO REPROVADO\033[m')
elif m > 4.9 and m < 7:
    print('\033[33mALUNO EM RECUPERACÃO\033[m')
else:
    print('\033[32mALUNO APROVADO\033[m')