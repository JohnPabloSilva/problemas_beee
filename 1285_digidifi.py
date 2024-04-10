while True:
    try:
        inicio, fim = input().split(' ')
        fim = int(fim)
        inicio = int(inicio)
        casas = 0
        for i in range(inicio, fim+1):
            func = True
            num = list(str(i))
            for k in num:
                if num.count(k) >= 2:
                    func = False
                    break
            if func:
                casas += 1
        print(casas)
    except EOFError:
        break
