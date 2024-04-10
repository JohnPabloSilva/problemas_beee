enter = input().split(' ')
numbers = list()
for i in range(0,3):
    numbers.append(int(enter[i]))
numbers.sort()
for i in range(0,3):
    print(numbers[i])
print()
for i in range(0,3):
    print(enter[i])