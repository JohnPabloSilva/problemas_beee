notas, total_n, provas, cont = input() , 0, 0, 0
while cont != len(notas):
    if cont < len(notas) - 1 and notas[cont+1] == '0':
        total_n += int(notas[cont:cont+2])
        cont += 2
    else:
        total_n += int(notas[cont])
        cont += 1
    provas += 1
print(f'{(total_n/provas):.2f}')
