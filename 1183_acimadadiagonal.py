op = str(input()).strip().lower()[0]
#criando matriz
matriz = []
for j in range(12):
    linha = [0] * 12
    matriz.append(linha)
#soma
soma = 0
vezes = 0
#lendo matriz
for i in range(12):
    for k in range(12):
        matriz[i][k] = float(input())
        if k > i:
            soma += matriz[i][k]
            vezes += 1
if op == 'm':
    print(f'{(soma/vezes):.1f}')
else:
    print(f'{soma:.1f}')