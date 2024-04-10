vezes = int(input())
for i in range(vezes):
    codigo = list(input())
    palavr, eletra = '', False
    for j in codigo:
        if j.isalpha() and eletra == False:
            palavr += j
            eletra = True
        elif j == '·':
            eletra = False
    print(palavr)