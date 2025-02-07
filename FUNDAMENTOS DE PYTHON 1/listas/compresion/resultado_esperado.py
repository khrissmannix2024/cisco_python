my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # output True
print("A" not in my_list)  # output True
print(3 not in my_list)  # output True
print(False in my_list)  # output False



# Listas comprimidas.
squares = [x ** 2 for x in range(10)] # Crea una lista con los números [0, 1, 4, 9, 4, 25, 36, 49, 54, 81]
print(squares)

twos = [2 ** i for i in range(8)] # Este es semejante pero calcula las pontencias de 2. [1,2,4,8,16,32,64,128]
print(twos)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)
