notas = list()
n = input().split(' ')
for i in range(0,4):
    notas.append(float(n[i]))

media = (notas[0] * 2 + notas[1] * 3 + notas[2] * 4 + notas[3] * 1) / 10

if media >= 7.0:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5.0:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
elif 5.0 <= media < 6.9:
    n = float(input())
    notas.append(n)
    mediafinal = (media + notas[4]) / 2
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {notas[4]:.1f}')
    if (mediafinal >= 5.0):
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {mediafinal:.1f}')
