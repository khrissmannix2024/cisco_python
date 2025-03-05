# Así se manejan los errrores.
#try:
    #value = int(input('Ingresa un número natural: '))
    #print('El recíproco de', value, 'es', 1/value)        
#except:
    #print('No se que hacer con eso.')

#2
try:
    value = int(input('Ingresa un número natural: '))
    print('El recíproco de', value, 'es', 1/value)        
except ValueError:
    print('No se que hacer con', value)    
except ZeroDivisionError:
    print('La división entre cero no está permitida en nuestro Universo.') 