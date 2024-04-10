def binario (x):
    """Tranforma o elemento recebido no parâmetro x no mesmo número em formato binário"""
    #como juntaremos vários 0 e 1 em um elemento, a string será usada para tornar isso mais fácil
    bin = ''
    #a divisão na "receita" é feita várias vezes pois é necessário que o resto da divisão seja 1 ou 0
    while x > 1:
        bin += str(x%2)
        x = x // 2
    #caso ainda exista 1 ou 0 em x
    bin += str(x)
    #por definição os algarismos da "receita" são invertidas
    bin = bin[::-1]
    return bin

#programa principal
vezes = int(input())
for i in range(vezes):
    num = int(input())
    num_trocado = binario(num)
    print(num_trocado.count('1'))