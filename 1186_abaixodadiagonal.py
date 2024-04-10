op = str(input()).strip().lower()[0]
matriz = [[] for i in range(12)]
soma, itens = 0 , 0
for j in range(12):
    for k in range(12):
        num = float(input())
        if j + k > 11:
            soma += num
            itens += 1
        matriz[j].append(num)
print(f'{soma:.1f}') if op == 's' else print(f'{(soma/itens):.1f}')