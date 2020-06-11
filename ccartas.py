import random

class Baraja():
    palos = ('o', 'c', 'e', 'b')
    cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
    
    def __init__(self):
        self.__crea_baraja()
                
    def __crea_baraja(self):  #creo un método privado que no dejo que llamen fuera de la clase pero sí desde dos métodos
        self.naipes = []  #self. son variables de la clase, pertenecen a toda la clase
        self.mano = [] #Este atributo estaba en repartir, debo traerlo al init para poder hacerlo accesible a toda la clase
        for palo in self.palos:
            for carta in self.cartas:
                naipe = carta + palo   #Post-it  en cuanto se ejecuta el método desaparece
                self.naipes.append(naipe)
               

                
    #def num_naipes(self):
     #   return len(self.naipes)
    
    def mezclar(self):
        br = []     #br es un post-it que utilizo para colocar la baraja mezclada antes de devolverla en self.naipes(la baraja creada en __init__)
        while len(self.naipes) != len(br):
            n = random.randint(0, len(self.naipes)-1)
            while self.naipes[n] in br:
                n = random.randint(0, len(self.naipes)-1) #Al indicar len(self.naipes)-1 en vez de 39 estoy permitiendo usar la orden para barajas de distinto tamaño
            br.append(self.naipes[n])
        self.naipes[:] = br  #Sustituye todos sus índices 

    
    def repartir(self, players, cards):
        #self.mano = []   Me lo llevo a __init__ para que esté disponible en toda la clase
        for p in range(players):
            self.mano.append([])
        
        for ic in range(cards):    #ic es índice cartas
            for ij in range(players):    #ij es índice jugador
                carta = self.naipes.pop(0)
                self.mano[ij].append(carta)
                
    def recoger(self):
        self.__crea_baraja()
        