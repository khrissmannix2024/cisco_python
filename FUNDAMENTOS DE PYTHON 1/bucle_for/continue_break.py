# Vamos a mirar cómo funciona el break y el continue en los bucles.

# break - ejemplo

print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break # En este caso al llegar a 3 se sale del bucle.
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo

print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue # En este caso se salta en valor que cumple la condición y el bucle sigue.
    print("Dentro del bucle.", i)
print("Fuera del bucle.")
