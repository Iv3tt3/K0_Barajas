from barajas import crear_baraja, barajar_for, Baraja

num = ('A', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R')
pal = ('o', 'c', 'e', 'b')

b = crear_baraja(num, pal)
print(b)
barajar_for(b)
print(b)

mi_baraja = Baraja(num, pal)
print(mi_baraja.naipes)

print(mi_baraja.repartir(2,4))