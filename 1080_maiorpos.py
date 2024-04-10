for i in range(1, 101):
    num = int(input())
    if i == 1:
        maior = num
        pos = i
    elif num > maior:
        maior = num
        pos = i
print(f'{maior}')
print(f'{pos}')

i = 1
while True:
    if i > 100:
        break
    try:
        n = int(input())
        if i == 1:
            maior = n
        elif n > maior:
            maior = n
            pos = i
    except EOFError:
        break
    i += 1
print(f'{maior}')
print(f'{pos}')
