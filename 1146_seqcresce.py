while True:
    try:
        n = int(input())
        if n == 0:
            break
        else:
            for i in range(1, n+1):
                if i == n:
                    print(i)
                else:
                    print(i,end=' ')
    except EOFError:
        break