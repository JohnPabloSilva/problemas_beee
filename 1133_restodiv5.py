x = int(input())
y = int(input())
if x > y:
    for cont in range (y , x):
        if cont % 5 == 2 or cont % 5 == 3:
            print(cont)
elif y > x:
    for cont in range (x, y):
        if cont % 5 == 2 or cont % 5 == 3:
            print(cont)
elif x == y and (x % 5 == 2 or x % 5 == 3) :
    print(x)
