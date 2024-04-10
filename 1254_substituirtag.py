def encontra_tag(codigoexe, errado, certo):
    tagcriadas, aberto = [], False
    for i in range(len(codigoexe)):
        if codigoexe[i] == '<':
            aberto = True
            posi = i + 1
        elif codigo[i] == '>' and aberto:
            posf = i
            if errado in codigoexe[posi:posf]:
                trecho = codigoexe[posi:posf]
                trecho_c = trecho.replace(errado, certo)
                codigoexe = codigoexe.replace(trecho, trecho_c)
            aberto = False
    return codigoexe                         
        





while True:
    try:
        tag = str(input())
        correta = str(input())
        codigo = (input())
    
        nova = encontra_tag(codigo, tag, correta)
        print(nova)
    except EOFError:
        break