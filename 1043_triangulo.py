n = input().split(' ')
num = []
for i in range(0,3):
    num.append(float(n[i]))
if (num[0] >= num[1] + num[2]) or (num[1] >= num[0] + num[2]) or (num[2] >= num[0] + num[1]):
    area = (num[0] + num[1]) * num[2] / 2
    print(f'Area = {area:.1f}')
else:
    peri = num[0] + num[1] + num[2]
    print(f'Perimetro = {peri:.1f}')