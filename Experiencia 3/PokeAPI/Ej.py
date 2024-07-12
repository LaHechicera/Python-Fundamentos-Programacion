secuencia = input("Ingresa una secuencia de números separados por espacios: ")
lista_numeros = [int(numero) for numero in secuencia.split()]

print(lista_numeros)



secuencia = input("Ingresa una secuencia de números separados por espacios: ")
lista_numeros = []

for numero in secuencia.split():
    lista_numeros.append(int(numero))

print(lista_numeros)