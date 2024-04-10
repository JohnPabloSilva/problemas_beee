name = str(input())
salary_fixed = float(input())
sales = float(input())
salary_bonus = (15*sales/100)+salary_fixed
print('TOTAL = R$ {:.2f}'.format(salary_bonus))