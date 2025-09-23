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
quad = [x ** 2 for x in range(11)]
print (quad)
par = [x for x in quad if x % 2 == 0 ]
print(par)