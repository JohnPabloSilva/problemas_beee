while True:
    try:
        frase = list(input().lower().split())
        cont, aux, ali = 0, frase[0][0], 0  
        for i in range(1, len(frase)):
            if frase[i][0] == aux:
                cont += 1
            elif frase[i][0] != aux:
                aux = frase[i][0]
                if cont != 0:
                    ali += 1
                    cont = 0
        if cont != 0:
            ali += 1
        print(ali)
    except EOFError:
        break