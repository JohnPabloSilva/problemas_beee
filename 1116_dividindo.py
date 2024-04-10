vezes = int(input())
cont = 0
while True:
    try:
        x, y = input().split(' ')
        x = int(x)
        y = int(y)
        if y == 0:
            print('divisao impossivel')
        else:
            print(f'{x/y:.1f}')
        cont += 1
        if cont == vezes:
            break
    except EOFError:
        break