

print("Seleccione el producto a canjear")
print("1.-  Gift Card de $10.000, valor de 10.000 puntos")
print("2.-  Secadora de pelo, valor de: 25.000 puntos")
print("3.-  Disco duro portátil, valor de: 30.000 puntos")

continu = int(input("Seleccione la opción"))

sw = 1
puntos = 100000
puntos = puntos-10000
while sw==1:
    if continu==1:
      print(f"Canje exitoso, le quedan: ${puntos} puntos") 
    elif continu==2:
       puntos = puntos-25000
       print(f"Canje exitoso, le quedan: ${puntos} puntos")
    elif continu==3:
       puntos = puntos-30000
       print(f"Canje exitoso, le quedan: ${puntos} puntos")

