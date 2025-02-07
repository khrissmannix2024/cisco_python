# Crea una lista y elimina los número repetidos usando int y del.

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Crear una lista única iterando sobre los elementos
unique_list = [] 
for number in my_list: 
    if number not in unique_list: # Si no está en la lista se agrega a continuación.
        unique_list.append(number) 

print("La lista con elementos únicos:")
print(unique_list)
