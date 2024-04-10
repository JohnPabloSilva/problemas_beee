jogo = input()
if jogo.count('O') >= 2 or jogo.count('X') == 3:
    print('?')
elif jogo[2] == jogo[1] or jogo[0] == jogo[1]:
    print('Alice')
else:
    print('*')
