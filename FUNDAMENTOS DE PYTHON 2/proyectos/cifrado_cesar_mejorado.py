#El cifrado César original cambia cada carácter por otro
#a se convierte en b, z se convierte en a, y así sucesivamente. 
#Hagámoslo un poco más difícil y permitamos que el valor desplazado provenga del rango 1..25.

#Además, dejemos que el código conserve las mayúsculas y minúsculas 
#(las minúsculas permanecerán en minúsculas) y todos los caracteres no alfabéticos deben permanecer intactos.

#Tu tarea es escribir un programa el cual:

#Le pida al usuario una línea de texto para encriptar.
#Le pida al usuario un valor de cambio (un número entero del rango 1..25, nota: debes obligar al usuario a ingresar un valor de cambio válido (¡no te rindas y no dejes que los datos incorrectos te engañen!).
#Imprime el texto codificado.