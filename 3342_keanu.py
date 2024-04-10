ordem = int(input())
tabuleiro = []
for i in range(ordem):
    linha = ['Vazio'] * ordem
    tabuleiro.append(linha)

controle = 0
for linhas in range(ordem):
    for colunas in range(ordem):
        if controle % 2 == 0 and colunas % 2 == 1:
            tabuleiro[linhas][colunas] = 'Preto'
        elif controle % 2 == 1 and colunas % 2 == 1:
            tabuleiro[linhas][colunas] = 'Branco'

        if controle % 2 == 0 and colunas % 2 == 0:
            tabuleiro[linhas][colunas] = 'Branco'
        elif controle % 2 == 1 and colunas % 2 == 0:
            tabuleiro[linhas][colunas] = 'Preto'
    if linhas % 2 == 1:
        controle = 0
    else:
        controle = 1
casasp = 0
casasb = 0
for j in range(ordem):
    for k in range(ordem):
        if tabuleiro[j][k] == 'Preto':
            casasp += 1
        else:
            casasb += 1
print(f'{casasb} casas brancas e {casasp} casas pretas')