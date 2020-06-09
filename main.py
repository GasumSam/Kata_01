'''
#Si importas todo en el print llamas al módulo

import cartas

print(cartas.crea_baraja())   


o 

#Si importas específicamente el módulo cartas, ya no es encesario llamarlo en el print de forma específica, ya que en este caso ya está invocado directamente cartas

from cartas import crea_baraja

print(crea_baraja())

'''

import cartas

b = cartas.crea_baraja()

manos = cartas.repartir(b, 3, 5)

print(manos)


#mensaje prueba git