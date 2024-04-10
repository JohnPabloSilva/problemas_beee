jogadores, rodadas = map(int, input().split(' '))
pontos_j = [0] * jogadores
partidas = list(map(int, input().split(' ')))
matriz = []
for i in range(len(partidas)):
    if i == 0:
        matriz.append(partidas[:jogadores])
    elif i % jogadores == 0:
        matriz.append(partidas[i:i+jogadores])

for j in range(rodadas):
    for k in range(jogadores):
        pontos_j[k] += matriz[j][k]

for m in range(jogadores):
    if m == 0:
        maior_p = pontos_j[m]
        ind = m + 1
    elif pontos_j[m] >= maior_p:
        maior_p = pontos_j[m]
        ind = m + 1
print(ind)
print(matriz)
print(pontos_j)