#  Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

def numero_primo():
    numero = int(input("Ingresa el número para determinar si es primo: "))
    
    if numero < 2:
        print("Números menores que 2 no son primos.")
        return f"{numero} no es un primo."
    
    for n in range(2, int(numero ** 0.5) + 1):
        if numero % n == 0:
            return f"{numero} no es un primo"
        
    return f"{numero} es un número primo."

print(numero_primo())
