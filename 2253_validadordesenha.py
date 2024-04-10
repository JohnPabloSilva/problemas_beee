while True:
    try:
        senha = str(input())
        maior = False
        menor = False
        numer = False
        espaco = False
        if 6 <=len(senha) <= 32: 
            for i in senha:
                if i.isalnum():
                    if i.isupper():
                        maior = True
                    if i.islower():
                        menor = True
                    if i.isdigit():
                        numer = True
                else:
                    espaco = True
            if maior and menor and numer and espaco == False:
                print('Senha valida.')
            else:
                print('Senha invalida.')
        else:
            print('Senha invalida.')     
    except EOFError:
        break