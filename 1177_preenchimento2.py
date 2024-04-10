n = int(input())
vetor = [0] * 1000
for i in range(1000): 
    if i % n == 0:
        aux = 0
    vetor[i] = aux
    print(f'N[{i}] = {vetor[aux]}')
    aux += 1