# Concatenando string y convirtiendo a string.
# Este programa pide dos valores y realiza las operaciones básicas.

a = float(input("Ingresa un valor: "))
b = float(input("Ingresa otro valor: "))

suma = a + b
resta = a - b
producto = a * b
cociente = a / b

print( "La suma es: " + str(suma) + "\nLa resta es: " + str(resta) + "\nEl producto es: " + str(producto) + "\nEl cociente es: " + str(cociente))
print("\n¡Eso es todo, amigos!")

# Otra forma de hacer lo mismo.
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")