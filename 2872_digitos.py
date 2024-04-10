vezes = int(input())
for i in range(vezes):
    base, expo = map(int, input().split())
    num = str(base ** expo)
    print(len(num))