import random 

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


def mezclar(b):
    br = []
    i = 0
    while i < 40:
        n = random.randint(0,39)
        while b[n] in br:
            n = random.randint(0, 39)
        br.append(b[n])
        i += 1
    b[:] = br  #Sustituye todos sus índices 
    return b

def repartir(b, players, cards):
    #res = [[]]*players

    res = []     #resultado
    for p in range(players):
        res.append([])
        
    for ic in range(cards):    #ic es índice cartas
        for ij in range(players):    #ij es índice jugador
            carta = b.pop(0)
            res[ij].append(carta)
            
    return res 

def invertir(b):
    for i in range(len(b)//2):
        aux = b[i]
        b[i] = b[-1-i]
        b[-1-i] = aux