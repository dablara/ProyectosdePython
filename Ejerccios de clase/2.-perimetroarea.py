# 2. Calcular el perímetro y área de un rectángulo dada su base y su altura.
print ('2. Calcular el perímetro y área de un rectángulo dada su base y su altura.')

base = int(input('Escribe la base del rectangulo '))
altura = int(input('Escribe la altura del rectangulo '))

area = base*altura
perimetro = base*2+altura*2

print (f'El are del rectangulo es {area} y el perimetro es {perimetro}')
