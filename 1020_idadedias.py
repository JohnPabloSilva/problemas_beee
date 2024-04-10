idade = int(input())
x = idade % 365
ano = idade // 365
mes = x // 30
dia = (x % 30)
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))