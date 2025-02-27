# Aquí se puede ver lo estudiado en el curso, "lineas de código repetidas".

#print("Ingresa un valor: ")
#a = int(input())

#print("Ingresa un valor: ")
#b = int(input())

#print("Ingresa un valor: ")
#c = int(input())

def mensaje():
    valor = int(input("Ingresa un valor: "))
    if valor == 3:
        print("¡Correcto!")
#mensaje()
#mensaje()
#mensaje() # Se puede llamar cuantas veces sea necesario.

# Ahora intentaremos pasarle argumentos a la función definiendola con parámetros.
def mostrar_nombre(nombre):
    print("Tu nombre es: ", nombre)
#mostrar_nombre(input("Ingresa el nombre: ")) # Se puede usar input en la llamada.

# Parametros posicionales / mostrar en diferente orden los valores. Presentación en Hungría.
def introduction(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

#introduction("Luke", "Skywalker")
#introduction("Jesse", "Quick") # Si cambio el orden acá, se imprimirá en orden establecido.
#introduction("Clark", "Kent")

# Paso de argumentos de palabra clave.
def introduction2(first_name, last_name):
    print("Hola, mi nombre es", first_name, last_name)

#introduction2(first_name = "James", last_name = "Bond") # Acá la diferencia es que se especifica el valor asignandolo a la variable.
#introduction2(last_name = "Skywalker", first_name = "Luke")

def introduction3(first_name, last_name="Smith"):
     print("Hola, mi nombre es", first_name, last_name)

#introduction3("Edmundo")

def hi_all(name_1, name_2):
    print("Hola,", name_2)
    print("Hola,", name_1)

#hi_all("Sebastián", "Konrad")

def address(street, city, postal_code):
    print("Tu dirección es:", street,"St.,", city, postal_code)

s = input("Calle: ")
p_c = input("Código Postal: ")
c = input("Ciudad: ")
address(s, c, p_c)

