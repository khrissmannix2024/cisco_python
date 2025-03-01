# Cifrado César.
#text = input("Ingresa tu mensaje: ") # Recibe una cadena.
#cipher = '' # Almacenará el cifrado.
#for char in text: # Recorre los caracteres de la cadena.
#    if not char.isalpha(): # Conprueba si el caracter es una letra.
#        continue # Si no es una letra, continua.
#    char = char.upper() # Convierte cada caracter a mayúscula.
#    code = ord(char) + 1 # Almacena cada caracter en su conversión a ASCII.
#    if code > ord('Z'): # # Comprueba que el caracter sea 'Z'.
#        code = ord('A') # Si es 'Z' asigana el valor de 'A' a la variable code.
#    cipher += chr(code) # Guarda cada caracter iterado en la variable cipher.

#print(cipher) # Imprime el resultado.

# Mejoraré el código para que guarde los caracteres especiales.

text = input("Ingrese su mensaje: ")
cipher = ""
for char in text:
    if char.isalpha():
        char = char.upper()
        code = ord(char) + 1
        if code > ord("Z"):
            code = ord("A")
        cipher += chr(code)
    else:
        cipher += char

print(cipher)
# Ese código funciona mejor, pero en caso de que haya un una entrada con una letra con acento (á,é,í,ó,ú)
# el resultado de la conversión del caracter será siempre la letra 'A', ya que los caracteres con acento
# siempre serán mayores que Z en ASCII.