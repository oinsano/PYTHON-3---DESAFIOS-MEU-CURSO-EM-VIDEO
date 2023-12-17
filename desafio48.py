a = 0
for c in range(1, 501, 2):
    if c % 2 == 1 and c % 3 == 0:
        a = a + c
print(a)