vezes = int(input())
relatorio, setcordenadas = [], set()
for i in range(vezes):
    coordenadas = str(input())
    relatorio.append(coordenadas)
setcordenadas = set(relatorio)
print('1') if len(setcordenadas) < len(relatorio) else print('0')