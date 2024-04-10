while True:
    try:
        frase = str(input()).lower().strip()
        if frase == '*':
            break
        else:
            lista = list(frase.split())
            ver = True
            pri = lista[0][0]
            for i in lista:
                if i[0] != pri:
                    ver = False
            print('Y') if ver else print('N')     
    except EOFError:
        break