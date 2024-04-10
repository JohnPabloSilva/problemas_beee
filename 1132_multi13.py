x = int(input())
y = int(input())
somanao13 = 0
if x > y:
    for cont in range(y, x+1):
        if cont % 13 != 0:
            somanao13 += cont
elif y > x:
    for cont in range(x, y+1):
        if cont % 13 != 0:
            somanao13 += cont
elif x == y:
    if x % 13 != 0:
        somanao13 += x
print(somanao13)