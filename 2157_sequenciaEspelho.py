vezes = int(input())
for i in range(vezes):
    inicio, fim = map(int, input().split(' '))
    vazio = ''
    for k in range(inicio, fim+1):
        vazio += str(k)
    vazio += vazio[::-1]
    print(vazio)