while True:
    while True:
        n1 = float(input())
        if 0 <= n1 <=10:
            break
        else:
            print('nota invalida')
    while True:
        n2 = float(input())
        if 0.0 <= n2 <= 10.0:
            break
        else:
            print('nota invalida')
    media = (n1 + n2) / 2
    print(f'media = {media:.2f}')
    while True:
        print('novo calculo (1-sim 2-nao)')
        cont = int(input())
        if cont == 2 or cont == 1:
            break
    if cont == 2: 
        break