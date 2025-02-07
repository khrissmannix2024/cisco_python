# Insertar nuevo elemento.

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.update({"pato": "canard"})
print(dictionary)

# Eliminar elemento.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

del dictionary['perro']
print(dictionary)

# Eliminar el último elemento
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary.popitem()
print(dictionary)    # salida: {'gato': 'chat', 'perro': 'chien'}

# Ordenar diccionario.
for key in sorted(dictionary.keys()):
    print(dictionary)

# Imprimir las claves.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for key in dictionary.keys():
    print(key, "->", dictionary[key])


# imprimir los valores y no las claves.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

for french in dictionary.values():
    print(french)

# reemplazar valores.
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary['gato'] = 'minou'
print(dictionary)