#inversor de cadenas texto
#Entrada/proceso/salida de datos
#Entender que las cadenas de texti pythin las interpreta como array

print("-----Texto invertido-----")
cadena = input("Ingrese palabra u oración ")
inversor = cadena[::-1] #la funcion slicing [::-1] invierte el texto que ingrese el usuario
print(f"La variable invertida es: {inversor}")

#funcion slicing : [entrada:fin:paso] se coloca -1 por que le decimos que comience desde el final del texto
