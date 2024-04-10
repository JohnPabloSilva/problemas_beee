consu = int(input())
agenda = []
for i in range(consu):
    inicio, fim = input().split(' ')
    linha = [int(inicio), int(fim)]    
    agenda.append(linha)

print(agenda)
dispo = 0
for linhas in range(consu):
    for colunas in range(0, 2):
        if linhas > 0:
            
print(dispo)
