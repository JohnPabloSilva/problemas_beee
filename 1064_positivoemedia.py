positivos = 0 
total = 0
totaldig = 0
for i in range(1,7):
    n = float(input())
    if n > 0:
        positivos = positivos + 1
        total = total + n
        totaldig = totaldig + 1
media = total / totaldig
print(f'{positivos} valores positivos')
print(f'{media:.1f}')
