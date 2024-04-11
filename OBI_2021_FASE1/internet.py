acumulado = 0
x = int(input())
n = int(input())

for i in range(n):
    m = int(input())
    acumulado += x - m

print(acumulado+x)
