alcool = 0
gasosa = 0
diesel = 0
while True:
    x = int(input())
    if 1 <= x <= 4:
        if x == 4:
            break
        elif x == 1:
            alcool += 1
        elif x == 2:
            gasosa += 1
        elif x == 3:
            diesel += 1
print('MUITO OBRIGADO')
print(f'Alcool: {alcool}')
print(f'Gasolina: {gasosa}')
print(f'Diesel: {diesel}')