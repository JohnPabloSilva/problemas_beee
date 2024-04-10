pontos = input().split(' ')
x = float(pontos[0])
y = float(pontos[1])
if ( x > 0):
    if ( y > 0):
        print('Q1')
    elif (y == 0):
        print('Eixo X')
    else:
        print('Q4')
elif (x < 0):
    if (y > 0):
        print('Q2')
    elif( y == 0):
        print('Eixo X')
    else:
        print('Q3')
elif (x == 0) and (y == 0):
    print('Origem')
else:
    print('Eixo Y')