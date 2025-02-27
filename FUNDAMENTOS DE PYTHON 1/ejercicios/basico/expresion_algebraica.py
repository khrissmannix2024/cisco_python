#Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x,
#e imprime el valor de la variable llamada y. 
# Tu tarea es completar el código para evaluar la siguiente expresión:
#3x3 - 2x2 + 3x - 1 aqui es 3 por x elevado a la 3 y los otros igual.
#El resultado debe ser asignado a y.

x =  input("ingresa un número: ")
x = float(x)
y = (3 * (x ** 3)) - (2 * (x ** 2)) + (3 * x) - 1
print("y =", y)