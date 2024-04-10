while True:
    try:
        churas = dict()
        vezes = int(input())
        for i in range(vezes):
            carne, data = input().split()
            churas.update({int(data): carne})
        churas = dict(sorted(churas.items()))
        mac = []
        for i in churas.values():
            if i not in mac:
                mac.append(i)
        print(*mac)
    except EOFError:
        break
