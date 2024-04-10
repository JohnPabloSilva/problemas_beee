while True:
    try:
        op = str(input())
        for i in range(len(op)):
            if op[i] == '+':
                x = op[:i]
                break
        for k in range(len(op)):
            if op[k] == '=':
                y = op[i+1:k]
                break
        z = op[k+1:]
        if x.isalpha():
            print(int(z)-int(y))
        elif y.isalpha():
            print(int(z)-int(x))
        elif z.isalpha():
            print(int(x)+int(y))
    except EOFError:
        break