
#Tipos de condicionales/indicar si un dato es verdadero o falso

# Condicional 1 - Igualdad
5 == 5 # Verdadero
'hola' == 'adiós' # Falso

#Condicional 2 - Desigualdad
1 != 8 # Verdadero
'python' != 'python' # Falso

#Condicional 3 - Mayor que
7 > 3 # Verdadero

#Condicional 4 - Menor que
3 < 5 # Verdadero

#Condicional 5 - Mayor o igual que
7 >= 7 # Verdadero

#Condicional 6 - Menor o igual que
3 <= 5 # Verdadero

#Conjunción (AND)
#La conjunción se entiende cuando todas las condiciones que conecta son verdaderas.

#Conjunción
edad1 = 18
tiene_licencia = True
if edad1 >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

#Disyunción (OR)
#La disyunción se entiende cuando a lo menos una de las condiciones que conecta son verdaderas.

#Disyunción
edad2 = 18
tiene_licencia = True
if edad2 >= 18 or tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

#Sintaxis
#La estructura básica if se utiliza para ejecutar un 
#bloque de código si una condición es verdadera
# Sentencia IF
#   if condicion:
	    # Código a ejecutar si la condición es verdadera

# Sentencia ELIF
#Permite evaluar condiciones adicionales si la primera 
#condición en un bloque if no es verdadera.
#   if condicion1:
	    # Código a ejecutar si la condición1 es verdadera
#   elif condicion2:
	    # Código a ejecutar si la condicion1 no es verdadera y 
	    #la condicion2 es verdadera

# Sentencia ELSE
#Se ejecuta si ninguna de las condiciones anteriores es 
#verdadera. Es opcional y se coloca al final.
#   if condicion:
	    # Código a ejecutar si la condición es verdadera
#   else:
	    # Código a ejecutar si la condición no es verdadera


edad = 18
if edad < 18:
	print("Eres menor de edad.")
elif 18 <= edad <= 40:
	print("Eres adulto joven.")
elif 41 >= edad < 65:
	print("Eres adulto.")
else:
	print("Eres un adulto mayor.")


from typing import Match
def verificar_tipo(valor: Match[int, str, float]) -> str:
    Match valor:
        case 1:
	        return "Es un número entero"
        case "texto":
	        return "Es una cadena de texto"
        case 3.14:
	        return "Es un número decimal"
        case _:
	        return "Es un tipo de dato no reconocido”

        resultado = verificar_tipo(10)
    print(resultado)

