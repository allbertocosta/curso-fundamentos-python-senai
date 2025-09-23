#Lista em lista:
# row = []
# for i in range (8):
#     row.append("Alberto")
# print(row)

# Lista de compreensão
# row = ["SENAI" for i in range (8)]
# print(row)

# Potencia
# 
# quad = [x ** 2 for x in range(11)]
# print (quad)
# par = [x for x in quad if x % 2 == 0 ]
# print(par)


#Exemplo 1
# matriz = []
# for i in range(8):
#     row = ["SENAI" for i in range (8)]
#     matriz.append(row)
#     print(row)
#     print("***"*50)
#     print(matriz)


# Exemplo 2
matriz =[["Alberto" for i in range(3)] for j in range (5)]
print(matriz)

