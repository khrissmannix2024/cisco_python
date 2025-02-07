# Tu tarea es muy simple aquí: escribe un programa que use un bucle for para 
# "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, 
# el programa debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!"

#mississippi = 1

#while mississippi != 6:
#    print("Mississippi ", mississippi)
#    mississippi += 1

#print("¡Listos o no, ahí voy!")
# Era con for y lo hice con while

import time  # Importa el módulo time

for i in range(1, 6):
    print("Mississippi ", i)
    time.sleep(1)  # Pausa el programa por 1 segundo

print("¡Listos o no, ahí voy!")
