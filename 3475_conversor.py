entrada = input().strip().lower()
digito = {'zero': 0, 'um': 1, 'dois':2, 'tres': 3, 'quatro': 4,
          'cinco': 5, 'seis':6, 'sete':7, 'oito':8, 'nove':9}

algaris = {0:'zero', 1:'um', 2: 'dois', 3:'tres', 4:'quatro',
           5:'cinco', 6:'seis', 7:'sete', 8:'oito', 9:'nove'}
if entrada.isalpha():
    print(digito[entrada])
elif entrada.isdigit():
    print(algaris[int(entrada)])