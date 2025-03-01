# Si queremos intercambiar el contenido de las variables pasando el contenido de "a" a "b" y viseversa.
# Se procede de la siguiente manera:

my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)

# Esa es una propiedad de Python, pero si quisieramos intercambiar los valores a 100 variables?
# Se puede usar un bucle for para ello.
my_list = [10, 1, 8, 3, 5]

# Declara la variable length y asigna la longitud de la lista
length = len(my_list)

# Intercambia los elementos
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)
