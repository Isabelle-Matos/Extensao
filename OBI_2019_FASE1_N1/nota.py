B = int(input())
T = int(input())

area_metade = (70*160)/2
h = 70
if B > T:
    base_triangulo = B - T
else:
    base_triangulo = T - B

area_triangulo = (base_triangulo*h)/2

if B > T:
    area_quadrado = T * h
else:
    area_quadrado = B * h

f = area_triangulo + area_quadrado

if f > area_metade:
    print(1)
elif f < area_metade:
    print(2)
else:
    print(0)
