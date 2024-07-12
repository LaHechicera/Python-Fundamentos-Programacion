print("----Inscripción para torneo de videojuegos----")
print(" \nSeleccione una opción")
print(" \n1. Inscripción a videojuegos del torneo\n2. Lista inscripciones\n3. Lista detalle por videojuego\n4. Salir")

respuesta = int(input("Ingrese su respuesta: "))

def listainscripciones(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)
    print(f"Contenido agregado en: {nombre_archivo} exitosamente")






while True:
    if respuesta == 1:
        
        nom=input("Ingrese su nombre y apellido: ").lower()
        ciudad=input("Ingrese ciudad de origen: ").lower()
        juego=input("Videojuego a inscribirse: ").lower()
        
        resp = (input("¿Desea agregar otra inscripcion?(S/N): ").lower())
        if resp == "s":
            

        inscripciones = {
                "Nombre= ": nom,
                "Ciudad= ": ciudad,
                "juego= ": juego
            }
        for key1, key2 in inscripciones.items():
            print(key1, key2)
        break

    elif respuesta == 2:
        listainscripciones('Lista inscripciones',)

