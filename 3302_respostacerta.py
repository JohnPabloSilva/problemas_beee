tamanho = int(input())
resp = dict()
for i in range(1, tamanho+1):
    num = int(input())
    resp.update({i: num})
for j, k in resp.items():
    print(f'resposta {j}: {k}')