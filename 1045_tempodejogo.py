time = input().split(' ')
begin = int(time[0])
end = int(time[1])
if begin >= end:
    duration = end - begin + 24
else:
    duration = end - begin
print(f'O JOGO DUROU {duration} HORA(S)')