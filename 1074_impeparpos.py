vezes = int(input())
cont = 0
while True:
    try:
        x = int(input())
        if x % 2 == 0 and x > 0:
            print('EVEN POSITIVE')
        elif x % 2 == 1 and x > 0:
            print('ODD POSITIVE')
        elif x % 2 == 0 and x < 0:
            print('EVEN NEGATIVE')
        elif x % 2 == 1 and x < 0:
            print('ODD NEGATIVE')
        else:
            print('NULL')
        cont += 1
        if cont == vezes:
            break
    except EOFError:
        break