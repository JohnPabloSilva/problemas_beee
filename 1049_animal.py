ave = [{'carnivoro': 'aguia', 'onivoro': 'pomba'}]
mamifero = [{'onivoro': 'homem', 'herbivoro': 'vaca'}]

inseto = [{'hematofago':'pulga', 'herbivoro': 'lagarta'}]
anelideo = [{'hematofago':'sanguessuga', 'onivoro':'minhoca'}]

separa = str(input()).strip().lower()
ramifica = str(input()).strip().lower()
alimento = str(input()).strip().lower()
if separa == 'vertebrado':
    if ramifica == 'ave':
        print(ave[0][alimento])
    else:
        print(mamifero[0][alimento])
else:
    if ramifica == 'inseto':
        print(inseto[0][alimento])
    else:
        print(anelideo[0][alimento])

#Acho que dá pra reduzir, colocando as listas em outras listas



