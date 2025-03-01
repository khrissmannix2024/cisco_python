#Procesador de Números.
# El programa recibe una cadena con dígitos como caractres para funcionar,
# luego los separa los convierte a valóres numéricos float y los suma y alamacena.

line = input("Ingresa una línea de números, sepáralos con espacios: ") # Recibe la acdena de entrada.
strings = line.split() # Separa la cadena en una lista.
total = 0 # inicia la variable que guardará la suma.
try: # Se utiliza este condicional para que no se genere error en la conversión de cadena a float.
    for substr in strings: # Itera entre los valores de la lista
        total += float(substr) # Asigna a total el valor convertido a float y la suma de la cantidad anterior.
    print("El total es:", total) # Imprime el resultado de la suma cuando termina el bucle.
except ValueError: # Aquí es mejor ser específico en cuanto al tipo de error que maneja la excepción.
    print(substr, "no es un numero.") # Si se ingresa una cadena con caracter diferente a numérico, se manda una excepción.
except Exception as e: # Si hay un error de diferente tipo se maneja en esta parte.
    print("Ocurrió un error inesperado:", e)
    # Esto es solo para manejar correctamente las excepciones.