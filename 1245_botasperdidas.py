while True:
    try:
        vezes = int(input())
        botas_d, botas_e, cont = list(), list(), 0
        for k in range(vezes):
            tamanho, pe = input().split()
            if pe == 'E':
                botas_e.append(tamanho)
            elif pe == 'D':
                botas_d.append(tamanho)
        botas_e_set = set(botas_e)
        botas_d_set = set(botas_d)
        if len(botas_d_set) >= len(botas_e_set):
            menor = (botas_e_set)
        else:
            menor = (botas_d_set)
        for i in menor:
            if botas_e.count(i) >= botas_d.count(i):
                cont += botas_d.count(i)
            else:
                cont += botas_e.count(i)
        print(cont)  
    except EOFError:
        break