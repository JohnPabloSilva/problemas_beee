vezes = int(input())
cont = 0
term = 0
while True:
    cont += 1
    if cont % 4 == 0:
        print('PUM')
        term += 1
    else:
        print(f'{cont}', end=' ')
    if term == vezes:
        break