# Método paraordenar listas.

# 1. Método sorted(): Crea una nueva lista ordenada.

lista = ['omega', 'alpha', 'pi', 'gamma']
lista2 = sorted(lista)
print(lista2)

# 2. Método sort(): El segundo método afecta a la lista misma, no se crea una nueva lista

second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
    