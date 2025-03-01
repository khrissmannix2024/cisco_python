# Creamos una lista y realizamos algunas operaciones básica sobre ella como un CRUD
# Las listas están implícitamente enumeradas de 0 a x-1 donde x es el último valor de la lista de izquierda a derecha.
# Se usan corchetes para delimitar. Se pueden escribir sub listas dentro de otras listas.

lista = [1,2,3,4,5,6] # En este caso el 1 tiene el índice 0, el 2 el índice 1,..., el 6 el índice 5.
print("Contenido de la lista: ", lista)

lista[0] = 111 # Se modifica el valor en la posición 0. De 1 a 111.
print("La lista modificada con el nuevo escalar es: ", lista)

lista[1] = lista[4] # Y ahora queremos copiar el valor del quinto elemento al segundo elemento.
print("La nueva lista es: ", lista)

# Imprimir la longitud de la lista.
print("La longitud de la lista es: ", len(lista))

# Eliminando elemntos de la lista.
del lista[1]
print("La nueva lista es: ", lista, " longitud: ", len(lista))
