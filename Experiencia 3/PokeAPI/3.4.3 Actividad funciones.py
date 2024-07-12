
def validar_lista_numeros():
    while True:
        lista = input("Ingrese una lista de números enteros separados por espacios: ")
        try:
            lista =[int(numero) for numero in lista.split()]
            return lista
        except ValueError:
            print("Lista no valida, ingrese nuevamente: ")

lista_valida = validar_lista_numeros()

par = []
impar = []

for i in lista_valida:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print(f"Números pares: {par}")
print(f"Números impares: {impar}")
