# Realizamos una prueba para determinar que sin especificar el tipo de dato en el input
# el programa siempre traerá valores tipo cadena con los cuales no se puede realizar
# operaciones matemáticas.

anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)

# Para que funcione el programa anterior se debe cambiar el tipo de dato del input
# de la siguiente manera:

anything = float(input("Ingresa un número:"))
something = anything ** 2.0
print(anything, "al cuadrado es", something)