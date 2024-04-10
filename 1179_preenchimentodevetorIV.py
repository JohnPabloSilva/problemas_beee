par = []
imp = []
for i in range(15):
    num = int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        imp.append(num)
    if len(par) == 5:
        for pos, ele in enumerate(par):
            print(f'par[{pos}] = {ele}')
        par = []
    if len(imp) == 5:
        for pos, ele in enumerate(imp):
            print(f'impar[{pos}] = {ele}')
        imp = []
#imprimindo o resto
for j in range(len(imp)):
    print(f'impar[{j}] = {imp[j]}')
for k in range(len(par)):
    print(f'par[{k}] = {par[k]}')
