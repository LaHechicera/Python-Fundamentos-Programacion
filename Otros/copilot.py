while True:
    try:
        panCiab = int(input("Ingrese cantidad de Pan Ciabatta: "))
        pieLim = int(input("Ingrese cantidad de Pie de Limon: "))
        cafe = int(input("Ingrese cantidad de cafe: "))
        te = int(input("Ingrese cantidad de té: "))
        alfajor = int(input("Ingrese cantidad de alfajor: "))

        panCiabcosto = panCiab * 2000
        pieLimcosto = pieLim * 3500
        cafecosto = cafe * 2200
        tecosto = te * 1600
        alfajorcosto = alfajor * 1000

        total = panCiabcosto + pieLimcosto + cafecosto + tecosto + alfajorcosto
        break  # Salir del bucle si la entrada es válida
    except ValueError:
        print("Favor ingrese un número válido")

print("\n-----Resumen de ventas-----")
print(f"Total Pan Ciabatta: {panCiabcosto}")
print(f"Total Pie de Limón: {pieLimcosto}")
print(f"Total Cafe: {cafecosto}")
print(f"Total té: {tecosto}")
print(f"Total Alfajores: {alfajorcosto}")
print(f"Total ventas: {total}\n")

if total >= 50000:
    print(f"Saco buena venta hoy, un total de {total}\n")
else:
    print(f"Sus ventas fueron bajas hoy, un total de {total}\n")