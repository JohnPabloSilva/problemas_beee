while True:
    try:
        maos = list(input().split())
        A, B, C = maos[0], maos[1], maos[2]
        if A == B == C:
            print('*')
        elif A == B:
            print('C')
        elif A == C:
            print('B')
        elif C == B:
            print('A')
    except EOFError:
        break