#Comentarios de una línea (Los comentarios comienzan con "#")

""" (Comillas triple se utilizan normalmente para explicar funciones y tambien comentarios)

Comentarios de varias lineas

Que es una variable: (Son datos)
Es un espacio de memoria reservado para almacenar datos que pueden cambiar en el transcurso del programa.

Python es un lenguaje de programación dinámico, no es necesario declarar explicitamente el tipo de variable antes de utilizarla.


"""
#variables en Python:
#Deben contener letras, números o guiones bajos.
#Variables deben comensar con una LETRA no con un número.
#Case sensitive (es sensible a letras mayusculas)

variable = 1 #(Ejemplo de variable)
Variable = 1 #(esta variable es diferente solo por la mayuscula)

#No se pueden utilizar palabras reservadas para definir variable (es decir funciones con sus palabras reservadas)
#Palabras reservadas: 
"""
False, None, True, as, and, assert, await, break, class, continue, def (para definir funciones), del, elif, else, except, finally, for, from, global, if, import, in, is, lambda, nonlocal, not, or, pass, raise, try, while, with y yield. 
"""

#Tippos de datos:
entero = 2
decimalFloat = 1.5
cadenasTexto = "Hola soy una cadena shavales"

suma = 2+5
resta = 3-2
multiplicacion = 3*3
division = 10/2

#Imprimir datos con Print
print ("La suma es ",suma)
print ("La resta es ",resta)
print ("La multiplicacion es ",multiplicacion)
print ("La division es ",division)

mensaje = "Hola"
nombre = "Campo"

print (mensaje,nombre)
print (mensaje + " texto extra " + nombre)

#El "+" sirve para concatenar variables

#Booleanos
#Son True y False

edad = 18
esEstudiante = True 
estaTrabajando = False

#Operación lógica con booleanos

esMayorDeEdad = edad>=18
puedeVotar = esMayorDeEdad and estaTrabajando
print(esMayorDeEdad)
print(puedeVotar)

#Listas: Son colecciones de datos ordenados y modificables. (contienen distintos tipos de datos) Se hacen con "[]"

numeros = [1,2,3,4,5,6,7,8,9]
nombres = ["Raul", "Pedro", "Cosme Fulanito"]
mixta = [1,  "cosme", True, 1.4]

print (numeros)
print (numeros[6])
print (numeros [-3])
print (numeros[-1])

#Tuplas: son colecciones de datos ordenados e inmutables (no se puede modificar) se declaran con "()"

coordenadas = (10,20)
meses = ("Enero ","Febrero","Marzo")

print (meses)
print (meses[-1])


