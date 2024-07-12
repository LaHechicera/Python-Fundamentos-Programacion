#Contador de vocales programa que cuente el texto que ingrese el usuario

palabras = input("Ingrese una palabra u oración: ")

a = palabras.count("a")
e = palabras.count("e")
i = palabras.count("i")
o = palabras.count("o")
u = palabras.count("u")

variable = a+e+i+o+u

print(variable)