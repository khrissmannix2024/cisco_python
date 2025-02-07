 # Así se importa un módulo que básicamente es código reutilizable. Como funciones, pero en una escala mayor.
import math
print(math.sin(math.pi/2))

# De este otro modo se importa solo la entidad que se desea utilizar. Así evitas cargar todo el archivo del módulo.

print(math.sin(math.pi/2))


print(dir(math)) # Devuelve la lsita de entidades del módulo.

# Usa una función del módulo math.
print(math.factorial(4))