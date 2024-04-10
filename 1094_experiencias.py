vezes = int(input())
total = 0
coelho = 0
ratos = 0
sapos = 0
for i in range(vezes):
    quant, animal = input().split(' ')
    quant = int(quant)
    if animal.lower() == 'c':
        coelho += quant
    elif animal.lower() == 's':
        sapos += quant
    elif animal.lower() == 'r':
        ratos += quant
    total += quant

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelho}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {(coelho*100)/total:.2f} %')
print(f'Percentual de ratos: {(ratos * 100)/total:.2f} %')
print(f'Percentual de sapos: {(sapos*100)/total:.2f} %')