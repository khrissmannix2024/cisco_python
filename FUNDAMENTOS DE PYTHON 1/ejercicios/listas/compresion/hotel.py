# Imagina un hotel con 3 edificios de 15 pisos y 20 habitaciones por piso.
import random

rooms = [[[random.choice([True, False]) for h in range(20)] for p in range(15) ] for e in range(3)]

# Todas las habitaciones están desocupadas.
# Ahora ya puedes reservar una habitación para dos recién casados: 
# en el segundo edificio, en el décimo piso, habitación 14:

#rooms[1][9][13] = True

# y desocupar el segundo cuarto en el quinto piso ubicado en el primer edificio:
#rooms[0][4][1] = False

# Verifica si hay disponibilidad en el piso 15 del tercer edificio:
vacancy = 0

for room_number in range(20):
    if not rooms[2][14][room_number]:
        vacancy += 1
print(vacancy)


# Modificamos esto para comprobar el commit -m