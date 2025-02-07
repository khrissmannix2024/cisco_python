# La pirámide se apila de acuerdo con un principio simple: 
# cada capa inferior contiene un bloque más que la capa superior.
# Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, 
# y generar la altura de la pirámide que se puede construir utilizando estos bloques.

# Nota: La altura se mide por el número de capas completas - 
# si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, 
# terminan su trabajo inmediatamente.
#altura = 0
#cantidad_bloques = int(input("Ingrese la cantidad de bloques disponibles: "))
#bloques_usados = 0
#while cantidad_bloques >= bloques_usados + 1:
#    bloques_usados += 1
#    cantidad_bloques -= bloques_usados
#    altura += 1
#print("La altura es de ", altura, " bloques.")

# Otro programa igual que reparte caramelos aumentando 1 cada vez.
#niños_con_caramelos = 0
#cantidad_de_caramelos = int(input("Ingresa la cantidad de caramelos disponibles: "))
#caramelos_por_niño = 0


#while cantidad_de_caramelos >= caramelos_por_niño + 1:
#    caramelos_por_niño += 1
#    cantidad_de_caramelos -= caramelos_por_niño
#    niños_con_caramelos += 1
# Resultados finales
#print("La cantidad de niños con caramelos es:", niños_con_caramelos)
#print("Los caramelos restantes son:", cantidad_de_caramelos)

# otra forma de hacer lo mismo.
cantidad_de_tareas = int(input("Ingresa la cantidad total de tareas disponibles: "))
trabajadores_atendidos = 0

# Bucle for con cálculo acumulativo
for tareas_por_trabajador in range(1, cantidad_de_tareas + 1):
    if cantidad_de_tareas >= tareas_por_trabajador:
        cantidad_de_tareas -= tareas_por_trabajador
        trabajadores_atendidos += 1
    else:
        break  # Si no quedan suficientes tareas, salir del bucle

# Resultados finales
print("La cantidad de trabajadores atendidos es:", trabajadores_atendidos)
print("Las tareas restantes son:", cantidad_de_tareas)
