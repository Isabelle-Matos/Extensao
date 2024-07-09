n = int(input())
string = input()
anterior = ''
aux = []
count = 1

for i in string:
    
    if i == anterior:
        count += 1
    else:
        if anterior != '':
            aux.append(f'{count} {anterior}')
            print(aux)
        anterior = i
        print("valor dentro do else ", anterior)
        count = 1

aux.append(f'{count} {anterior}')
resposta = " ".join(aux)
print(resposta)


## ----------- Utilizando dicionários considerando que o problema deseja saber a quantidade total de valores na string ------------
# n = int(input())
# dicionario = {}
# string = input()
# lista = []
# count = 1
# for i in string:
#     if i in dicionario:
#         valor = dicionario[i]
#         valor+= 1
#         dicionario[i] = valor
#     else:
#         dicionario[i] = count

# print(dicionario)

# # Acessando as chaves no nosso dicionário
# for i in dicionario:
#     print({i})

# # Acessando as chaves e valores no nosso dicionário
# for chave, valor in dicionario.items():
#     print(f'Chave: {chave} Valor: {valor}')

# dicionario.items()

# # Acessando valores no dicionário
# for valor in dicionario.values():
#     print(f'Valor: {valor}')

# # Acessando chaves no dicionario
# for chaves in dicionario.keys():
#     print(f'Chave: {chaves}')