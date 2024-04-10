bolas = int(input())
galho = int(input())
resto = int(galho / 2) - bolas
if resto > 0:
    print(f'Faltam {resto} bolinha(s)')
else:
    print(f'Amelia tem todas bolinhas!')