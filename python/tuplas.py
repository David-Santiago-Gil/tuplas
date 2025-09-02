tupla = (1, 20, 3, 40, 5, 60, 7, 80, 9, 10)
tupla2 = "Lian", "Leon", "Lina"
nuevalista = tupla
print (tupla[4])
print (tupla2)
print(nuevalista)

tupla3 = tuple([52, 87, 24, 44, 10])
ordenada = sorted(tupla3)
print (tupla3)
print (ordenada)

tupla4 = ('David', 18, 'Colomnia')
nombre, edad, nacionalidad = tupla4
print (nombre)
print (edad)
print (nacionalidad)

tupla5 = ((1, 2), (3, 4), (5, 6))
print(tupla5[2][1])


tupla6 = (7, 7, 7)
tupla7 = (7, 7, 7)

tupla8 = (6, 6, 6)
tupla9 = (2, 2, 2)


print(tupla6 == tupla7)
print(tupla6 > tupla7)
print(tupla6 < tupla7)

print(tupla8 == tupla9)
print(tupla8 > tupla9)
print(tupla8 < tupla9)