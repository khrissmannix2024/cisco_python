# El dispositivo registra la temperatura del aire cada hora y lo hace durante todo el mes. 
# Esto te da un total de 24 × 31 = 744 valores.

# Luego tomarás la decisión arbitraria de que las filas registrarán las lecturas cada hora exactamente
# (por lo que la fila tendrá 24 elementos) y cada una de las filas se asignará a un día del mes 
# (supongamos que cada mes tiene 31 días, por lo que necesita 31 filas).

# Puede suponer que se actualiza automáticamente utilizando agentes de hardware especiales. 
# Lo que tienes que hacer es esperar a que la matriz se llene con las mediciones.

# Ahora es el momento de determinar la temperatura promedio mensual del mediodía. 
# Suma las 31 lecturas registradas al mediodía y divida la suma por 31. 
# Puedes suponer que la temperatura de medianoche se almacena primero.

import random

# Simular temperaturas entre -10°C y 40°C
temps = [[random.uniform(-10.0, 40.0) for h in range(24)] for d in range(31)]


total = 0.0

for day in temps:
    total += day[11]

average = total / 31

print("Temperatura promedio al mediodía:", round(average,2))

# Encontrar la temperatira más alta del mes.
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("La temperatura más alta fue:", round(highest,2))

# Contar los días en que la tempertaura al medio día fue de al menos 20°C.
hot_days = 0

for day in temps:
    if day[11] > 20.0:
        hot_days += 1

print(hot_days, "fueron los días calurosos.")

