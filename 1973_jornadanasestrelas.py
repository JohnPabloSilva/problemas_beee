sitios = int(input())
carneiros = list(map(int, input().split()))
rouba, ini, sitios_roub, car = 0, 0, [0] * sitios, sum(carneiros)
while 0 <= ini < sitios:
        aux = carneiros[ini]
        if carneiros[ini] > 0:
            carneiros[ini] -= 1
            rouba += 1
            sitios_roub[ini] = 1
        if aux % 2 == 0:
            ini -= 1
        else:
            ini += 1
print(f'{sum(sitios_roub)} {car - rouba}')