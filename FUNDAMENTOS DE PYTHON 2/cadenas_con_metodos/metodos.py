
nombre = "khrístopher es mi nombre"
apellido1 = "castro es mi Apellido"
apellido2 = "arias es mi Segundo Apellido"
edad = "Tengo 27 años"
nombre2 = "Khrístopher"


# 1- Método capitalize()

# Si el primer carácter dentro de la cadena es una letra 
# (nota: el primer carácter es el elemento con un índice igual a 0, no es el primer carácter visible), 
# se convertirá a mayúsculas.
# Todas las letras restantes de la cadena se convertirán a minúsculas.
#print(nombre.capitalize()) # Se debe tener en cuenta que el método no guarda la conversión. 
#print(nombre) # Esto imprimirá la cadena sin aplicar el método.
#print(apellido1.capitalize()) 
#print(apellido2.capitalize())
#inicial_mayuscula = nombre.capitalize()  # Para guardar la conversión se debe asignar a una variable.
#print(inicial_mayuscula)



# 2- Método center()

# Centra una cadena agregando espacios antes y después.
# El número de espacios es introducido por el usuario y también es permitido cambiar los espacios por un caracter.
#print(nombre.center(30)) # El número de espacios debe ser mayor al número de carateres de la cadena, sino imprime la cadena.
#print(apellido1.center(30,"-")) # Aquí se puede ver mejor cómo funciona.
# Nota: Hay otros dos método ljust() y rjust()
#print(nombre.ljust(60, "*")) # Alinea a la izquierda
#print(apellido2.rjust(60, "+")) # Alinea a la derecha



# 3- Método endswith()

# El método endswith() comprueba si la cadena dada termina con el argumento especificado 
# y devuelve True(verdadero) o False(falso), dependiendo del resultado.
#print(nombre.endswith("bre"))
#if nombre.endswith("khri"):
#    print("Correcto")
#else:
#    print("Incorrecto")



# 4- Método find()

# Busca una subcadena y devuelve el índice de la primera aparición de esta subcadena.
# No genera un error para un argumento que contiene una subcadena inexistente (devuelve -1 en dicho caso).
# Funciona solo con cadenas.
# No se debe buscar un solo caracter con este método.
#print(nombre.find("opher"))

# 4.1- El método .rfind() 

# En Python busca la última aparición de una subcadena dentro de una cadena dada
#  y devuelve el índice donde se encuentra
# cadena.rfind(subcadena, inicio, fin)
#print("tau tau tau".rfind("ta")) # La última aparición es en el índice 8, por lo que imprime 8



# 5- Método isalnum()

#  Comprueba si la cadena contiene solo dígitos o caracteres alfabéticos (letras) 
# y devuelve True (verdadero) o False (falso) de acuerdo al resultado.
# print(nombre2.isalnum())
# print(edad.isalnum())



# 6- Método isalpha()

# El método .isalpha() en Python verifica si una cadena contiene solo letras del alfabeto 
# (sin números, espacios ni caracteres especiales).
#print(nombre2.isalpha())
#print("mañana".isalpha())   # True (incluye "ñ")
#print("canción".isalpha())  # True (incluye "ó")
#print("año2024".isalpha())  # False (contiene números)
#print("hola mundo".isalpha())  # False (contiene un espacio)



# 7- Método isdigit()

#  El método isdigit() busca solo dígitos, cualquier otra cosa produce False (falso) como resultado.
#print("Hola Mundo 2025".isdigit()) # False
#print("12345".isdigit()) # True



# 8- Método islower()

# El método islower() es una variante de isalpha(), solo acepta letras minúsculas.
#print(nombre.islower()) # True
#print(nombre2.islower()) # False


# 8.1- Método lower()

# Genera una copia de una cadena, reemplaza todas las letras mayúsculas con sus equivalentes en minúsculas.
#print(nombre2.lower())  



# 9- Método isspace()

# Identifica espacios en blanco.
#print(' \n '.isspace()) # True
#print(" ".isspace()) # True
#print("mooo mooo mooo".isspace()) # False



# 10- Metodo isupper()

# Es la versión en mayúscula de islower(), se concentra solo en letras mayúsculas.
#print("Moooo".isupper())
#print('moooo'.isupper())
#print('MOOOO'.isupper())



# 11- Método join()

# El método realiza una unión y espera un argumento del tipo lista; 
# se debe asegurar que todos los elementos de la lista sean cadenas.
# Todos los elementos de la lista serán unidos en una sola cadena pero,
# la cadena desde la que se ha invocado el método será utilizada como separador, puesta entre las cadenas.
# La cadena recién creada se devuelve como resultado.
#print(" * ".join(["omicron", "pi", "rho"])) # Coloca la cadena inicial entre cada unión de los valores de la lista.



# 12- Método lstrip()

# El método sin parámetros lstrip() devuelve una cadena recién creada 
# formada a partir de la original eliminando todos los espacios en blanco iniciales.
#print("[" + " tau ".lstrip() + "]") # Solo elimina los espacios en blanco iniciales.
# Si se le agrega un parámetro, se elimina de la cadena el parámetro ingresado.
#print("www.cisco.com".lstrip("w.")) # Da cisco.com
# Nota: Solo elimina si encuentra el argumento al inicio, si se encuentra con un valor diferente al
# del argumento, entonces se detiene el método. Por eso imprime el punto en cisco.com

# 12.1- Método rstrip()

# Hacen casi lo mismo que el método lstrip, pero afecta el lado opuesto de la cadena.
#print("[" + " upsilon ".rstrip() + "]") # Solo elimina los espacios en blanco finales.
#print("cisco.com".rstrip(".com")) # Devuelve cis



# 13- Método replace()

# El método replace() con dos parámetros devuelve una copia de la cadena original
# en la que todas las apariciones del primer argumento han sido reemplazadas por el segundo argumento.
#print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # Imprime 'www.pythoninstitute.org'
#print("This is it!".replace("is", "are", 1)) # El numero determina los reemplazos, sino reemplaza todas las apariciones.
#print("Apple juice".replace("juice", ""))



# 14- Método split()

# El método split() divide la cadena y crea una lista de todas las subcadenas detectadas.
# El método asume que las subcadenas están delimitadas por espacios en blanco, 
# los espacios no participan en la operación y no se copian en la lista resultante.
#print("phi       chi\npsi".split())



# 15- Método startswith()

# El método startswith() es un espejo del método endswith(), 
# comprueba si una cadena dada comienza con la subcadena especificada.
#print("omega".startswith("meg"))
#print("omega".startswith("om"))



# 16- Método strip()

# El método strip() combina los efectos causados por rstrip() y lstrip(), 
# crea una nueva cadena que carece de todos los espacios en blanco iniciales y finales.
#print("[" + "   aleph   ".strip() + "]") # Quita los espacios



# 17- Método swapcase()

# Crea una nueva cadena intercambiando todas las letras por mayúsculas o minúsculas 
# dentro de la cadena original: los caracteres en mayúscula se convierten en minúsculas y viceversa.
#print(nombre2.swapcase())



# 18- Método title()

# Cambia la primera letra de cada palabra a mayúsculas, convirtiendo todas las demás a minúsculas.
#print(nombre.title())



# 19- Método upper()

# Hace una copia de la cadena de origen, reemplaza todas las letras minúsculas con sus equivalentes en mayúsculas, 
# y devuelve la cadena como resultado.
#print(nombre.upper())