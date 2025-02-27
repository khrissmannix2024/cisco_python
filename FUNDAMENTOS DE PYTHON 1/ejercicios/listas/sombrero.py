# Había una vez un sombrero. El sombrero no contenía conejo, 
# sino una lista de cinco números: 1, 2, 3, 4, y 5.
# Tu tarea es:
# Escribir una línea de código que solicite al usuario que reemplace el número central en la lista
#  con un número entero ingresado por el usuario (Paso 1)
# Escribir una línea de código que elimine el último elemento de la lista (Paso 2)
# Escribir una línea de código que imprima la longitud de la lista existente (Paso 3).

sombrero = [1,2,3,4,5]
nuevo_numero_central = int(input("""Ingrese el número nuevo para reemplazarlo en la lista 
por el número central: """))
sombrero[2] = nuevo_numero_central
del sombrero[-1]
print("La lista es: ", sombrero, " la longitud es: ", len(sombrero))

# Agregando elementos al final de la lista.
sombrero.append(39)
print("La nueva lista es: ", sombrero)

# Agregando elementos a lugares específicos de la lista.
sombrero.insert(2,000)
print("La nueva lista es: ", sombrero)


# Insertando datos con for.
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.insert(0, i + 1) # Los número se insertan en orden inverso, 
                             # ya que se van corriendo a la derecha en cada interacción.
print(my_list) # [5,4,3,2,1]

# Otra función de las listas.
my_list = [10, 1, 8, 3, 5]
total = 0

for i in my_list: # La variable i toma el valor de cada elemento de la listas en cada interración.
    total += i   # Luego suma y asigna a total el valor.
# En este caso la interacción es igual al número de valores que haya en la lista y simultaneamente la i toma el valor en interacción.

print(total)