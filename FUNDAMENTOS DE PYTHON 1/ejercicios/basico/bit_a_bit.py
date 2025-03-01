x = 4
y = 1

a = x & y  # 4 = 100; 1 = 001 -> 100 & 001 = 000 = 0 en decimal
b = x | y  # 4 = 100; 1 = 001 -> 100 | 001 = 101 = 5 en decimal
c = ~x  # ¡difícil! el contrario de x = -4 -1 = -5 en decimal
d = x ^ 5 # 4 = 100; 5 = 101 -> 100 ^ 101 = 001 = 1 en decimal
e = x >> 2 # 4 = 100; ...,4,2,1 son las posiciones en bits si se desplaza dos a la derecha queda en 1 bit.
f = x << 2 # 4 = 100; ...,16,8,4,2,1 son las posiciones en bits, si se desplaza dos a la izquierda queda en 16.

print(a, b, c, d, e, f)