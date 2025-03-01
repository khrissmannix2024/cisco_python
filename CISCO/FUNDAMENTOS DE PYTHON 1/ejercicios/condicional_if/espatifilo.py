# Escribe un programa que utilice el concepto de ejecución condicional, 
# tome una cadena como entrada y que:

# imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!"
# en la pantalla si la cadena ingresada es "ESPATIFILO" (mayúsculas)
# imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
# imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. 
# Nota: [entrada] es la cadena que se toma como entrada.

entrada = input("Ingresa el enunciado: ")
if entrada == "ESPATIFILO":
    print("Sí - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
else:
    if entrada == "espatifilo":
        print("No, ¡quiero un gran Espatifilo!")
    else:
        print("¡Espatifilo!, ¡No ",entrada, "!")