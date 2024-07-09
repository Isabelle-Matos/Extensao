# n = int(input())

# matriz = []

# for i in range(n):
#     lista = input()
#     matriz.append([char for char in lista])

# for i in range(n):
#     print("".join(map(str, matriz[i])))

# for i in range(n):
#     lista = [int(x) for x in input().split()]
#     matriz.append(lista)

# for i in range(n):
#     print(*matriz[i])

def encontrou(lista, num):
    for i in lista:
        if i == num:
            return 1
    return 0

lista = [int(x) for x in input().split()]
resposta = encontrou(lista, 3)

if resposta == 1:
    print("Numero foi encontrado")
else:
    print("Nao foi possível encontrar o número")