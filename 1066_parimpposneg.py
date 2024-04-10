contepar = 0
conteimpar = 0
contepos = 0
conteneg = 0

for i in range(0,5):
    n = int(input())
    if ( n % 2 == 0):
        contepar = contepar + 1
    elif (n % 2 == 1):
        conteimpar = conteimpar + 1
    if ( n > 0 ):
        contepos = contepos + 1
    elif( n < 0 ):
        conteneg = conteneg + 1

print(f'{contepar} valor(es) par(es)')
print(f'{conteimpar} valor(es) impar(es)')
print(f'{contepos} valor(es) positivo(s)')
print(f'{conteneg} valor(es) negativo(s)')