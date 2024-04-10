alunos, comps, queimados, semcom = input().split(' ')
alunos = int(alunos)
comps = int(comps)
queimados = int(queimados)
semcom = int(semcom)

inu = queimados + semcom + 1 
sala = [0] * comps

cont = 0
while cont < inu:
    if cont >= len(sala):
        break
    else:
        if sala[cont] == 0:
            sala[cont] = 1
            cont += 1 
print(sala)
util = sala.count(0)
if util >= alunos:
    print('Igor feliz!')
else:
    if queimados > semcom // 2:
        print('Caio, a culpa eh sua!')
    else:
        print('Igor bolado!')