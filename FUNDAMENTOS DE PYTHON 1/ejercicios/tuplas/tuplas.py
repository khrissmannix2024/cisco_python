# Ejemplo 1: iterar en la tupla.
tuple_1 = (1, 2, 3)
for elem in tuple_1:
    print(elem)

# Ejemplo 2: Verificar si un elemento existe en la tupla.
tuple_2 = (1, 2, 3, 4)
print(5 in tuple_2)
print(5 not in tuple_2)

# Ejemplo 3: Ver cuantos elementos tiene.
tuple_3 = (1, 2, 3, 4)
print(len(tuple_3))
print(5 not in tuple_3)

# Ejemplo 4: Unirlas o multiplicarlas.
tuple_4 = tuple_1 + tuple_2
tuple_5 = tuple_3 * 2
print(tuple_4)
print(tuple_5)
