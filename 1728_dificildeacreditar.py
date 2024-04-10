while True:
    try:
        operacao = input()
        for i in range(len(operacao)):
            if operacao[i] == '+':
                a = (operacao[:i])
                break
        for k in range(len(operacao)):
            if operacao[k] == '=':
                b = (operacao[i+1:k])
                break
        c = (operacao[k+1:])
        aa, bb, cc = int(a[::-1]), int(b[::-1]), int(c[::-1])
        print(aa + bb == cc)
        if a==b==c=='0' and len(a) == 1 and len(b) == 1 and len(c) == 1:
            break
    except EOFError:
        break