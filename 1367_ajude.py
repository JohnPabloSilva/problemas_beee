while True:
    try:
        vezes = int(input())
        if vezes == 0:
            break
        else:
            pontos_li, letra_li, incore, cont = list(), list(), list(), 0
            for i in range(vezes):
                letra, pontos, corein = input().split()
                if letra not in letra_li and corein == 'correct':
                    letra_li.append(letra)
                    pontos_li.append(int(pontos))
                elif corein == 'incorrect' and letra not in letra_li:
                    incore.append(letra)
            for k in letra_li:
                if k in incore:
                    cont += incore.count(k)
            pontos_totais = sum(pontos_li) + cont * 20
            print(len(letra_li), pontos_totais)
    except EOFError:
        break