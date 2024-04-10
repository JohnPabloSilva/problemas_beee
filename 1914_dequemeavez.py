vezes = int(input())
for i in range(vezes):
    j1, op1, j2, op2 = input().split()
    jogj1, jogj2 = map(int, input().split())
    if (op1.upper() == 'PAR' and (jogj1+jogj2)%2==0) or (op1.upper()=='IMPAR' and (jogj1+jogj2)%2==1):
        print(j1)
    elif (op2.upper()=='PAR' and (jogj1+jogj2)%2==0) or (op2.upper()=='IMPAR' and (jogj1+jogj2)%2==1):
        print(j2)

