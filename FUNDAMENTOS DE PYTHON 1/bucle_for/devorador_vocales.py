# Tu programa debe:

# pedir al usuario que ingrese una palabra.
# utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas;
#  hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
# utiliza la ejecución condicional y la instrucción continue 
# para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
# imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada

palabra = input("Ingrese una palabra: ")

palabra = palabra.upper()
# Se puede poner una variable que almacene una lista:
# vocales = ["A","E","I","O","U"]
consonantes= ""
for i in palabra:
    if i in "AEIOU":
        continue
    consonantes = consonantes + i

print(consonantes)