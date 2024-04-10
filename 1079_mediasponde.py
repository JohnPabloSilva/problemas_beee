vezes = int(input())
cont = 0
while True:
    try:
        n1, n2, n3 = input().split(' ')
        media = (float(n1)*2 + float(n2)*3 + float(n3)*5) /10
        print(f'{media:.1f}')
        cont += 1
        if cont == vezes:
            break
    except EOFError:
        break