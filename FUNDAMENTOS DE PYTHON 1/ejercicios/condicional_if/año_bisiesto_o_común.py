# Como seguramente sabrás, debido a algunas razones astronómicas,
# el año puede ser bisiesto o común. 
# Los primeros tienen una duración de 366 días, 
# mientras que los últimos tienen una duración de 365 días.

# Desde la introducción del calendario Gregoriano (en 1582), 
# se utiliza la siguiente regla para determinar el tipo de año:

# Si el número del año no es divisible entre cuatro, es un año común.
# de lo contrario, si el número del año no es divisible entre 100, es un año bisiesto.
# de lo contrario, si el número del año no es divisible entre 400, es un año común.
# de lo contrario, es un año bisiesto.

# El código debe mostrar uno de los dos mensajes posibles, 
# que son Año Bisiesto o Año Común, según el valor ingresado.

# Sería bueno verificar si el año ingresado cae en la era Gregoriana y emitir una advertencia 
# de lo contrario: No dentro del período del calendario Gregoriano. Consejo: utiliza los operadores != y %.

año = int(input("Ingrese el año para determinar si es bisisesto o común: "))

if año > 1582:
    if año % 4 != 0:
        print("Es un año común.")
    else:
        if año % 100 != 0:
            print("Es un año bisisesto.")
        else:
            if año % 400 != 0:
                print("Es un año común.")
            else:
                print("Es un año bisisesto.")
else:
    print("No dentro del período del calendario Gregoriano. ", año, " es antes de 1582.")