import random

def crear_baraja(n, p):
    numeros = n
    palos = p

    baraja = []
    
    for palo in palos:
        for numero in numeros:
            naipe = numero + palo
            baraja.append(naipe)
    
    return baraja

def barajar_for(baraja):
    for i in range(len(baraja)):
        j = random.randrange(len(baraja))
        baraja[i],baraja[j] = baraja[j],baraja[i]
    return baraja

class Baraja:
    def __init__(self, numeros, palos):
        self.naipes = []
        for palo in palos:
            for numero in numeros:
                naipe = numero + palo
                self.naipes.append(naipe)
    def barajar(self):
        for i in range(len(self.naipes)):
            j = random.randrange(len(self.naipes))
            self.naipes[i], self.naipes[j] = self.naipes[j], self.naipes[i]
    
    def repartir(self, mano, jugadores):
        players = []
        for p in range(jugadores):
            players.append([])

        for num_carta in range(mano):

            for jugador in range(jugadores):
                carta = self.naipes.pop(0)
                players[jugador].append(carta)

        return players
