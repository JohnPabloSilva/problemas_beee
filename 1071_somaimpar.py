number = []
for i in range(1,3):
    n = int(input())
    number.append(n)
sumip = 0
number.sort()
for i in range(number[0]+1, number[1]):
    if i % 2 == 1:
        sumip += i
print(sumip)