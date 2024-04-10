while True:
    try:
        rodadas = int(input())
        if rodadas == 0:
            break
        else:
            john, mary = 0, 0
            lista = list(map(int,input().split()))
            for i in lista:
                if i == 1:
                    john += 1
                else:
                    mary += 1
            print(f'Mary won {mary} times and John won {john} times')             
    except EOFError:
        break