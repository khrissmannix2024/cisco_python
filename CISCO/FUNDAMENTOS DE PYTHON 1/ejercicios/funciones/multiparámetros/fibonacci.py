# Dice esta serie que:
# El primer elemento de la secuencia es igual a uno.
# El segundo elemento también es igual a uno.
# Cada número después de ellos son la suman de los dos números anteriores.

def fibonacci(n):
    primero = 0 # El primer elemento se inicia en 0 para que al empezar la serie de 1.
    segundo = 1 # Esto en 1 por la misma razón anterior.
    for i in range(1, n + 1): # Se itera de 1 a n.
        print(primero, segundo, sep="-",end=" ") # Se pone aquí el print para que imprima 1 y 0 en el primer bucle.
        # Acá se empieza a asignar nuevos valores a la variables.
        primero = primero + segundo # El primero más el segundo se guarda en primero.
        segundo = primero + segundo # El nuevo valor de primero se suma al segundo y se guarda en segundo.
    return "Fin"
        
print(fibonacci(9))
# Cuando una función se invoca a si misma, se le conoce como recursividad.
# Implementación recursiva de la función factorial.

def factorial(n):
    if n == 1:    # El caso base (condición de terminación).
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) # 4 * 3 * 2 * 1 = 24