while True:
    try:
        reclama = int(input())
        print('vai ter copa!') if reclama == 0 else print('vai ter duas copas!')
    except EOFError:
        break