vezes = int(input())
for i in range(vezes):
    lista, palavra = [], ''
    frase = list(input().lower())
    frase_set = set(frase)
    maior = 0
    while ' ' in frase_set:
        frase_set.remove(' ')
    for n in frase_set:
        if frase.count(n) == maior:
            lista.append(n)
        elif frase.count(n) > maior:
            maior = frase.count(n)
            lista.clear()
            lista.append(n)
    lista.sort()
    for i in lista:
        palavra += i
    print(palavra)