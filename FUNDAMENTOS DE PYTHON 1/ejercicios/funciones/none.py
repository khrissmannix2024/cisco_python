# Solo existen dos tipos de circunstancias en las que None se puede usar de manera segura:

# Cuando se le asigna a una variable (o se devuelve como el resultado de una función)
# Cuando se compara con una variable para diagnosticar su estado interno.

#value = None
#if value is None:
#    print("Lo siento, no contienes ningún valor")

def strange_function(n):
    if(n % 2 == 0):
        return True
print(strange_function(2))
print(strange_function(3))