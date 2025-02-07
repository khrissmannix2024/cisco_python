# Instrucción return

def happy_new_year(wishes = True):
    print("Tres...")
    print("Dos...")
    print("Uno...")
    if not wishes:
        return # Si estra a esta parte, return detiene la función.

    print("¡Feliz año nuevo!")

#happy_new_year(True)
#happy_new_year(False)

# return con expresiones.

def boring_function():
    print("Ahora sí.")
    return 123 # Guarada la expresión (En este caso el valor) y para la función.
    print("Hola mundo") # Esto no se ejecuta ya que el return está antes.

x = boring_function()

print("La función boring_function ha devuelto su resultado. Es:", x)

