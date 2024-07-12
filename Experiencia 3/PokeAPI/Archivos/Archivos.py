#Importar las librerias necesarias

#Funciones para crear archivos

import csv #Excel separado por comas
import json #Parecido a diccionarios

#Crear un archivo de texto
def crear_archivo_texto(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)
    print(f"archivo: {nombre_archivo} creado exitosamente")

#Funcion para crear un archivo CSV
def crear_archivo_csv(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerows(datos)
    print(f"archivo: {nombre_archivo} creado exitosamente")

#crear un Json
def crear_archivo_json(nombre_archivo, datos):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    
    print(f"archivo JSON: {nombre_archivo} creado exitosamente")


#Leer txt
def leer_archivo_txt(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return archivo.read()
    
#Leer csv
def leer_archivo_csv(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return list(csv.reader(archivo))

#Leer json
def leer_archivo_json(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        return json.load(archivo)
    
#Agregar texto a un txt existente
def agregar_contenido_txt(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:
        archivo.write(contenido)
    print(f"Contenido agregado en: {nombre_archivo} exitosamente")


#datos txt
contenido_txt = "Este es un texto de ejemplo"

crear_archivo_texto('Ejemplo.txt', contenido_txt)


#datos de csv
datos_csv = [
    ['Nombre', 'Edad', 'Comuna'],
    ['Eduardo', 33, 'Puerto Montt'],
    ['Antonella', 18, 'Puerto Montt'],
    ['Jhon', 24, 'Puerta Sur en su casa']
]

crear_archivo_csv('Ejemplo.csv', datos_csv)

#datos json
datos_json = {
    'nombre': "Marcelo",
    'edad': 37,
    'ciudad': "Llanquihue",
    'habilidades': ['Python', 'HTML', 'CSS']
}

crear_archivo_json('Ejemplo.json', datos_json)

print(leer_archivo_txt('Ejemplo.txt'))

#Leer y mostrar el contenido de un csv
for fila in leer_archivo_csv('Ejemplo.csv'):
    print(fila)

#Leer y mostrar el contenido de un json
print("\nContenido del archivo JSON: ")
print(json.dumps(leer_archivo_json('Ejemplo.json'), indent=4))

contenido_adicional_txt = "\n Este es contenido adicional"

agregar_contenido_txt('ejemplo,txt', contenido_adicional_txt)

print(leer_archivo_txt('ejemplo.txt'))

#metodos adicionales para leer archivos
with open("ejemplo.txt", "r") as fichero:
    print("\n Contenido leido con read()")
    print(fichero.read())

#Leer un fichero linea por linea
with open('ejemplo.txt', 'r') as fichero:
    linea = fichero.readline()
    while linea != "":
        print(linea, end='')
        linea = fichero.readline()

#readlines()

with open('ejemplo.txt', 'r') as fichero:
    print("readline()")
    for linea in fichero.readlines():
        print(linea, end="")

#escribir un archivo usando write() y writelines()
lista = ["Manzanita\n", "Perita\n", "Platanito\n"]
with open('datos_guardados.txt', 'w') as fichero:
    fichero.writelines(lista)

#comunicacion entre 2 funciones usando archivos
def escribe_fichero(mensaje):
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write(mensaje)

#funcion para leer el fichero 
def lee_fichero():
    with open('fichero_comunicacion.txt', 'r') as fichero:
        mensaje = fichero.read()
    with open('fichero_comunicacion.txt', 'w') as fichero:
        fichero.write('')
    return mensaje

escribe_fichero("Este es un mensaje para fichero")
print("\n mensaje leido del fichero de comunicacion")
print(lee_fichero())