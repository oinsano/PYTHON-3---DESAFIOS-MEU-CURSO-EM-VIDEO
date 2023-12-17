from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {n}')
for c in range(0, 5):
    if c == 0:
        M = m = n[c]
    if m > n[c]:
        m = n[c]
    if M < n[c]:
        M = n[c]
print(f'O maior valor foi {M}') # maior valor
print(f'O menor valor foi {m}') # menor valor

print(f'{max(n)}')
print(f'{min(n)}')