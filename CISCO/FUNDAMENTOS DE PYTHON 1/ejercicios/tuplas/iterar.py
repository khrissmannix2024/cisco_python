pol_esp_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
    }

for key, value in pol_esp_dictionary.items():
    print("Pol/Esp ->", key, ":", value)

# Desempaquetar
tup = 1, 2, 3
a, b, c = tup

print(a * b * c) # Salida: 6


tup = (1, 2, 3, 4, 5)
a, *b, c = tup  # a = 1, c = 5, b = [2, 3, 4]
print(a, b, c)  # Salida: 1 [2, 3, 4] 5
