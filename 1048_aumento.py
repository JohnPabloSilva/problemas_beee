salario = float(input())
if salario <= 400:
    novo_salario = salario + (salario / 100 * 15)
    reajuste = salario / 100 * 15
    por = 15
elif 400 > salario <=800:
    novo_salario = salario + (salario / 100 * 12)
    reajuste = salario / 100 * 12
    por = 12
elif 800 < salario <= 1200:
    novo_salario = salario + (salario / 100 * 10)
    reajuste = salario / 100 * 10
    por = 10
elif 1200 < salario <= 2000:
    novo_salario = salario + (salario / 100 * 7) 
    reajuste = salario / 100 * 7
    por = 7
else:
    novo_salario = salario + (salario / 100 * 4)
    reajuste = salario / 100 * 4
    por = 4
print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {por} %')