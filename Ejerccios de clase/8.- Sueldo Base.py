# 8. Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
# el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza 
# en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.

import math
sueldo = int(input('Introduce el suedo base '))
venta1 = int(input ('Introduce el montante de su primera venta '))
venta2 = int(input('Introduce el motante de sus segunda venta '))
venta3 = int(input ('Introduce el montante de su tercera venta '))

comisiones = 1000/venta1+venta2+venta3*3
totalsueldo = sueldo+comisiones


print (f'El sueldo base del vendedor es {sueldo}€ y gracias a las ventas que ha relizado su sueldo acciende a {totalsueldo}€')


