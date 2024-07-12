
#Ciclos y bucles de repeticion

#Bucle "For" se utiliza cuando hay un numero conocido de repeticiones, se deben dar datos de inicializacion y condicion 
#Permite ejecutar una tarea un numero determinado de veces

for elemento in range(5):
    print(" No habiamos visto tanto frio como frio este año")


#Bucle "While" se utiliza mientras la condicion sea verdadera, cuando no tenemos certeza de cuando deberia acabar la condicion, o finalice cuando un dato cumpla la condicion

a = 5
while(a>0):
	print(f"el valor de a es :{a}")
	a = int(input("ingrese un valor"))
      
#Try Except
#Maneja errores en python sin detener la ejecucion del codigo

#Try
#1- Evalua porcion de codigo (se pueden colocar diferentes funciones, acepta cualquier tippo de codigo)

#Excep
#2- Maneja posibles errores

	#A- valueError: cuando se proporciona un valor inapropiado
    #B- zeroDivisionError: cuando realizamos una dicisión por 0
    #C- fileNotFoundError: cuando queremos acceder a un archivo que no existe
    #D- KeyError: cuando intentamos acceder a una clave que no existe en un diccionario
    #E- typeError: cuando los tipos de datos no existen

#finally: se ejecuta independientemente si hay o no errores

#else: se ejecuta cuando no exista error (si hay error no se ejecuta)