def quadrado_cubo(x):
    cont = 1
    for i in range(x):
        resultado = cont, cont**2, cont**3
        print(*resultado)
        cont+=1

num = int(input())
quadrado_cubo(num)

'''vezes = int(input())
cont = 1
while True:
    try:
        print(f'{cont**1} {cont**2} {cont**3}')
        cont += 1
        if cont == vezes + 1:
            break
    except EOFError:
        break
print('-'*15)
for i in range(1, vezes+1):
    print(f'{i} {i**2} {i**3}')'''