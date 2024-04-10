caso = 1
while True:
    try:
        num = int(input())
        lista = [0]
        if num == 0:
            print(f'Caso {caso}: 1 numero')
            print('0')
        else:
            aux = 0
            while lista.count(num) != num:
                aux += 1
                for k in range(aux):
                    lista.append(aux)
            print(f'Caso {caso}: {len(lista)} numeros')
            for k in range(0, len(lista)):
                if k == len(lista) - 1:
                    print(lista[k])
                else:
                    print(lista[k],end=' ')   
        print()
        caso += 1
    except EOFError:
        break