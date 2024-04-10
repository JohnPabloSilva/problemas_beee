while True:
    try:
        vezes = int(input())
        if vezes == 0:
            break
        else:
            for i in range(vezes):
                planeta, ano, tempo = input().split()
                if i == 0:
                    menor = int(ano) - int(tempo)
                    mais_a = planeta
                elif int(ano) - int(tempo) < menor:
                    menor = int(ano) - int(tempo)
                    mais_a = planeta
            print(mais_a)
    except EOFError:
        break