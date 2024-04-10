money = int(input())
rest = money % 100
hu1ndred = money // 100
fifty = rest // 50
twenty = (rest % 50) // 20
ten = ((rest % 50) % 20) // 10
five = (((rest % 50) % 20) % 10) // 5
two = ((((rest % 50) % 20) % 10) % 5) // 2
one = ((((rest % 50) % 20) %10) % 5) % 2

print('{}'.format(money))
print('{} nota(s) de R$ 100, 00'.format(hu1ndred))
print('{} nota(s) de R$ 50, 00'.format(fifty))
print('{} nota(s) de R$ 20, 00'.format(twenty))
print('{} nota(s) de R$ 10, 00'.format(ten))
print('{} nota(s) de R$ 5, 00'.format(five))
print('{} nota(s) de R$ 2, 00'.format(two))
print('{} nota(s) de R$ 1, 00'.format(one))