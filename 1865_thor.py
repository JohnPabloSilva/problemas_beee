digno = ['Thor' , '50']
vezes = int(input())
for i in range(vezes):
    nome, forca = input().split(' ')
    print('Y') if nome ==  digno[0] else print('N')