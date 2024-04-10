while True:
    try:
        a, b = input().split(' ')
        a = int(a)
        b = int(b)
        soma = 0
        if a <= 0 or b <= 0:
            break
        else:
            if a > b:
                for i in range(b, a+1):
                    print(f'{i}',end=' ')
                    soma += i
            elif b > a:
                for i in range(a, b+1):
                    print(f'{i}',end=' ')
                    soma += i
            print(f'Sum={soma}')         
    except EOFError:
        break