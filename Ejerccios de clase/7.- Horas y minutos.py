# 7. Realiza un programa que reciba una cantidad de minutos y 
# muestre por pantalla a cuantas horas y minutos corresponde.

import math
from fractions import Fraction
minutos = int(input('Introduce un número de minutos '))

horas= minutos/60
franccion = Fraction(horas)
minu = franccion*60


print (f'{minutos} minutos son {horas} horas y {minu} minutos')
print (f'la fraccion es {franccion}')