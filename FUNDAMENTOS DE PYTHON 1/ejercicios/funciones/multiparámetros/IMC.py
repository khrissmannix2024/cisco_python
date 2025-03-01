# Defina la función para calcular el indice de masa corporal.
# El peso debe indicarse en Kg y la altura em metros.

# La \ (diagonal invertida) permite continuar el código en la línea siguiente.
def IMC(peso, altura):
    if altura < 1.0 or altura > 2.5 or \
        peso < 20 or peso > 200:
        return None
    return peso / altura ** 2

# Nueva función que convierte libras a kg
def lb_to_kg(lb):
    return lb * 0.45359237

# Convertir pies y pulgadas.
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254

# Calcular solo pies sin pulgadas.
def ft_and_inch_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(IMC(peso = lb_to_kg(176), altura = ft_and_inch_to_m(5, 7)))