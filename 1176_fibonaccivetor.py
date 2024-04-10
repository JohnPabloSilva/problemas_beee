n = int(input())
for i in range(n):
    ate = int(input())
    ant1 = 0
    ant2 = 1
    prox = 0
    if ate == 0:
        print(f'Fib({ate}) = {ant1}')
    else:
        for j in range(ate):
            prox = ant1 + ant2
            ant2= ant1
            ant1 = prox 
            if j+1 == ate:
                print(f'Fib({ate}) = {prox}')