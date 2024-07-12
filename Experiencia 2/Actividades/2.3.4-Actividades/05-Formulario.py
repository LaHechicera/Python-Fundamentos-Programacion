
print("----Formulario----")
print("A continuación deberas responder unas preguntas referentes a \n\"DC comics\" en su mayoria del universo de Batman por cada \nrespuesta correcta obtendras puntaje (Maximo puntaje 15)")
print(" ")
print("¿Cuál es la identidad secreta de Batgirl original?")
print(" ")
print("A. Barbara Gordon")
print("B. Cassandra Cain")
print("C. Stephaine Brown")
print("D. Harley Quinn")
print(" ")
respt1 = input("Ingrese su respuesta (Ej: D) ")

if respt1 == "A":
    respt1 = 5
    print("Respuesta correcta")
elif respt1 == "B":
    respt1 = 3
    print("A pesar de que si fue una Batgirl no es la original")
elif respt1 == "C":
    respt1 = 1
    print("A pesar de que si fue una Batgirl no es la original")
else:
    respt1 = 0
    print("Harley Quinn es una antiheroe")



print(" ")
print("¿Cuál es el villano principal de Batman?")
print(" ")
print("A. Salomon Grundy")
print("B. Jim Gordon")
print("C. Joker")
print("D. Gatubela")
print(" ")
respt2 = input("Ingrese su respuesta ")

if respt2 == "A":
    respt2 = 3
    print("A pesar de que si es un villano no es el principal")
elif respt2 == "B":
    respt2 = 0 
    print("Jim Gordon es el comisionado de policia")
elif respt2 == "C":
    respt2 = 5
    print("Respuesta correcta")
else:
    respt2 = 1
    print("Gatubela es una antiheroe")

print(" ")
print("¿Que Robin murio a manos del Joker en el primer comic \"La Muerte en la Familia\"?")
print(" ")
print("A. Dick Grayson")
print("B. Stephanie Brown")
print("C. Victor Szas")
print("D. Jason Todd")
print(" ")
respt3 = input("Ingrese su respuesta ")

if respt3 == "A":
    respt3 = 3
    print("Dick Grayson fue el primer Robin pero no murio a manos del Joker")
elif respt3 == "B":
    respt3 = 0
    print("A pesar de que si fue un Robin por más tiempo fue una Batgirl")
elif respt3 == "C":
    respt3  = 1
    print("Es un villano")
else:
    respt3 = 5
    print("Respuesta correcta")

puntos = respt1+respt2+respt3

if puntos > 0 and puntos < 5:
    print("Su puntaje es ", puntos, " de 15, no sabe mucho de DC comics")
elif puntos > 6 and puntos < 10:
    print("Su puntaje es ", puntos, " de 15, no sabe mucho de DC comics")
else:
    print("Su puntaje es ", puntos, " de 15 usted sabe mucho de DC comics")

#import time
#time.sleep(segundos) => temporizador, cuenta segundos