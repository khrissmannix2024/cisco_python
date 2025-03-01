# Vamos a intentar importar un módulo que está una carpeta arriba de la actual.

#import sys
#import os

#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # Agregar la carpeta 'main' al sys.path
#from new_modulo import funcion_new_modulo_main
#print(funcion_new_modulo_main())



from ..new_modulo import funcion_new_modulo_main  # Importación relativa

print(funcion_new_modulo_main())
