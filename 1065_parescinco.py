contepar = 0
for i in range(0,5):
    n = int(input())
    if ( n % 2 == 0):
        contepar = contepar + 1
print(f'{contepar} valores pares')