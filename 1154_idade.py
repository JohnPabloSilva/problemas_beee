total_idade = 0
n_idades = 0
while True:
    try:
        n = int(input())
        if n < 0:
            break
        else:
            total_idade += n
            n_idades += 1
    except EOFError:
        break
print(f'{total_idade/n_idades:.2f}')