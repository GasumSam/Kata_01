class Baraja():
    palos = ('o', 'c', 'e', 'b')
    cartas = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
    
    def __init__(self):
        self.naipes = []
        for palo in self.palos:
            for carta in self.cartas:
                naipe = carta + palo
                self.naipes.append(naipe)
                
                
    def num_naipes(self):
        return len(self.naipes)
    
    def mezclar(self):
        pass
    
    def repartir(self, players, cards):
        pass