s = 1
cont = 2
for i in range(3, 40, 2):
    s += i / cont
    cont *= 2
print(f'{s:.2f}')