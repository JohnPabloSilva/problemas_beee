num = input().split(' ')
for i in range(0,3):
    num[i] = float(num[i])
num.sort(reverse=True)
if(num[0] < num[1] + num[2]):
    if num[0]**2 == num[1] ** 2 + num[2]**2:
        print('TRIANGULO RETANGULO')
    elif num[0]**2 >= num[1]**2 + num[2]**2:
        print('TRIANGULO OBTUSANGULO')
    else:
        print('TRIANGULO ACUTANGULO')
    if num[0] == num[1] == num[2]:
        print('TRIANGULO EQUILATERO')
    elif num[0] == num[1] or num[0] == num[2] or num[1] == num[2]:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
