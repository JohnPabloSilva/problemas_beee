def encaixa (texto=''):
    """Esta função tenta criar uma lista de caracteres e espaços em uma lista de palavras e espaços"""
    lista = list(texto)
    frase = []
    palavra = ''
    espacos = ''
    umespaco = False
    for i in lista:
        if i.isspace() == False:
            if umespaco:
                frase.append(espacos)
                umespaco = False
            umapalavra = True
            espacos = ''
            palavra += i
        else:
            if umapalavra:
                frase.append(palavra)
                umapalavra = False
            umespaco = True
            palavra = ''
            espacos += ' '
    frase.append(palavra)
    return frase
            
vezes = int(input())
for k in range(vezes):
    carta = encaixa(str(input()))
    for j in range(len(carta)):
        if carta[j].isspace() == False:
            if carta[j][1:9].lower() == 'oulupukk':
                if carta[j][-1] == '.':
                    carta[j] = 'Joulupukki.'
                else:
                    carta[j] = 'Joulupukki'
    print(*carta,sep='')
                 