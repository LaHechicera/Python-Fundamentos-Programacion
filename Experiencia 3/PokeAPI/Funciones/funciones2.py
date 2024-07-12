
#CLASE SEGUNDA PARTE - 13/06/24
#Función con **kwarg
def saludo_completo(**kwargs):
    saludo = "Hola "
    for clave, valor in kwargs.items():
        saludo += f"{valor}"
    saludo += "Bienvenido a la clase de funciónes 2 "
    print(saludo)
    print(type(kwargs))

#Llamada a la fx
saludo_completo(nombre="Camila ", apellido="González ")

#Función *args (tupla) y **kwargs (diccionario)
def informacion_completa(*tupla, **diccionario):
    print("Información recibida")
    for args in tupla:
        print(f"{args}")
    for clave, valor in diccionario.items():
        print(f"Clave: {clave}, Valor: {valor}")
informacion_completa(1,2,3,4,5,6,7,8,9, nombre="Andy", comuna="Puerto Montt")

#Función que recibe argumentos más complejas
def estadisticas(*args):
    suma_total = sum(args)
    promedio = suma_total/len(args)
    maximo = max(args)
    minimo = min(args)
    return suma_total, promedio, maximo, minimo

#Llamamos a la fx
suma_total, promedio, maximo, minimo = estadisticas(10,20,30,40,50)
print(f"Suma total: {suma_total}\nPromedio: {promedio}\nMáximo: {maximo}\nMínimo: {minimo}")

#Función recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
resultado_factorial = factorial(5)
print(f"El factor de 5 es: {resultado_factorial}")

#Función anidada
def operacion_anidada(a,b):
    def suma(numero1, numero2):
        return numero1 + numero2
    def multiplicar(numero1, numero2):
        return numero1*numero2
    total_suma = suma(a,b)
    total_multiplicacion = multiplicar(a,b)
    return total_suma, total_multiplicacion

total_suma, total_multiplicacion = operacion_anidada(10,20)
print(f"La suma de 10 + 20 es: {total_suma} y la multiplicacion de 10*20 es: {total_multiplicacion}")

#Ejemplo de una fx lambda
elevar_cuadrado = lambda X: X**2
lista_de_numeros = [1,2,3,4,5]
numeros_cuadrados = list(map(elevar_cuadrado, lista_de_numeros))
print(f"Los números {lista_de_numeros} al cuadrado son {numeros_cuadrados}")