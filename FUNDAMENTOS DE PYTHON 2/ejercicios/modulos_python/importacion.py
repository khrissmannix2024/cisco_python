# Un módulo siempre que es importado se ejecuta implícitamente,
# por tanto es recomendable usar la siguiente sentencia para
# evitar ese comportamiento si así se desea.
# En otras palabras, al importar un módulo que tiene un print, por ejemplo,
# el print siempre se ejecutará a menos que se use la sentencia en cuestión.


# Sentencia:
if __name__ == "__main__": # Cuando el módulo es ejecutado directamete imprime el print.
    print("Este módulo se está ejecutando directamente.")
    # Sino: si el módulo es importado, no imprime nada.