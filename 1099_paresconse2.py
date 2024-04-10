n = int(input())
i = 1
while True:
    if i == n:
        break
    try:
        somaimpar = 0
        x, y = input().split(' ')
        x = int(x)
        y = int(y)
        if x == y:
            somaimpar = 0
        elif x > y:
            for i in range(y+1, x):
                if i % 2 == 1:
                    somaimpar += i
        elif x < y:
            for i in range(x+1, y):
                if i % 2 == 1:
                    somaimpar += i
        print(somaimpar)
    except EOFError:
        break
    i += 1