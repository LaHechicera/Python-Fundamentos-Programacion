#Conjuntos: los conjuntos de datos desordenados y no indexados de elementos únicos. Se definen utilizando llaves {} o la función set () solo cuando se utilizan letras.

#Conjunto de números
numerosPrimos = {2,3,5,7,11}

#Conjunto de letras, se declara con "set()"
lenguaje = set("Python3")

#Agregar elementos a un conjunto 
numerosPrimos.add(13)
print(numerosPrimos)

numerosPrimos.remove(7) #para eliminar un número de la lista
print(numerosPrimos)

#eliminar algo especifico de un conjunto variable declarada mas arriba
lenguaje.remove("3")
print(lenguaje)

#Diccionarios: son colecciones de datos pares mediante la logica clave: -> Valor

alumno = {
    "Nombre": "Juanito",
    "Edad": 30,
    "Beca": True,
    "Ciudad": "Puerto Monttcito",
    "Provincia": "Llanquihue",
    "Comuna": "Llanquihue",
}
print(alumno)

#Imprimir dato especifico de un diccionario
print(alumno["Ciudad"])

#Modificar un dato especifico de un diccionario
alumno["Edad"]=50
print(alumno)

#Agregar un nuevo clave: -> valor
alumno["altura"]=1.20
alumno["Nombre"]="Miguelito"
print(alumno)

#Como saber de que tipo es una variable: con type

print(type (numerosPrimos))
print(type (alumno))

#Como obtener un dato del usuario
datoUsuario= input("Ingrese un numerijillo") #string
print(datoUsuario)
print(type(datoUsuario))

#int significa entero, solo número enteros no decimales