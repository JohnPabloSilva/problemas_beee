n = int(input())
x = 0
dentro = 0
fora = 0
while x < n:
    test = int(input())
    if 10 <= test <= 20:
        dentro += 1
    else:
        fora += 1
    x += 1
print(f'{dentro} in')
print(f'{fora} out')