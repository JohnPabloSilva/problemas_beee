code1, number1, price1 = input().split(' ')
code1 = int(code1)
number1 = int(number1)
price1 = float(price1)
code2, number2, price2 = input().split(' ')
code2 = int(code2)
number2 = int(number2)
price2 = float(price2)
total = price1 * number1 + price2 * number2
print('VALOR A PAGAR: R$ {:.2f}'.format(total))

#dá pra fazer usando um for