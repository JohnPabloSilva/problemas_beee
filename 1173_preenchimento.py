n = int(input())
vetor = [0] * 10
vetor[0] = n
print(f'N[0] = {n}')
for i in range(1, 10):
    vetor[i] = vetor[i-1] * 2
    print(f'N[{i}] = {vetor[i]}')