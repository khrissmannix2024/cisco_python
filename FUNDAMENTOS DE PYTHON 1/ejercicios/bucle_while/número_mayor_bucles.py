# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = input("Introduce un número o escribe 'stop' para detener: ")

while number != "stop":
    number = int(number)
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = input("Introduce un número o escribe 'stop' para detener: ")

# Imprime el número más grande.
print("El número más grande es:", largest_number)

