dic = {'11':'Sao Paulo', '61':'Brasilia', '71':'Salvador', '21':'Rio de Janeiro',
       '32':'Juiz de Fora', '19':'Campinas', '27':'Vitoria', '31':'Belo Horizonte'}
ddd = str(input())
if ddd in dic:
    print(f'{dic[ddd]}')
else:
    print('DDD nao cadastrado')