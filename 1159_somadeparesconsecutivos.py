while True:
    try:
        num = int(input())
        if num == 0:
            break
        else:
            cont = 1
            soma = 0
            i = num
            while cont <= 5:
                if i % 2 == 0:
                    soma += i
                    cont += 1
                i += 1
            print(soma)
    except EOFError:
        break