x = int(input())
impar = 0
i = 0
while impar < 6:
    n = x + i
    if n % 2 == 1:
        print(n)
        impar += 1
    i += 1