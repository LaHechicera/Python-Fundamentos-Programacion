#Funcion sin argumento y sin retorno
def saludo():
    """
    imprime un saludo si recibir argumento ni retorno
    """
    print("Hola Mundito")
saludo()

#Funcion sin argumentos y con retorno
def obtener_suma():
    num1 = 5
    num2 = 90
    return num1 + num2
print("resultado suma: ", obtener_suma())

#Funcion con argumento y sin retorno
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(contenido)
    print(f"Contenido guardado en {nombre_archivo}")

#agregamos los datos
nombre_archivo = input("Ingresa el nombre del archivo")
contenido = """Es el llamado Dovahkiin, que en castellano se traduce 
Sangre de dragón y en inglés, Dragonborn. Aunque en realidad da igual cómo lo digas. 
Se trata del único personaje de Skyrim capaz de derrotar de forma definitiva a un dragón, pues absorbe su alma."""

escribir_archivo(nombre_archivo, contenido)

#Funcion que recibe argumentos y devuelve un return
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as archivo:
            contenido = archivo.read()
        return contenido
    except FileNotFoundError:
        return "El archivo no fue encontrado"
    
nombre_archivo = input("Ingrese el archivo a leer: ")
contenido_archivo = leer_archivo(nombre_archivo)

print(f"Contenido de {nombre_archivo}: \n {contenido_archivo}")

#Ejemplo funcion con argumento y retorno
def contar_palabra(contenido):
    """Contar las palabras totales"""
    palabras = contenido.split() #split separa las palabras por los espacios 
    return len(palabras)

numero_palabras = contar_palabra(contenido_archivo)
print(f"El archivo: {nombre_archivo} tiene {numero_palabras} palabras")

def contar_lineas(contenido):
    lineas = contenido.split('\n')
    return len(lineas)

numero_lineas = contar_lineas(contenido_archivo)
print(f"El archivo {nombre_archivo} tiene {numero_lineas} lineas")

#Funcion que encuentre la cantidad de palabras que se repiten en una cadena
def buscar_palabra(contenido, palabra):
    return contenido.lower().split().count(palabra.lower())
palabra = input("Ingresa la palabra a encontrar: ")
aparicion = buscar_palabra(contenido, palabra)

print(f"La palabra {palabra} aparece {aparicion} veces en el archivo {nombre_archivo}")

#Esta funcion recibe una cantidad indeterminada de argumentos *args tuplas
def suna_multiple(*args):
    suma_total = 0
    print (type(args))
    for numero in args:
        suma_total += numero
    return suma_total
#llamar a la funcion
resultado_multiple = suna_multiple(1,2,3,4,5,6,7,8,9,10)
print(f"La suma de 1,2,3,4,5,6,7,8,9,10 es: {resultado_multiple}")