vezes = int(input())
cont = 0
while True:
    try:
        cont += 1
        dias = 0
        comida = float(input())
        soma = 0
        while True:
            soma = comida / 2 + soma
            comida = comida / 2
            dias += 1
            if comida <= 1:
                break
        print(f'{dias} dias')
        if cont == vezes:
            break
    except EOFError:
        break