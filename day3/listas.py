mi_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lista3 = mi_lista + lista2
lista4 = ["R", "Q", "C", "D", "E", "H", "Z", "G", "A"]

print(type(mi_lista))
print(len(mi_lista))
print(mi_lista[7:])
print(mi_lista+lista2)

# lista3[0] = "cosa"
# print(lista3)

lista3.append("cosa")
lista3.pop(0)
print(lista3)

lista4.sort()
print(lista4)
lista4.reverse()
print(lista4)
