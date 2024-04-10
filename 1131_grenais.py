grenais = 0
empates = 0
interna = 0
gremiof = 0
while True:
    try:
        golinter, golgrem = input().split(' ')
        golinter = int(golinter)
        golgrem = int(golgrem)
        if golinter > golgrem:
            interna += 1
        elif golgrem > golinter:
            gremiof += 1
        else:
            empates += 1
        grenais += 1
    except EOFError:
        break
    print('Novo grenal (1-sim 2-nao)')
    resp = int(input())
    if resp == 2:
        break
print(f'{grenais} grenais')
print(f'Inter:{interna}')
print(f'Gremio:{gremiof}')
print(f'Empates:{empates}')
if interna > gremiof:
    print(f'Inter venceu mais')
elif gremiof > interna:
    print(f'Gremio vencei mais')
else:
    print('Nao houve vencedor')