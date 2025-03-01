#La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado,
#expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59).
#El resultado debe ser mostrado en la consola.
#Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.
#No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida -
#lo más importante es que el código produzca una salida correcta acorde a la entrada dada.
#Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito.

hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

minutos_totales = mins + (hour * 60) + dura #convierto las horas a minutos y le sumo los minutos más la duración del evento.
hora_final_evento = minutos_totales // 60 # calculo las horas totales.
minutos_final_evento = minutos_totales % 60 # calculo los minutos restantes de las horas totales.
hora_definitiva = hora_final_evento % 12 # Hago que las horas no sean mayores a 24 0 12 dependiendo el reloj.

if hora_definitiva == 0: # si el evento termina a las 12 es posible que se muestre 0 horas devido a que no existe se cambia a 12
    hora_definitiva = 12 # esto pasa porque mod siempre devuelve 0 cuando el dividendo es un múltiplo exacto del divisor.
#Esto ocurre porque el módulo no tiene ninguna noción de "relojes" o "horarios". Simplemente sigue las reglas matemáticas

print("El evento termina a las ", hora_definitiva, " horas y ", minutos_final_evento, " minutos.")

#El código anterior se puede abreviar usando las mismas variables para guardar nuevos valores en ellas.
# Por ejemplo:
# mins = mins + (hour * 60) + dura
# hour = mins // 60
# mins = mins % 60
# hour = hour % 12
