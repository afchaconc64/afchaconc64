'''
Calcula el azimut de una línea a partir de las coordenadas (x,y) de sus puntos extremos
'''
import math # importar la librería matemática

X1= float(input('Digite la coordenada X del punto 1: '))
Y1= float(input('Digite la coordenada Y del punto 1: '))
X2= float(input('Digite la coordenada X del punto 2: '))
Y2= float(input('Digite la coordenada Y del punto 2: '))

dx= X2-X1
dy= Y2-Y1

if dy != 0: 
    rumbo = math.degrees(math.atan(dx/dy))

    if dx > 0 and dy>0: #Condición para el primer cuadrante
        azimut= rumbo
    elif dx > 0 and dy < 0: #segundo cuadrante
        azimut= 180 + rumbo
    elif dx < 0 and dy < 0: #Tercer cuadrante
        azimut= 180 + rumbo
    elif dx < 0 and dy > 0: #Cuarto cuadrante
        azimut= 360 + rumbo
    elif dx == 0 and dy > 0:
        azimut: 0
    elif dx == 0 and dy < 0:
        azimut = 180

    else:
        if dx > 0:
            azimut: 90
        elif dx < 0:
            azimut= 270
        else:
            azimut= ''
        print('No se puede calcular el azimut de un punto')

grados= int(azimut)
auxiliar= (azimut - grados)*60
minutos= int(auxiliar)
segundos= (auxiliar - minutos)*60
segundos= int(round(segundos,0))

print('El azimut de la línea es:', str(grados)+ '° '+ str(minutos)+ "' "+str(segundos)+ '"')


