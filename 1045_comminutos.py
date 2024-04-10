'''entre = input().split(' ')
horas = [int(entre[0]), int(entre[2])]
minutos = [int(entre[1]), int(entre[3])]
if horas[0] >= horas[1]:
    horas_totais = horas[1] - horas[0] + 24
else:
    horas_totais = horas[1] - horas[0]

if minutos[0] >= minutos[1] and horas[0] != horas[1]:
    minutos_totais = minutos[1] - minutos[0] + 60
    horas_totais -= 1
    if horas[0] + 1 == horas[1]:
        horas_totais = 0
    if minutos_totais >= 60:
        minutos_totais = minutos_totais % 60
elif minutos[0] > minutos[1] and horas[1] == horas[0]:
    minutos_totais = minutos[1] - minutos[0] + 60
    horas_totais -=1
else:
    minutos_totais = minutos[1] - minutos[0]
    if (horas[0] == horas[1] and minutos[0] < minutos[1]):
        horas_totais = 0

print(f'O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)')'''

#consegui reduzir 

enter = input().split(' ')
tempo = [int(enter[0])*60 + int(enter[1]), int(enter[2])*60 + int(enter[3])]
if tempo[0] >= tempo[1]:
    todo_tempo = tempo[1] - tempo[0] + 1440
else:
    todo_tempo = tempo[1] - tempo[0]
horas = todo_tempo // 60
minutos = todo_tempo % 60
print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

