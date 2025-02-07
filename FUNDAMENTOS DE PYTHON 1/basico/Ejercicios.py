"""
Disena un algoritmo para calcular el área de un círculo dado su radio. (Recuerda
que el área de un círculo es π veces el cuadrado del radio.)
"""
print("### Calcula el área de un círcilo ###")
import math
pi = math.pi
a = float (input("Radio: "))
area = (a ** 2) * pi

print("El area del circulo es: ", area)
"""
Disena un algoritmo que calcule el IVA (16%) de un producto dado su precio de
venta sin IVA.
"""
print("### Calcula el precio con IVA (16%) de un producto dado sin IVA ####")
precio = float (input("Ingresa el precio del producto: "))
iva = (( precio * 16) / 100)

precioTotal = precio + iva
print("El precio con iva del producto ingresado es: ", precioTotal)

"""
¿Podemos llamar algoritmo a un procedimiento que escriba en una cinta de papel
todos los numeros decimales de π?
"""
print("""No. Al no ser un proceso finito, no puede llamarse algoritmo en forma clásica:
         Es un algoritmo si escribes un número finito de decimales de 𝜋.
         No es un algoritmo si intentas escribir infinitos decimales, ya que carece de finitud.""")