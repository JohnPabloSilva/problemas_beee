dia_1 = input()
x,y,z = input().split(':')
dia_2 = input()
a,b,c = input().split(':')
x,y,z = int(x),int(y),int(z)
a,b,c = int(a),int(b),int(c)
dia_1 = int(dia_1[-1])
dia_2 = int(dia_2[-1])

total = (dia_2*60*60*24 + a*60*60 + b*60 + c) - (dia_1*60*60*24 + x*60*60 + y*60 + z)
dia = total//86400 
resto_dia = total%86400 
hora = resto_dia//3600
resto_hora = resto_dia%3600
min_a = resto_hora//60
seg = resto_hora%60
print(f'{dia} dia(s)\n{hora} hora(s)\n{min_a} minuto(s)\n{seg} segundo(s)')
