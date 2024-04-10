nome = str(input())
dia1, mes1, ano1 = input().split('/')
dia2, mes2, ano2 = input().split('/')
if dia1 == dia2 and mes1 == mes2:
    print('Feliz aniversario!')

dias_Ae = int(dia1) + int(mes1) * 30
dias_De = int(dia2) + int(mes2) * 30
idade = int(ano1) - int (ano2)
if dias_Ae < dias_De:
    idade -= 1

print(f'Voce tem {idade} anos {nome}.')
