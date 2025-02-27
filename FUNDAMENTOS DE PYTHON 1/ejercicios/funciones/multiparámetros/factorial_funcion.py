def factorial_function(n):
    if n < 0: # Los número negativos no tienen definido factorial.
        return None
    if n < 2: # El factorial de 0 y 1 da 1 por definición matemática.
        return 1
    factorial = 1 # se inicia en 1 porque si no, el resultado de multiplicar cualquier número será 0
                  # y ya que que n x 1 siempre es n, laprimera iteción no afecta el resultado.
    for i in range(2, n + 1):
        factorial *= i
    return factorial

for n in range(1, 6): # probando
    print(n, factorial_function(n))