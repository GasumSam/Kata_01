palos = ('o', 'c', 'e', 'b')
cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')


def crea_baraja():  #No necesito especificar nada porque ya está definidos, si lo hiciera los recorrería
                        #Puede ser interesante cuando hay varias tuplas de datos
                            #Meter parámetros cuando tenga sentido hacerlo

    baraja = []
    
    for palo in palos:
        for carta in cartas:
            naipe = carta + palo
            baraja.append(naipe)
        
    return baraja
