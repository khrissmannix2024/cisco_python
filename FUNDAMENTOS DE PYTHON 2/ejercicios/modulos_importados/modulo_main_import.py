# Importar módulo desde una carpeta que está en esta misma ruta.

import main.new_modulo # Llamando el módulo
print(main.new_modulo.funcion_new_modulo_main())

# Importar función desde una carpeta que está en esta misma ruta.

from main.new_modulo import funcion_new_modulo_main # Llamando la  función específica.
print(funcion_new_modulo_main())

# Bien. Esto está correcto.



# Se importará una función desde una subcarpeta.

from main.sub_main.sub_modulo import funcion_sub_modulo_sub_main
print(funcion_sub_modulo_sub_main())

# Se importará un módulo que está en una sub carpeta.

import main.sub_main.sub_modulo as mod_sub_main
print(mod_sub_main.funcion_sub_modulo_sub_main())