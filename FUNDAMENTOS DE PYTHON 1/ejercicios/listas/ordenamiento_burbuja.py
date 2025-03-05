# Este es el ordenamiento burbuja que se usa para enseñar a ordenar comparando el valor adiacente.

Lista = [30,12,67,24,1,27,100,-5,98]
activar = True
while activar:
    activar = False
    for i in range(len(Lista)-1):
        if Lista[i] > Lista[i + 1]:
            Lista[i], Lista[i + 1] = Lista[i + 1], Lista[i]
            activar = True
    
print(Lista)

# Este es un método en Python que permite ordenar una lista con sort().
my_list = [8, 10, 6, 2, 4]
my_list.sort()
print(my_list)

# También existe este otro método llamado reverse() que se usa para invertir la lista.
lst = [5, 3, 1, 2, 4]
print(lst)

lst.reverse()
print(lst)  # output: [4, 2, 1, 3, 5]
