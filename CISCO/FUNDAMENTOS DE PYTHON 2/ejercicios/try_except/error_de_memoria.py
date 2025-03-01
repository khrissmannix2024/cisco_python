# Este código causa la excepción MemoryError.
# Advertencia: el ejecutar este código puede afectar tu Sistema Operativo.
# ¡No lo ejecutes en entornos de producción!

#string = 'x'
#try:
#    while True:
#        string = string + string
#        print(len(string))
#except MemoryError:
#    print('¡Esto no es gracioso!')

# Al parecer esa tardaba mucho en terminar así que se me recomendó este otro:
try:
    my_list = [1]
    while True:
        my_list = my_list * 2  # Duplica la lista en cada iteración
        print(len(my_list))
except MemoryError:
    print('¡Esto no es gracioso!')
    del my_list