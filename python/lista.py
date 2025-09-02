numeros = [1, 10, 15, 20, 30, 40, 50, 70, 20]

def saludar (nombre):
    print ("hola python saluda", nombre)

saludar("David") 

def num (numeros):
    print (numeros)

num(numeros)

diccionario=[
    {"nombre": "David", "edad": 32,"ciudad": 'Funza'},
    {"nombre": "Pepe", "edad": 12,"ciudad": 'Bosa'},
    {"nombre": "Pablo", "edad": 5,"ciudad": 'Madrid' },
    {"nombre": "Martin", "edad": 19,"ciudad": 'Bogotá'},
    {"nombre": "Santiago", "edad": 28,"ciudad": 'Faca' },
    {"nombre": "Alejandro", "edad": 41,"ciudad": 'Lima'}]

for i in range(0, 6):
    val = diccionario[i]["nombre"] 
    print (val)


nombre = (input("Ingrese su nombre: "))
edad = (input("Ingrese su edad: "))

archivo = open("Dic.txt", "a")
archivo.write(nombre + ", " + str(edad) + "\n")
archivo.close()