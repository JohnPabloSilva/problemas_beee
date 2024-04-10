money = float(input())
#cédulas
rest = money % 100
hun1dred = money //100
fifty = rest // 50
twenty = (rest % 50) // 20
ten = ((rest % 50) % 20) //10
five = (((rest % 50) % 20) % 10) // 5
two = ((((rest % 50 )% 20)% 10) % 5) // 2

#moedas
moedas = ((((rest % 50) % 20) % 10) % 5) % 2
one = moedas // 1.0
fiftycent = round((moedas % 1.0) // 0.5)
quarter = round(((moedas % 1.0) % 0.5)//0.25)
tencent = round((((moedas % 1.0) % 0.5) % 0.25) // 0.10)
fivecent = round(((((moedas % 1.0) % 0.5) % 0.25) % 0.10) // 0.05)
onecent = round((((((moedas % 1.0) % 0.5) % 0.25) % 0.10) % 0.05) , 2)
onecent = int(onecent / 0.01)

print('NOTAS:')
print('{:.0f} nota(s) de R$ 100.00'.format(hun1dred))
print('{:.0f} nota(s) de R$ 50.00'.format(fifty))
print('{:.0f} nota(s) de R$ 20.00'.format(twenty))
print('{:.0f} nota(s) de R$ 10.00'.format(ten))
print('{:.0f} nota(s) de R$ 5.00'.format(five))
print('{:.0f} nota(s) de R$ 2.00'.format(two))
print('MOEDAS:')
print('{:.0f} moeda(s) de R$ 1.00'.format(one))
print('{:.0f} moeda(s) de R$ 0.50'.format(fiftycent))
print('{:.0f} moeda(s) de R$ 0.25'.format(quarter))
print('{:.0f} moeda(s) de R$ 0.10'.format(tencent))
print('{:.0f} moeda(s) de R$ 0.05'.format(fivecent))
print('{:.0f} moeda(s) de R$ 0.01'.format(onecent))