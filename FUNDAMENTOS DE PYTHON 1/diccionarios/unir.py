dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#2
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = dict1 | dict2 # Usando |
print(result)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#3
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

result = {**dict1, **dict2} # Desempaquetar.
print(result)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
