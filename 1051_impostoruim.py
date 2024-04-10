sal = float(input())
if sal <= 2000:
    print('Isento') 
else:
    if sal > 2000:
        impos = (sal - 2000) * 0.08
    if 3000 <= sal <= 4500:
        impos = (sal - 3000) * 0.18 + 80
    if sal > 4500:
        impos = (sal - 4500) *0.28 + 350
    print(f'R$ {impos:.2f}')

#Na verdade isso tá melhor do que a solução da lista