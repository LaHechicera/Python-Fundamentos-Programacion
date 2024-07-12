#Calculadora IMC (indice de masa corporal)
print("-----Calculadora IMC-----")

altura = float(input("Ingrese su altura en formato 1.65: "))
peso = float(input("Ingrese su peso en formato 80: "))

imc = peso/altura**2

print("Su IMC ", imc)

print(f"Tu IMC es de: {imc: .2f}") #otra manera abreviada para redondear, al abrir esos corchetes se indica que el resultado es flotante, le decimos que despues de la coma del decimal solo se mostraran 2 numeros

cadena = "este es un texto de prueba"
total_caracteres = len(cadena)
print (total_caracteres)