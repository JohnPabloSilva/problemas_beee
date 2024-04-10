frutas, totalk, totalkilos, cont = dict(), 0, 0, 1
vezes = int(input())
for i in range(vezes):
    preco = float(input())
    totalk += preco
    lista = list(input().split())
    print(len(lista))
    totalkilos += len(lista)
    frutas.update({cont: len(lista)})
    cont += 1
for k, l in frutas.items():
    print(f'day {k}: {l} kg')
print(f'{(totalkilos/vezes):.2f} kg by day')
print(f'R$ {(totalk/len(frutas)):.2f} by day')

    