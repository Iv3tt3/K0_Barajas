def crear_baraja(n, p):
    numeros = n
    palos = p

    baraja = []
    
    for palo in palos:
        for numero in numeros:
            naipe = numero + palo
            baraja.append(naipe)
    
    return baraja