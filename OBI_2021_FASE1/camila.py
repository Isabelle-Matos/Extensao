A = input()
B = input()
C = input()

lista = [A, B, C]
# Odenação de vetores



for i in range(len(lista)):
    for j in range(i, len(lista)):
        if lista[i] > lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

print(lista[1])