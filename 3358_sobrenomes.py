vezes = int(input())
conso = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
for i in range(vezes):
    sobre = str(input())
    dific = False
    for k in range(len(sobre)-1):
        if (k!=0) and sobre[k].lower() in conso and sobre[k-1].lower() in conso and sobre[k+1].lower() in conso:
            dific = True
            break
    print(f'{sobre} nao eh facil') if dific else print(f'{sobre} eh facil')