posi = 0
for i in range(0,6):
    val = float(input())
    if val > 0:
        posi = posi + 1
print('{} valores positivos'.format(posi))