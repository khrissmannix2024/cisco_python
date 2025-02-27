import sys
import os

ruta_zip = os.path.abspath("C:/Users/Khris/OneDrive/Escritorio/Python/CISCO/FUNDAMENTOS DE PYTHON 2/modulo_zip/paquete.zip")

if not os.path.exists(ruta_zip):
    print("El archivo paquete.zip no existe.")
    sys.exit(1)

sys.path.insert(0, ruta_zip)  # Agregar el ZIP al path

try:
    import paquete.module  # Importar el módulo dentro del paquete
    print(paquete.module.zip_funcion())  # Llamar la función del módulo
except ModuleNotFoundError as e:
    print("Error al importar el módulo desde el ZIP:", e)
except Exception as e:
    print("Otro error ocurrió:", e)

# Este método funciona, pero importar módulos de zip no es muy optimo, excepto para casos específicos.
# Lo mejor es descomprimir los paquetes y usar la forma tradicional.
# VSC sigue marcando problema en la línea 13, a pesar de que al ejecutar el código funciona.