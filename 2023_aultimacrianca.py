lista, lista_v = [], []
while True:
    try:
        nome = str(input())
        lista.append(nome.lower())
        lista_v.append(nome)
    except EOFError:
        break
lista.sort()
for j in lista_v:
    if j == lista[-1]:
        print(j)
        break