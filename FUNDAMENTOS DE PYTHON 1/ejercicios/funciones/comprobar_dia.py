# La idea principal de la función es calcular el número de días transcurridos desde el 1 de enero
# hasta la fecha que le pases, como por ejemplo 2000-12-31.

# Para lograr esto, la función tiene dos partes clave:

# Acumular los días de todos los meses anteriores al mes que se está consultando.
# Sumar el día específico del mes que se está verificando.

def is_year_leap(year): # Comprueba si el año es bisisesto.
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    if year < 1582 or month < 1 or month > 12: # Comprueba si el mes está en el rango y el año.
        return None
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Se especifica en orden la cantidad de días que tiene el mes.
    res  = days[month - 1] # Resta 1 al mes ya que cuenta de 0 - 11. Ejemolo: mes 2 sería marzo menos 1 = febrero.
    if month == 2 and is_year_leap(year): # Comprueba que el año sea visiesto en cuyo caso cambia el valor de res a 29 para el mes 2.
        res = 29
    return res

def day_of_year(year, month, day):
    days = 0
    for m in range(1, month): # Itera del mes 1 al mes ingresado.
        md = days_in_month(year, m) # Cuenta los días del mes en el que se encuentra el bucle (número de la iteracción).
        if md == None:
            return None
        days += md # Acumular los días de todos los meses anteriores al mes que se está consultando.
    md = days_in_month(year, month) # Cuenta los días del més que se está verificando.
    if day >= 1 and day <= md:
        return days + day # Sumar el día específico del mes que se está verificando.
    else:
        return None

print(day_of_year(2001, 3, 3))