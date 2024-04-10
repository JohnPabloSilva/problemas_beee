salario = float(input())
por = [0.08 , 0.18, 0.28]
aux = [2000, 1500, 4500]
if salario <=2000:
    print('Isento')
else:
    aux1 = 0
    for i in range(0, 3):  
        salario -= aux[i]
        print(salario)
        if salario <= 0:
            break
        else:
            aux1 = salario * por[i] + aux1
print(f'R$ {aux1:.2f}')
