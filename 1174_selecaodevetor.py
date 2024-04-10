vetor = [0] * 100
for i in range(100):
    vetor[i] = float(input())
for pos, ele in enumerate(vetor):
    if ele <= 10:
        print(f'A[{pos}] = {ele:.1f}')
