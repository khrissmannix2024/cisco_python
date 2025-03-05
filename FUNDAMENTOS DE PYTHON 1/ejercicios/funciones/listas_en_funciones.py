# Se puede usar listas como argumentos para funciones.
def list_sum(lst):
    s = 0

    for elem in lst:
        s += elem

    return s

#print(list_sum([5,3,1]))

# Una lista puede ser el resultado de una función.
def strange_list_fun(n): # El pará metro será el valor hasta donde itera.
    strange_list = [] # Se crea lista que se devolverá.
    
    for i in range(0, n): # Se itera desde 0 -4.
        strange_list.insert(0, i) # Se insertan valores en la pocisión 0 cada vez.
    
    return strange_list # Retorna la lista.

print(strange_list_fun(5)) # Imprime la lista [4,3,2,1,0]
# Acá el 5 se pasa como argumento, pero nunca se imprime en el cuerpo de la función.
# Lo que se imprime es el valor del return.